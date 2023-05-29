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
    try:
        subprocess.call(["sudo", "apt-get", "update"], 
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT)
        time.sleep(1)
    except:
        print("System update failed.")

def install_python2():
    python2_commands = ["apt install -y python2.7", 
                        "apt install -y python-pip python-setuptools build-essential python2.7-dev"]
    
    try:
        subprocess.call(["apt", "install", "-y", "python2.7"],stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT )
        subprocess.call(["apt", "install", "-y", "python-pip", "python-setuptools", "build-essential", "python2.7-dev" ],stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT )
    except:
        print("Cloning volatility failed.")

def clone_volatility():
    pass

def install_volatility():
    pass

def clone_and_install() -> bool:
    print("Installing volatility.")
    commands = ["python2 -m pip install distorm3", "python2 -m pip install pycrypto",
                "git clone https://github.com/volatilityfoundation/volatility", 
                "sudo mv volatility/ /opt"]
    
    for fcmd in commands:
        try:
            os.system(f"{fcmd}")
        except IOError:
            print("Incorrect system priveledges. Please run with sudo")
        except Exception as e:
            print(f"{e}")

    print(f"[+] VOL2 Should be installed.\nCheck /opt dir")
    return True


def install_volatility2():
    update()
    install_python2()
    clone_and_install()
    
def main():
    try:
        install_volatility2()
    except:
        print(f"Failed to Execute {__name__}\nExiting...")
    raise SystemExit

if __name__ == "__main__":
    main()
