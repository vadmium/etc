def pythonstartup():
    from os.path import expanduser
    import readline
    import atexit
    
    HISTFILE = expanduser("~/python.history")
    try:
        readline.read_history_file(HISTFILE)
    except EnvironmentError:
        pass
    atexit.register(readline.write_history_file, HISTFILE)
    
    import rlcompleter 
    readline.parse_and_bind("tab: complete")

if __name__ == "__main__":
    pythonstartup()
    del pythonstartup
