import os, subprocess

# Script does need to be ran with sudo or root

def install_volatility2() -> None:
    clear = lambda: os.system('clear')
    
    def update() -> bool:
        try:
            subprocess.call(["sudo", "apt-get", "update"])

            clear()        

            return True
        except:
            pass
    
    update()


    def install_python2() -> None:
        python2_commands = ["apt install -y python2.7", 
                        "apt install -y python-pip python-setuptools build-essential python2.7-dev"
                        ]

        for command in python2_commands:
            os.system(f"{command}")

        clear()

    
    install_python2()


    def clone_and_install() -> bool:
        commands = ["python2 -m pip install distorm3", "python2 -m pip install pycrypto",
                    "git clone https://github.com/volatilityfoundation/volatility", 
                    "sudo mv volatility/ /opt"]
        
        for fcmd in commands:
            try:
                os.system(f"{fcmd}")
                clear()

            except Exception as e:
                print(f"{e}")

        print(f"[+] VOL2 Should be installed.\nCheck /opt dir")
        return True

    clone_and_install()


if __name__ == "__main__":
    try:
        install_volatility2()

    except:
        print(f"Failed to Execute {__name__}\nExiting...")
        raise SystemExit
    
