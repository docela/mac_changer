#!/usr/bin/env python

import subprocess
import argparse
import random

# This function enables the user to state the interface to change the command line.


def get_interface():
    parser = argparse.ArgumentParser(description="Change your MAC Address.")
    parser.add_argument(
        "-i", "--interface", help="The interface you want to change.", dest="interface")
    args = parser.parse_args()
    return args.interface

# This function creates six random hexadecimal numbers (removing the 0x) and puts it together to create a new MAC address


def mac_maker():
    mac_one = hex(random.randrange(16, 256))[2:].upper()
    mac_two = hex(random.randrange(16, 256))[2:].upper()
    mac_three = hex(random.randrange(16, 256))[2:].upper()
    mac_four = hex(random.randrange(16, 256))[2:].upper()
    mac_five = hex(random.randrange(16, 256))[2:].upper()
    mac_six = hex(random.randrange(16, 256))[2:].upper()
    mac_address = f"{mac_one}:{mac_two}:{mac_three}:{mac_four}:{mac_five}:{mac_six}"
    return mac_address


# We assign the functions to a variable for the below function to actually change the MAC address.
interface = get_interface()
new_mac = mac_maker()


# This is the function that actually runs the commands to change the MAC address in the shell.
def change_mac(iface, mac):
    print(f"Changing the MAC address for {iface}")
    # The actual process
    subprocess.run(["sudo", "ip", "link", "set",
                    "dev", iface, "down"], shell=True)
    subprocess.run(["sudo", "ip", "link", "set", "dev",
                    iface, "address", mac], shell=True)
    subprocess.run(["sudo", "ip", "link", "set",
                    "dev", iface, "up"], shell=True)
    subprocess.run(["ip", "-s", "link", "show", iface], shell=True)


change_mac(interface, new_mac)
