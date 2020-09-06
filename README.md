# MAC Address Changer

This is a script that changes the MAC Address for a device. State the interface/device you want to change, using the `-i` flag, on the terminal and it creates a new MAC address and sets it to the device. 

## Why Change a MAC Address?
Changing a MAC address is useful for:
- Increasing anonymity.
- Bypassing filters.
- Impersonating another device.

## Modules Used
The following Python libraries were used:
1. **Subprocess** - This was used to run commands in a shell/ terminal.
2. **Argparse** - This was used to create commands to be used on the terminal.
3. **Random** - This was used to generate random numbers, which would then be converted into hexadecimal numbers, and used to create the MAC address.

### How it Works

The `get_interface`function, using the `i` flag, takes the interface/device the user wants to change.

The `mac_maker` function creates a new MAC address by creating six random numbers, all assigned to variables, in the range 16 - 255 and converts the numbers to hexadecimal numbers. The numbers were chosen because 16 is the first number that uses two digits in the hexadecimal system (10) and 255 is the last number that uses two digits (FF). `[2:]` is used to select the last two digits as using `hex()` adds an "0x" to the beginning of converted numbers. The hex() converts the numbers to string and so `.upper()` is used as MAC addresses are usually capitalised.

The `change_mac` function is the final function and it takes the interface and new MAC address as arguments. Using the subprocess library it sends commands to the shell/terminal and makes the changes.


To run the script:
```
python mac_changer.py -i <interface>

python mac_changer.py -i wlan0
```