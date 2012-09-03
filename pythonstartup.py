def pythonstartup():
    from os.path import expanduser
    import readline
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

if __name__ == "__main__":
    pythonstartup()
    del pythonstartup
