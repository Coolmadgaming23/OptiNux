# COMPILE THIS PROGRAM USING PYINSTALLER OR SMT.
# LINUX VERSION
# Optimization app by shandoku
import os
import time

print("Updating and running system checkups...")
time.sleep(1)
os.system("sudo apt update && sudo apt upgrade") 
time.sleep(2)
print("System is up-to-date!")
time.sleep(2)
print("Starting optimizer app...")
time.sleep(3)

while True:
    os.system("clear")
    print("====={[System Optimizer 1.0]}=====")
    print("1. Delete temporary files")
    print("2. Performance Mode")
    print("3. Install Graphics Driver - For Ubuntu/Debian Only!") 
    print("4. Enable ZRAM - Compressed RAM Swap")
    choice = input("Select: ")

    if choice == "1":
        print("Confirm?")
        print("Y/n")
        print(" ")
        print("Note: Please select then hit enter.")
        confirm = input(" ")
        if confirm == "Y":
            print("Waiting for the host to respond...")
            time.sleep(2)
            os.system("sudo apt clean && sudo apt autoclean")
            print("Success!")
            time.sleep(2)
            continue
        elif confirm == "n":
            print("Exiting...")
            time.sleep(1)
            continue
        else:
            print("Invalid input!")
            time.sleep(1)
            continue

    elif choice == "2":
        print("Setting up to performance mode...")
        time.sleep(4)
        print("Waiting for results...")
        time.sleep(1)
        os.system("echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor")
        print("Success!")
        time.sleep(2)
        continue
    elif choice == "3":
        os.system("clear")
        print("Finding updated and compatible drivers...")
        os.system("sudo add-apt-repository ppa:graphics-drivers/ppa && sudo apt update")
        time.sleep(1)
        print("What distro are you using?")
        print("1. Ubuntu")
        print("2. Debian")
        distro = input("Select:")

        if distro == "1":
            print("Finding compatible drivers...")
            time.sleep(1)
            os.system("sudo ubuntu-drivers autoinstall")
            print("Success!")
            time.sleep(2)
            continue

        elif distro == "2":
            print("Finding compatible drivers...")
            time.sleep(1)
            os.system("sudo apt install linux-headers-$(uname -r) build-essential dkms nvidia-detect")
            os.system("nvidia-detect")
            os.system("sudo apt install nvidia-driver nvidia-kernel-dkms")
            print("System needs to be restarted in order to continue.")
            time.sleep(1)
            print("Performing automatic restart...")
            time.sleep(2)
            os.system("sudo reboot")

    elif choice == "4":
        os.system("clear")
        print("Enabling ZRAM...")
        time.sleep(2)
        os.system("sudo apt install zram-tools && sudo systemctl enable --now zramswap")
        print("Success!")
        time.sleep(2)
        continue

    else:
        print("Invalid Input!")
        time.sleep(1)
        continue
