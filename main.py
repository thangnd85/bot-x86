# import pdb
from helper import *
import signal
import execute
import sys
signal.signal(signal.SIGTSTP, execute.handler)
signal.signal(signal.SIGINT, execute.signal_handler)
import dem
import threading
import time
#os.system('pulseaudio --start')
dem.mainloop()

