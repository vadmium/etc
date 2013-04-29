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
        
        class Completer(rlcompleter.Completer):
            def _callable_postfix(self, val, word):
                if readline.get_completion_type() == ord("\t"):
                    return word
                else:
                    return rlcompleter.Completer._callable_postfix(
                        self, val, word)
        
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
