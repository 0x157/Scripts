#!/usr/bin/env python3

import subprocess, requests
import os, sys
from datetime import datetime
from time import sleep
import getpass


now = datetime.now()
current = now.strftime(f"%H:%M")
uid = os.getuid()


def check_connection() -> bool:
    
    link = f"https://www.github.com"
    
    r = requests.get(link)
    http_status_code = r.status_code

    if http_status_code != 200:
        print(f"\n[ - ] You are not connected\nExiting...")
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
        sleep(0.25)
        num += 0x1

        if num == 0x7:
            os.system("clear")
            pass


def check_root():
        
    print(f"[ *** ] Checking for root [ *** ] ")

    if not "SUDO_UID" in os.environ.keys() and uid != 0:
        print(f"\n[ \33[31m{current}\33[39m ] You must run this script with ROOT\n")
        raise SystemExit 

    else:
        print(f"\n[ + ] You are ROOT [ + ] ")
        sleep(3)
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
        print(f"\n[ X ] Could Not Update Repositories\nPassing ...\n") 
        pass


class InstallingPython:
    def __init__(self):
        try:
    
            PYTHON = subprocess.check_output(["python3", "--version"])
            checking_py_version = PYTHON[:8:].decode("utf-8")
            version_py = checking_py_version.strip()

            if version_py == "Python 3":
                
                user_version = PYTHON[:13:].decode("utf-8")
                print(f"[ + ] You Already Have {user_version} Installed.")
                sleep(2)
               
        except:
             
             print(f"[ - ] Python3 Was Not Found")
             os.system("clear")
             subprocess.call(["apt", "install", "python3"])
             print(f"Installed Python3")
        

        def installing_pip():
    
            try:

                print(f"[ + ] Installing Python3 PIP")
                subprocess.call(["apt", "install", "python3-pip", "-y"])
                os.system("clear")
                print("[ *** ] Installed Python3 Pip [ *** ]")
                
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
                    print("[ + ] You already have PIP3 installed")
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
                "cryptography", "yara", "pywal"
                ]
            number = 0x0

            try:
                while number != 11:
                    subprocess.call(["pip", "install", f"{modules[number]}", "--user"])
                    number += 0x1

                    if number == 0xB:
                        clearing()
                        print(f"[\33[36m***\33[39m] Done Installing {number} Modules [\33[36m***\33[39m]")
                        sleep(5)
                        clearing()
                         
                    
            except Exception as error:
                print(f"Could not Install Modules\nReason --> {str(error)} <--")
                sleep(5)
                pass


        installing_packages()
  


def installing_brave() -> None:

    commands = """

    sudo apt install curl;

    sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg;

    echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list;

    sudo apt update;

    sudo apt install brave-browser -y

    """


    os.system(commands)

    sleep(5)
    
    print("[+] Installed Brave")
    
    

def installing_ida():
    
    LINK = "https://out7.hex-rays.com/files/idafree82_linux.run"
    
    user = getpass.getuser()
    
    wanted_dir = f"/home/{user}/Downloads"
    
    CURRENT_DIR = subprocess.check_output(["pwd"])
    DCURRENT_DIR = CURRENT_DIR.decode('utf-8').strip("\n")
   

    if DCURRENT_DIR != wanted_dir:

        try:
            print(f"Current DIR --> {DCURRENT_DIR}\nChanging Directory")
            
            os.chdir(f"{wanted_dir}")

            check_c = subprocess.check_output(["pwd"])
            check_f = check_c.decode('utf-8').strip(f"\n")


            if check_f == wanted_dir:

                print(f"[+] Directory Changed, Installing IDA")

                os.system("clear")

                sleep(1)

                subprocess.call(["wget", f"{LINK}"])


            else:
                print(f"Could Not Change To The Proper Directory.")  

                raise SystemExit
            

        except Exception as Error:
            print(f"{str(Error)}")
   
     

def getting_ghidra():
    LINK = f"https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.1.5_build/ghidra_10.1.5_PUBLIC_20220726.zip"
    
    try:
        os.system("clear")
        print(f"[ * ] Trying to Get Ghidra")
        sleep(2)
        subprocess.call(["wget", f"{LINK}"])

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
            print(" [ + ] Ghidra is present")
            clearing()
            unpacking_ghidra()
            os.system("clear")
            sleep(5)
            print("[ + ] Successfully Installed Ghidra\nCheck ~/Downloads Directory")


        else:
            print(f"[ - ] Could Not Find Ghidra [ - ]")
            sleep(3)
            installing_ghidra()
            unpacking_ghidra()
            sleep(5)
            print("[ + ] Successfully Installed Ghidra\nCheck ~/Downloads Directory")


    check_for_ghidra()


def installing_tools():
   
    try:
        
        os.system("clear")
       
        print(f"[ + ] Trying to install Tools")
        
        sleep(3.5)

        tools = [
            "medusa", "apache2", "john", "proxychains4", "hashcat", "nmap", "ncat", "aircrack-ng",
            "autopsy", "tmux", "zsh", "ksh", "vim", "dnsrecon", "tcpdump", "code", "snort", "fcrackzip",
            "fping", "ffuf", "registry-tools", "mysql-client", "virtualbox"
            ]

        for installing_tools in tools:
            
            try:
 
                subprocess.call(["apt", "install", f"{installing_tools}", "-y"])

            except:
                print(f"[-] Something Went Wrong ( TOOLS FUNC )")
                
                pass
        

    except:
        print("[ X ] Could Not Install Certain T00LS")
 

def installing_misc():
   
    try:

        os.system("clear")
        print(f"[ ^^^ ] Installing Fun Programs [ ^^^ ]")
        sleep(2)
        
        subprocess.call(["apt", "install", "lolcat", "-y"])
        subprocess.call(["apt", "install", "figlet", "-y"])
        subprocess.call(["apt", "install", "cowsay", "-y"])
        subprocess.call(["apt", "install", "cmatrix", "-y"])
        subprocess.call(["apt", "install", "pi", "-y"])
        subprocess.call(["apt", "install", "neofetch", "-y"])
        subprocess.call(["apt", "install", "piper", "-y"])
        

    except Exception as e:
        print(f"[ X ] Something Went Wrong\n{str(e)}")
        pass
    

def removing_unwanted() -> bool:
    
    clear = lambda: os.system("clear")
    try:
        print(f"\n[ = ] Removing Unwanted Dependencies [ = ]")
        sleep(3)
        subprocess.call(["apt", "autoremove", "-y"])
        clear()
        return True

    except Exception as error:
        print(f"[ {error} ] \nAn ERROR has Occured Removing Unwanted Dependencies\nExiting...")
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
    installing_brave()
    installing_tools()
    installing_misc()
    installing_ida()
    removing_unwanted()


if __name__ == "__main__":
    
    print(f"Executing --> \33[32m{__name__}\33[39m")
    sleep(2)
    os.system("clear")
    
    main()
    print(f"[ {current} ] Ev3rything W3NT W3LL [ {current} ]")
    
    

