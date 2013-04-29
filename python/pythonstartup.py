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
        import atexit
        from functools import partial
        
        HISTFILE = expanduser("~/python.history")
        try:
            readline.read_history_file(HISTFILE)
        except EnvironmentError:
            pass
        
        global history_write
        history_write = partial(readline.write_history_file, HISTFILE)
        atexit.register(history_write)
        
        import rlcompleter
        readline.parse_and_bind("tab: complete")
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
                
                # Want Python 3's tokenize(), or generate_tokens() from
                # before Python 3. Functions of both names may exist in both
                # versions, which makes it hard to detect the appropriate
                # version.
                if hasattr(tokenize, "ENCODING"):  # Python 3
                    from io import BytesIO
                    io = BytesIO(line[:i].encode())
                    gen = tokenize.tokenize(io.readline)
                else:  # Python < 3
                    from cStringIO import StringIO
                    io = StringIO(line[:i])
                    gen = tokenize.generate_tokens(io.readline)
                while True:
                    type, string = next(gen)[:2]
                    if type == tokenize.ENDMARKER:
                        break
                    if string != "import":
                        continue
                    
                    packages = list()
                    while True:
                        type, string = next(gen)[:2]
                        if type == tokenize.ENDMARKER:
                            matches = list()
                            for match in self.import_list(packages, prefix):
                                if match.startswith(text):
                                    matches.append(match)
                            return matches
                        if string.isspace():
                            continue  # Skip trailing whitespace at EOF error
                        if type != tokenize.NAME:
                            break
                        packages.append(string)
                        _, string = next(gen)[:2]
                        if string != ".":
                            break
                
                matches = default(self, text)
                self.edit_keywords(matches)
                return matches
            
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
        
        readline.set_completer(Completer().complete)
    
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

if __name__ == "__main__":
    pythonstartup()
    del pythonstartup
