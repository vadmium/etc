def pythonstartup():
    from os.path import expanduser
    import readline
    import atexit
    from functools import partial
    import sys
    
    try:
        import builtins
    except ImportError:
        import __builtin__ as builtins
    
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
