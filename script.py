#!/usr/bin/env python3

import subprocess, requests
import os, sys
from datetime import datetime
from time import sleep


now = datetime.now()
current = now.strftime(f"%H:%M")
uid = os.getuid()


def check_connection() -> bool:
    link = f"https://www.github.com"
    
    r = requests.get(link)
    http_status_code = r.status_code

    if http_status_code != 200:
        print(f"You are not connected\nExiting...")
        raise SystemExit

    else:
        print("[ + ] Connected")
        return True


def load():
    spin = ["\33[0;92m▰▱▱▱▱▱▱", "\33[0;92m▰▰▱▱▱▱▱", "\33[0;92m▰▰▰▱▱▱▱", "\33[0;92m▰▰▰▰▱▱▱", "\33[0;92m▰▰▰▰▰▱▱", "\33[0;92m▰▰▰▰▰▰▱", "\33[0;92m▰▰▰▰▰▰▰"]
    num = 0x0
    while num != 0x7:
        sys.stdout.write(f"[\33[33m{spin[num]}\33[39m] Preparing for Installation {current}")
        sys.stdout.flush()
        sys.stdout.write("\r")
        sleep(0.3)
        num += 0x1
        if num == 0x7:
            os.system("clear")
            pass


def check_root():
        
    print(f"Checking for root\n")

    if not "SUDO_UID" in os.environ.keys() and uid != 0:
        print(f"[ \33[31m{current}\33[39m ] You must run this script with ROOT")
        raise SystemExit 

    else:
        os.system("clear")
        pass


def updating():
    try:
        print("Updating Repositories")
        subprocess.call(["apt", "update", "-y"])
        subprocess.call(["apt", "upgrade", "-y"])
        os.system("clear")
        print(f"[ {current} ] Updated Repositories")
        sleep(2)
        
    except:
        print(f"[X] Could Not Update Repositories") 


class InstallingPython:
    def __init__(self):
        try:
            PYTHON = subprocess.check_output(["python3", "--version"])
            checking_py_version = PYTHON[:8:].decode("utf-8")
            version_py = checking_py_version.strip()

            if version_py == "Python 3":
                user_version = PYTHON[:13:].decode("utf-8")
                print(f"You Already Have {user_version} Installed.")
                sleep(2)
               
        except:
             print("Python3 Was Not Found")
             os.system("clear")
             subprocess.call(["apt", "install", "python3"])
             print(f"Installed Python3")
        

        def installing_pip():
            try:
                print(f"Installing Python3 PIP")
                subprocess.call(["apt", "install", "python3-pip"])
                os.system("clear")
                print("Installed Python3 Pip")
                
            except:
                print(f"[ X ] Could Not install Python3 PIP\nExiting...") 
                sleep(2)
                raise SystemExit


        @staticmethod
        def check_pip():
            try:
                PIP = subprocess.check_output(["pip3", "--version"])
                check_version = PIP[:3:].decode("utf-8")
                final_pip = check_version.strip()

                if final_pip == "pip":
                    print("You already have PIP3 installed")
                    sleep(2)
                
            except:
                print("Did Not Find PIP\nTrying to Install...")
                installing_pip()


        check_pip()
            

    def installing_modules(self):
        clearing = lambda: os.system("clear")

        def installing_packages() -> None:
            clearing() 
            modules = [
                "bs4","requests","cursor","rich","selenium","scapy", "pyarmor", "python-nmap", 
                "cryptography", "yara"
                ]
            number = 0x0

            try:
                while number != 10:
                    subprocess.call(["pip", "install", f"{modules[number]}"])
                    number += 0x1

                    if number == 0xA:
                        clearing()
                        print(f"[\33[36m***\33[39m] Done Installing {number} Modules [\33[36m***\33[39m]")
                        sleep(5)
                        clearing()
                         

            except Exception as error:
                print(f"Could not Install Modules\nReason --> {str(error)}")
                sleep(5)
                pass


        installing_packages()



def getting_ghidra():
    LINK = f"https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.1.5_build/ghidra_10.1.5_PUBLIC_20220726.zip"
    
    try:
        os.system("clear")
        print(f"[ * ] Trying to Get Ghidra")
        sleep(2)
        subprocess.call(["wget", "install" ,f"{LINK}"])

    except:
        print("[ X ] Something Went Wrong Getting The Download")
    


def installing_ghidra() -> bool:
    global clearing
    clearing = lambda: os.system("clear")

    try:
        def jdk_11():
            try:
                subprocess.call(["apt", "install", "openjdk-11-jdk", "-y"])
                clearing()
                sleep(3)
                print(f"Installed JDK-11\n[ + ] Everything Is OK")

            except Exception as error:
                print(f"Could Not Install JDK --> {str(error)}")

        jdk_11()


        def check_directory():
            CALL = subprocess.check_output(["pwd"])
            current = CALL[::].decode("utf-8").strip()
            usr = os.getlogin()

            if current != f"/home/{usr}/Downloads":
                clearing()
                print(f"You are currently located at {current}\nMoving Directories...")
                sleep(3)
                try:
                    os.chdir(f"/home/{usr}/Downloads")
                    print(f"Moved to the proper Directory...\nGetting GHIDRA....")
                    sleep(2)
                    getting_ghidra()

                except:
                    print(f"Cannot Change Directories\nPassing....")

            else:
                print(f"You are in the proper directory\nGetting GHIDRA....")
                getting_ghidra()


        check_directory()

        return True

    except:
        print(f"[ X ] Could Not install JDK or Move Directories")
        return False


def unpacking_ghidra() -> str:

    def unzip():
        subprocess.call(["apt", "install", "unzip"])

    unzip()

    try:
        print(f"[ * ] Trying to Unpack Ghidra")
        subprocess.call(["unzip", "ghidra_10.1.5_PUBLIC_20220726.zip"])

    except:
        print("[ X ] Could not Unpack Ghidra")


def final_ghidra_function():
    def check_for_ghidra():
        usr = os.getlogin()
        clearing = lambda: os.system("clear")
        FILES = subprocess.check_output(["ls", f"/home/{usr}/Downloads"])
        check = FILES[::].decode("utf-8").strip()
        ghidra = f"ghidra_10.1.5_PUBLIC_20220726.zip"
        
        if ghidra in check:
            print("Ghidra is present")
            clearing()
            print(f"Trying to install JDK-11")
            clearing()
            unpacking_ghidra()
            os.system("clear")
            sleep(5)
            print("[ + ] Successfully Installed Ghidra\nCheck ~/Downloads Directory")


        else:
            print(f"Could Not Find Ghidra")
            installing_ghidra()
            unpacking_ghidra()
            sleep(5)
            print("[ + ] Successfully Installed Ghidra\nCheck ~/Downloads Directory")


    check_for_ghidra()


def installing_tools():
    try:
        os.system("clear")
        print(f"[ + ] Trying to install Tools")
        
        subprocess.call(["apt", "install", f"medusa", "-y"])
        subprocess.call(["apt", "install", f"apache2", "-y"])
        subprocess.call(["apt", "install", f"john", "-y"])
        subprocess.call(["apt", "install", f"proxychains4", "-y"])
        subprocess.call(["apt", "install", f"hashcat", "-y"])
        subprocess.call(["apt", "install", f"nmap", "-y"])
        subprocess.call(["apt", "install", f"ncat", "-y"])
        subprocess.call(["apt", "install", f"aircrack-ng", "-y"])
        subprocess.call(["apt", "install", f"autopsy", "-y"])

    except:
        print("[ X ] Could Not Install Certain T00LS")


def removing_unwanted() -> bool:
    clear = lambda: os.system("clear")
    try:
        subprocess.call(["apt", "autoremove", "-y"])
        sleep(1)
        clear()
        return True

    except Exception as error:
        print(f"[ {error} ] An ERROR has Occured\nExiting...")
        sleep(2)
        raise SystemExit 


def main() -> None: 
    load()
    check_root()
    check_connection()
    updating()
    py = InstallingPython()
    py.installing_modules()
    final_ghidra_function()
    installing_tools()
    removing_unwanted()


if __name__ == "__main__":
    print(f"Executing --> \33[32m{__name__}\33[39m")
    sleep(2)
    os.system("clear")
    main()
    print(f"[ {current} ] Ev3rything W3NT W3LL")
