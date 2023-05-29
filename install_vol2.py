"""
Author: 0x157
Description: A python script made to instal volatility2 on Linux Systems. 
Script needs to be ran with super user priveledges.
"""

import os
import subprocess
import progressBar
import time

def update():
    """
    Updating Linux System Hooks. No returns.
    """

    try:
        subprocess.call(["sudo", "apt-get", "update"], 
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT) # subproccess.call used to produce no output.
        time.sleep(1)
    except:
        print("System update failed.")
        raise SystemExit

def install_python2():
    """
    Installs python2 and requiried volatility2 dependencies. No returns.
    """

    try:
        subprocess.call(["apt", "install", "-y", "python2.7"],stdout=subprocess.DEVNULL, 
                        stderr=subprocess.STDOUT ) # subproccess.call used to produce no output.
        subprocess.call(["apt", "install", "-y", "python-pip", "python-setuptools", "build-essential", "python2.7-dev" ],
                        stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT )
        subprocess.call(["python2", "-m", "pip", "install", "dirstorm3"] ,
                        stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT )
        subprocess.call(["python2", "-m", "pip", "install", "pycrypto"] ,
                        stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT )
    except:
        print("Cloning installing python dependencies failed.")
        raise SystemExit

def clone_volatility():
    try:
        subprocess.call(["git", "clone", "https://github.com/volatilityfoundation/volatility"],
                        stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) # subproccess.call used to produce no output.
    except IOError:
            print("Incorrect system priveledges. Please run with sudo")
    except Exception as e:
            print(f"{e}")
            raise SystemExit

def install_volatility():
    subprocess.call(["sudo", "mv", "volatility/", "/opt"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) # subproccess.call used to produce no output.

def main():
    pBarUpdate = progressBar.progressBar("Updating System Hooks.")
    pBarPython = progressBar.progressBar("Installing Python2 Dependencies.")
    pBarClone = progressBar.progressBar("Installing Volatility.")
    try:
        # Updates System Hooks
        pBarUpdate.start()
        update()
        pBarUpdate.stop()
        time.sleep(1)

        # Updates Python
        pBarPython.start()
        install_python2()
        pBarPython.stop()
        time.sleep(1)

        # Installs volatility2
        pBarClone.start()
        clone_volatility()
        install_volatility()
        pBarClone.stop()
        time.sleep(1)
        print(f"\n[+] VOL2 Should be installed.\n[+] Check /opt dir")
    except:
        print(f"Failed to Execute {__name__}\nExiting...")
        raise SystemExit

if __name__ == "__main__":
    main()
