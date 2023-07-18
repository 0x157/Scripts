"""
Authors: 0X157 & Alternative Al
Description: A kit to install all basic reverse engineering tools. Leverages installer.py (install_vol2.py + linux_script.py) and progressbar.py
Version: 1.0
Last Updated By: Non Applicable.
"""
import argparse
import installer
import progressBar
import pyfiglet
from datetime import datetime
import subprocess
import time

# Global Variables
NOW = datetime.now()
PATH = subprocess.check_output(["pwd"])
TIME = NOW.strftime(f"%H:%M")

# Global Links
GITHUB = "https://www.github.com"
GHIDRA = "https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.1.5_build/ghidra_10.1.5_PUBLIC_20220726.zip"
ADA = "https://out7.hex-rays.com/files/idafree82_linux.run"

# Tools to install
TOOLS = ["lolcat", "figlet", "cowsay", "cmatrix", "pi", "neofetch", "piper", "sl", "duf", "snapd", "cava", "medusa", "apache2", "john", "proxychains4", "hashcat", "nmap", "ncat", "aircrack-ng",
            "autopsy", "tmux", "zsh", "ksh", "vim", "dnsrecon", "tcpdump", "code", "snort", "fcrackzip",
            "fping", "ffuf", "registry-tools", "mysql-client", "virtualbox", "netdiscover", "wireshark-qt", "wfuzz", "socat",
            "redis-tools", "smbclient", "nbtscan", "gobuster", "hydra", "freerdp2-x11", "binwalk", "tshark", "rkhunter", "sqlmap", 
            "steghide"]

def start():
    """
    A function to print an introductory banner.
    """

    result = pyfiglet.figlet_format("Rev-Kit Installer")
    print(result)
    print("A one stop installer for all your reverse engineering tools.")
    print("By 0x157 & Alt3rnativ3 Al (@ZatezaloAleksa on Twitter)")
    print("Made in May of 2023")
    time.sleep(2)

def finish():
    """
    Prints a finishing message to the screen.
    """
    
    result = pyfiglet.figlet_format("Happy Reversing!")
    print(result)

def system_check():
    """
    Runs a basic system check.
    """
    
    if installer.check_root():
        print('\n[+] Running as root.')
    else:
        print('[-] Must run as root.')
        return False
    if installer.check_connection(GITHUB):
        print('[+] Internet connection confirmed.\n')
    else:
        print('[-] Must be connected to the internet.')
        return False
    
def sys_update():
    """
    A function to update the system with required software. Returns a bool.
    """

    pBar = progressBar.progressBar("Updating system hooks.")
    pBar.start()
    installer.updating()
    pBar.setMsg("Installing Python 2.")
    installer.install_python2()
    pBar.setMsg("Installing Python 3.")
    installer.install_python3()
    pBar.setMsg("Installing PIP 3.")
    installer.install_pip()
    pBar.setMsg("Installing Python 3 Packages.")
    installer.install_packages()
    pBar.setMsg("Installing JDK11.")
    installer.jdk_11()
    pBar.stop()
    time.sleep(0.2)
    print('\n[+] System update complete. Dependencies installed.\n')
    return True

def install_dependencies():
    """
    Installs software required to unpack rev-kit tools.
    """

    print("Installing unpacking tools.")
    pBar = progressBar.progressBar("Installing unzip.")
    pBar.start()
    installer.install_unzip()
    pBar.setMsg("Installing curl.")
    installer.install_curl()
    pBar.setMsg("Installing wget.")
    installer.install_wget()
    pBar.stop()
    time.sleep(0.2)
    print('\n[+] System update complete. Dependencies installed.\n')


def install_tools():
    """
    Installs tools in TOOLS array.
    """

    installer.install_hack_kit(TOOLS) # pBar in installer
    print('\n[+] Basic tools installed.\n')
    return True


def installer_soft():
    """
    Function to install all other software.
    """
    
    pBar = progressBar.progressBar(f"Installing Ada at {PATH}.")
    pBar.start()
    installer.install_ada()
    pBar.setMsg(f"Installing Ghidra at {PATH}.")
    installer.install_ghidra()
    pBar.setMsg("Installing Volatility 2.")
    installer.install_volatility()
    pBar.stop()
    time.sleep(0.2)
    print('\n[+] Major tools installed.\n')
    return True
    
def remove_dependencies():
    """
    Removes unused system dependencies. Returns a bool.
    """
    pBar = progressBar.progressBar(f"Removing unused dependencies.")
    pBar.start()
    installer.remove_dependencies()
    pBar.stop()
    time.sleep(0.2)
    print('\n[+] Dependencies removed.\n')
    return True
def main():
    start()
    system_check()
    sys_update()
    install_dependencies()
    install_tools()
    installer_soft()
    remove_dependencies()
    finish()


if __name__ == "__main__":
    main()