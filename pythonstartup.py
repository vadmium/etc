from os.path import expanduser
import readline
import atexit

HISTFILE = expanduser("~/python.history")
try:
    readline.read_history_file(HISTFILE)
except EnvironmentError:
    pass
atexit.register(readline.write_history_file, HISTFILE)
del HISTFILE

import rlcompleter 
del rlcompleter
readline.parse_and_bind("tab: complete")

del expanduser
del readline
del atexit
