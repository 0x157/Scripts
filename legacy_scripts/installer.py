#!/usr/bin/env python3

"""
Author: 0x157
Description: A script used to install a number of usefull hacking tools. A consolidated version of install_vol2.py and linux_script.py.
Version: 1.1
Last Updated By: Alternative Al
"""

import subprocess, requests, os, sys, random
import progressBar
from time import sleep
from urllib import request
import time

# Global variables
PYTHON = subprocess.check_output(["python3", "--version"])
PIP = subprocess.check_output(["pip3", "--version"])

# Global Links
GITHUB = "https://www.github.com"
GHIDRA = "https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.1.5_build/ghidra_10.1.5_PUBLIC_20220726.zip"
ADA = "https://out7.hex-rays.com/files/idafree82_linux.run"

### 
# Functions for updating system
###
def check_root():
    """
    Checks permissions to see if you are a root user. Returns a bool.
    """
    if os.geteuid() != 0:
        return False
    return True


def check_connection(link):
    """
    Checks to see if you can connect to a link, link. Returns a bool. 
    """

    try:
        request.urlopen(link, timeout=1)
        return True
    except request.URLError as err: 
        return False
        
def updating():
    """
    Updating Linux System Hooks. Returns a bool.
    """

    try:
        subprocess.call(["sudo", "apt-get", "update", "-y"], 
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT) # subproccess.call used to produce no output.
        return True
    except:
        raise SystemExit

### 
# Functions for installing python
###
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
        return True
    except:
        raise SystemExit

def install_python3():
    """
    A function made to install python3. Takes no arguments. Returns bool.
    """

    checking_py_version = PYTHON[:8:].decode("utf-8")
    version_py = checking_py_version.strip()
    if version_py == "Python 3":                
        user_version = PYTHON[:13:].decode("utf-8")
        sleep(2)
    else:
        subprocess.call(["apt", "install", "-y", "python3"],stdout=subprocess.DEVNULL, 
                        stderr=subprocess.STDOUT ) # subproccess.call used to produce no output.
    return True

def check_pip():
    """
    Checks if pip3 is installed. Returns a boolean.
    """

    check_version = PIP[:3:].decode("utf-8")
    final_pip = check_version.strip()

    if final_pip == "pip":
        sleep(2)
        return True
    else:
        return False

def install_pip():
    """
    A function for installing pip for python3. Returns a bool.
    """

    try:
        if (check_pip() != True):
            print(f"[ + ] Installing Python3 PIP")
            subprocess.call(["apt", "install", "python3-pip", "-y"])
            os.system("clear")
            return True
    except:
        sleep(2)
        raise SystemExit

def install_packages():
    """
    A function for installing all required python packages. Returns a bool
    """

    modules = [
                "bs4","requests","cursor","rich","selenium","scapy", "pyarmor", "python-nmap", 
                "cryptography", "yara", "pywal"
                ]
    try:
        for i in range(len(modules) -1 ):
            subprocess.call(["pip", "install", f"{modules[i]}", "--user"],stdout=subprocess.DEVNULL, 
                        stderr=subprocess.STDOUT )
        return True            
    except Exception as error:
        print(f"[-] Could not Install Modules\nReason --> {str(error)} <--")
        sleep(5)
        return False

###
# Functions to install JDK.
###
def jdk_11():
            
            try:
                subprocess.call(["apt", "install", "openjdk-11-jdk", "-y"],stdout=subprocess.DEVNULL, 
                        stderr=subprocess.STDOUT )
                sleep(3)
                return True
            except Exception as error:
                raise error
###
# Functions to get and unpack packages.
###
def unzip(path):
    """
    Unpacks a zip file at path, path. Returns the path of the unzipped file.
    """

    subprocess.call(["unzip", path],
                        stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return True

def get_package(link):
    """
    A function made to get a git repository from url, link. Returns bool.
    """

    try:
        subprocess.call(["git", "clone", link],
                        stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) # subproccess.call used to produce no output.
        return True
    except IOError:
            print("Incorrect system priveledges. Please run with sudo")
    except Exception as e:
            print(f"{e}")
            raise SystemExit

def clone_volatility():
    """
    Clones the volatility repository. Returns a bool.
    """

    try:
        subprocess.call(["git", "clone", "https://github.com/volatilityfoundation/volatility"],
                        stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) # subproccess.call used to produce no output.
        return True
    except IOError:
            print("Incorrect system priveledges. Please run with sudo")
    except Exception as e:
            print(f"{e}")
            raise SystemExit

### 
# Functions to install tools.
###
def install_unzip():
    """
    A funciton to install unzip. Returns a bool.
    """

    subprocess.call(["apt", "install", "unzip"],stdout=subprocess.DEVNULL, 
                        stderr=subprocess.STDOUT )
    return True

def install_curl():
    """
    A funciton to install curl. Returns a bool.
    """

    subprocess.call(["apt", "install", "curl"],stdout=subprocess.DEVNULL, 
                        stderr=subprocess.STDOUT )
    return True

def install_wget():
    """
    A funciton to install wget. Returns a bool.
    """

    subprocess.call(["apt", "install", "wget"],stdout=subprocess.DEVNULL, 
                        stderr=subprocess.STDOUT )
    return True

def install_ada():
    """
    A function to install Ada. Returns a bool.
    """

    subprocess.call(["wget", ADA], stdout=subprocess.DEVNULL, 
                        stderr=subprocess.STDOUT)
    return True

def install_ghidra():
    """
    A function to install Ghidra. Returns a bool.
    """
    subprocess.call(["wget", GHIDRA], stdout=subprocess.DEVNULL, 
                        stderr=subprocess.STDOUT)
    unzip("ghidra_10.1.5_PUBLIC_20220726.zip")
    remove_repo("ghidra_10.1.5_PUBLIC_20220726.zip")
    return True

def install_volatility():
    """
    Instals volatility. Returns true.
    """

    get_package("https://github.com/volatilityfoundation/volatility")
    subprocess.call(["sudo", "mv", "volatility/", "/opt"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) # subproccess.call used to produce no output.
    remove_repo("volatility")
    return True

def install_hack_kit(tools):
    """
    A function to install hacking tools that can be installed through 'apt-get install'. 
    Installs from an array of tools called tools. Returns a bool.
    """
    pBar = progressBar.progressBar("Initializing Tools Array")
    pBar.start()
    for program in tools:
        pBar.setMsg("Installing " + program)
        try:
            subprocess.call(["sudo", "apt", "install", f"{program}", "-y"], stdout=subprocess.DEVNULL, 
                        stderr=subprocess.STDOUT)
        except Exception as Error:
            pass  
    pBar.stop()
    time.sleep(0.2)
    return True

### 
# Post and Post Instlation Functions.
###
def remove_repo(path):
    """
    A function to remove a folder at path path. Returns a bool.
    """

    subprocess.call(["sudo", "rm", "-rf", path],
                    stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return True

def remove_dependencies():
    """
    A function that removes all unnessacary dependencies. Returns bool.
    """

    try:
        sleep(3)
        subprocess.call(["apt", "autoremove", "-y"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        return True

    except Exception as error:
        print(f"[ {error} ] \nAn ERROR has Occured Removing Unwanted Dependencies\nExiting...")
        sleep(2)
        raise SystemExit