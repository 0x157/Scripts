"""
Author: Alternative Al
Description: A simple python loading bar for activities.
"""

import subprocess
import time, sys
import threading

class progressBar(threading.Thread):
    def __init__(self, message):
         super(progressBar, self).__init__()
         self.kill = False
         self.done = False
         self.message = message
    
    def setMsg(self, msg):
         self.message = msg
         sys.stdout.flush()
         sys.stdout.write(msg)


    def run(self):
            print(self.message),
            sys.stdout.flush()
            i = 0
            while self.done != True:
                    if (i%4) == 0: 
                        sys.stdout.write('\b/')
                    elif (i%4) == 1: 
                        sys.stdout.write('\b-')
                    elif (i%4) == 2: 
                        sys.stdout.write('\b\\')
                    elif (i%4) == 3: 
                        sys.stdout.write('\b|')

                    sys.stdout.flush()
                    time.sleep(0.2)
                    i+=1

            if self.kill == True: 
                print ('\b\b\b\b ABORT!'),
            else: 
                print('\b\b\bDone!')
    
    def stop(self):
         self.done = True

    def abort(self):
         self.kill = True