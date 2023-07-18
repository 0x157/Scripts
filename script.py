from tqdm import tqdm
import os, sys
import subprocess
from time import sleep
from datetime import datetime

AUTHOR = 0x157
now = datetime.now()
current_date = now.strftime("[%H:%M]")
clear = lambda: os.system('clear') 
uid = os.getuid()


def check_root() -> None:

    if not "SUDO_UID" in os.environ.keys() and uid != 0:
        print(f"\n{current_date} Script Must Be Ran As Root\n")

        raise SystemExit 
    
    else:
        clear()

        print(f"{current_date} You are Root !\n")
        sleep(1.24)

        clear()


def update_packages() -> None:
    bar = "Updating Packages [.........]"
    count_dots = bar.count(".")
    replaced = count_dots // 2
    replaced_pkg = count_dots // 2 + 3
    
    
    try:
        print(f"{bar.replace('.', '#', replaced)}\n")

        subprocess.call(["sudo", "apt", "update"], 
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)

        sleep(0.9)

        clear()

        print(f"{bar.replace('.', '#', replaced_pkg).replace('Updating Packages', 'Upgrading Packages')}\n")

        sleep(0.9)

        subprocess.call(["sudo", "apt", "upgrade", "-y"], 
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)
        
        clear()
        
        print(f"{bar.replace('.', '#', count_dots).replace('Updating Packages', 'Done')}\n")

        sleep(0.9)

        clear()

    except Exception as error:
        print(f"{error}")


class PythonPkgs(object):
    def __init__(self) -> None:
        pass


    @staticmethod
    def get_pkgs():
        modules = ["bs4","requests","cursor","rich","selenium","scapy", "pyarmor", "python-nmap", 
                "cryptography", "yara", "pywal", "dnspython", "pyshark", "paramiko", "splunk-sdk"
                ]

        print(f"\n")

        for module in tqdm(modules, colour="magenta", desc="Downloading Python PKGS"):
            subprocess.call(["pip3", "install", f"{module}"], 
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL)
            
        clear()
        print(f"[+] Done Installing {len(modules)} Python3 Packages.")

        sleep(1.25)
        clear()


class InstallTools(object):
    def __init__(self) -> None:
        check_snap = subprocess.check_output(["which", "snap"])
        dcd_snap = check_snap.decode('utf-8').replace("\n", "")[9::]
        
        if dcd_snap != "snap":
            print(f"[-] Snap is not installed\nInstalling...")

            try:

                subprocess.call(["sudo", "apt", "install", "snapd"], 
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
                
                print(f"[+] Installed SNAP")

                sleep(0.95)
                clear()

            except:
                print(f"Could Not Install Snap")
                pass

        else:
            print("[+] Snap is present :)")

            sleep(0.9)

            clear()


    @staticmethod
    def general_tools():

        print(f"\n")

        tools = ["medusa", "apache2", "john", "proxychains4", "hashcat", "nmap", "ncat", "aircrack-ng",
            "autopsy", "tmux", "zsh", "ksh", "vim", "dnsrecon", "tcpdump", "code", "snort", "fcrackzip",
            "fping", "ffuf", "registry-tools", "mysql-client", "virtualbox", "netdiscover", "wireshark-qt", "wfuzz", "socat",
            "redis-tools", "smbclient", "nbtscan", "gobuster", "hydra", "freerdp2-x11", "binwalk", "tshark", "rkhunter", "sqlmap", 
            "steghide", "stegseek", "foremost", "libimage-exiftool-perl", "pdfcrack", "pngcheck", "checksec",
            "dmitry", "nikto", "openvas-scanner", "sl", "awscli", "piper"]


        for tool in tqdm(tools, colour="yellow", desc="Installing Common Tools", smoothing=0.9):
            subprocess.call(["sudo", "apt", "install", f"{tool}", "-y"], 
                            stdout=subprocess.DEVNULL, 
                            stderr=subprocess.DEVNULL)
            
        clear()

        print(f"{current_date} Installed {len(tools)} Common Tools !\n")

        sleep(0.93)

    @staticmethod
    def ghidra() -> None:
        class Ghidra(object):
            def __init__(self) -> None:
                clear()

                try:
                    print(f"[+] Installing JDK-11")

                    subprocess.call(["sudo", "apt", "install", "openjdk-11-jdk"],
                                    stderr=subprocess.DEVNULL,
                                    stdout=subprocess.DEVNULL)
                    
                    print(f"[*] Installed JDK-11 for GHIDRA")

                    sleep(1.5)

                    clear()     

                except:
                    print(f"[-] Could Not Install JDK")
                    pass
                
            @staticmethod
            def main_ghidra():
                GHIDRA_LINK = "https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.3.1_build/ghidra_10.3.1_PUBLIC_20230614.zip"

                commands = ["unzip /opt/ghidra.zip"]
                clear()

                try:

                    subprocess.call(["wget", "-O", "/opt/ghidra.zip", f"{GHIDRA_LINK}"], 
                                    stdout=subprocess.DEVNULL, 
                                    stderr=subprocess.DEVNULL) 
                    
                    print(f"[?] Downloading GHIDRA")
                    
                    subprocess.call([f"{commands[0]}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 

                    print(f"\33[34m[***] Installed Ghidra [***]")

                    sleep(1.3)

                    clear()


                except Exception as Error:
                    print(Error)

                    clear()

                    pass

        install = Ghidra()

        install.main_ghidra()


def get_theme() -> bool:

    theme = f"https://github.com/EliverLara/Kripton.git"

    try:
        print(f"\n[+] Downloading Theme")

        sleep(0.1)

        clear()

        os.system("sudo rm -rf ~/.themes/ && mkdir ~/.themes")
        
        subprocess.call(["git", "clone", f"{theme}"], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

        clear()

        print(f"Installed the Theme!")

        sleep(2)

        return True

    except Exception as e:
        return False


def remove_unwanted() -> None:

    clear()

    try:

        print("\n[+] Cleaning Up")

        subprocess.call(["apt", "autoremove"], stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)

        clear()

        print(f"[***] Ev3ryth1ng W3n7 W311")

        sleep(4)

    except:
        pass


def main() -> bool:
    
    try:
        check_root()
        update_packages()

        pip_pkgs = PythonPkgs() 
        pip_pkgs.get_pkgs()

        gen_tools = InstallTools()
        gen_tools.general_tools()

        gen_tools.ghidra()

        get_theme()

        remove_unwanted()

        return True

    except KeyboardInterrupt:
        clear()
        print("[*] Kill Signal Sent\nExiting...")

        return False


if __name__ == "__main__":
    try:
        main()

    except Exception as error:
        print(error)
        