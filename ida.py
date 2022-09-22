import subprocess 
from platform import platform
import os
from time import sleep
from datetime import datetime


class IDA:
    def __init__(self):
        def change_directory():
            try:
                current = subprocess.check_output(["pwd"])
                print(f"You are Currently Located @ --> {current}")
                
            except:
                print(f"[ - ] Could Not Change Directories")
                pass

        change_directory()

    @staticmethod
    def getting_ida():

        link = "https://out7.hex-rays.com/files/idafree80_linux.run"
        try:
            print(f"[ * ] Trying to Get IDA")
            subprocess.call(["wget", "install", f"{link}"])

        except Exception as error:
            print(f"{error}")

            
def main():
    return NotImplemented


if __name__ == "__main__":
    main()
