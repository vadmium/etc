def pythonstartup():
    import sys
    
    try:  # Python 3
        import builtins
    except ImportError:  # Python < 3
        import __builtin__ as builtins
    
    try:
        import readline
    except ImportError:
        pass  # readline not normally available on Windows
    else:
        from os.path import expanduser
        from functools import partial
        
        HISTFILE = expanduser("~/python.history")
        
        global history_write
        history_write = partial(readline.write_history_file, HISTFILE)
        
        import rlcompleter
        import tokenize
        
        def excepthook(func):
            from functools import wraps
            import sys
            @wraps(func)
            def wrapper(*pos, **kw):
                try:
                    return func(*pos, **kw)
                except:
                    sys.excepthook(*sys.exc_info())
                    raise
            return wrapper
        
        class Completer(rlcompleter.Completer):
            def _callable_postfix(self, val, word):
                if readline.get_completion_type() == ord("\t"):
                    return word
                else:
                    return rlcompleter.Completer._callable_postfix(
                        self, val, word)
            
            def global_matches(self, text):
                return self.get_matches(text,
                    rlcompleter.Completer.global_matches)
            def attr_matches(self, text):
                return self.get_matches(text,
                    rlcompleter.Completer.attr_matches)
            @excepthook
            def get_matches(self, text, default):
                # Chop off any unfinished token at the cursor
                line = readline.get_line_buffer()
                i = readline.get_endidx()
                while i > 0:
                    c = line[i - 1]
                    if not c.isalnum() and c != "_" and ord(c) < 128:
                        break
                    i -= 1
                prefix = line[readline.get_begidx():i]
                
                gen = self.tokenize(line[:i])
                func = None  # Current function name in expression
                
                # Stack of function names being called for each bracket, or
                # None for other bracket instances
                bracket_funcs = list()
                
                while True:
                    type, string = next(gen)[:2]
                    if type == tokenize.ENDMARKER:
                        break
                    if string == "import":
                        packages = list()
                        while True:
                            type, string = next(gen)[:2]
                            if type == tokenize.ENDMARKER:
                                matches = list()
                                for match in self.import_list(packages,
                                prefix):
                                    if match.startswith(text):
                                        matches.append(match)
                                return matches
                            if type != tokenize.NAME:
                                break
                            packages.append(string)
                            _, string = next(gen)[:2]
                            if string != ".":
                                break
                    else:
                        if string == "(":
                            bracket_funcs.append(func)
                        if string in set("[{"):
                            bracket_funcs.append(None)
                        if string in set(")]}"):
                            del bracket_funcs[-1:]  # Pop if not empty
                        
                        if type == tokenize.NAME:
                            func = string
                        else:
                            func = None
                        
                        # Could next token be a function parameter?
                        param = string in set("(,")
                
                matches = default(self, text)
                self.edit_keywords(matches)
                
                if bracket_funcs:
                    func = bracket_funcs[-1]
                    if func and param:
                        if func in self.namespace:
                            func = self.namespace[func]
                        else:
                            func = getattr(builtins, func, None)
                        for arg in self.arg_list(func):
                            if arg.startswith(text):
                                matches.append(arg + "=")
                
                return matches
            
            def tokenize(self, code):
                # Want Python 3's tokenize(), or generate_tokens() from
                # before Python 3. Functions of both names may exist in both
                # versions, which makes it hard to detect the appropriate
                # version.
                if hasattr(tokenize, "ENCODING"):  # Python 3
                    from io import BytesIO
                    gen = tokenize.tokenize(BytesIO(code.encode()).readline)
                else:  # Python < 3
                    from cStringIO import StringIO
                    gen = tokenize.generate_tokens(StringIO(code).readline)
                
                while True:
                    try:
                        token = next(gen, (tokenize.ENDMARKER, None))
                    except Exception:
                        continue
                    (type, string) = token[:2]
                    # Skip trailing whitespace at EOF error
                    if type != tokenize.ERRORTOKEN or not string.isspace():
                        yield (type, string)
            
            def edit_keywords(self, matches):
                if readline.get_completion_type() == ord("?"):
                    return
                
                # Add a space to keywords when good style says they would
                # always have a space
                from keyword import kwlist
                spaced = {
                    "and", "as", "assert", "class", "def", "del", "elif",
                    "exec", "for", "from", "global", "if", "import", "in",
                    "is", "nonlocal", "not", "or", "while", "with",
                }.intersection(kwlist)
                for (i, match) in enumerate(matches):
                    if match in spaced:
                        matches[i] += " "
            
            def import_list(self, packages, prefix):
                import pkgutil
                
                # Confirm each element is a package before importing it
                name = ""
                for package in packages:
                    name += package
                    module = sys.modules.get(name)
                    if module:
                        if not hasattr(module, "__path__"):  # Not a package
                            return
                    else:
                        loader = pkgutil.find_loader(name)
                        if not loader:
                            return
                        is_package = getattr(loader, "is_package", None)
                        if not is_package or not is_package(name):
                            return
                    name += "."
                
                if not packages:
                    path = None
                else:
                    if not module:
                        package = name[:-1]  # Avoid trailing dot
                        module = loader.load_module(package)
                    path = module.__path__
                
                indicator = readline.get_completion_type() != ord("\t")
                for (_, name, ispkg) in pkgutil.iter_modules(path, prefix):
                    if indicator and ispkg:
                        name += "."
                    yield name
            
            def arg_list(self, func):
                try:  # Python 3
                    from inspect import getfullargspec as getargspec
                except ImportError:  # Python < 3
                    from inspect import getargspec
                try:
                    argspec = getargspec(func)
                except TypeError:
                    return ()
                return argspec.args + getattr(argspec, "kwonlyargs", list())
        
        readline.set_completer(Completer().complete)
        
        if __name__ == "__main__":
            try:
                readline.read_history_file(HISTFILE)
            except EnvironmentError:
                pass
            import atexit
            atexit.register(history_write)
            readline.parse_and_bind("tab: complete")
    
    # Monkey-patch SystemExit() so that it does not exit the interpreter
    class SystemExit(BaseException):
        def __init__(self, code=None):
            self.code = code
            BaseException.__init__(self, code)
    builtins.SystemExit = SystemExit
    
    def exit(code=None):
        global SystemExit
        raise SystemExit(code)
    sys.exit = exit
    
    if __name__ != "__main__":
        globals().update(locals())
pythonstartup()
del pythonstartup
