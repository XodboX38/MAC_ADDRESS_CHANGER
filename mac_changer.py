#!/usr/bin/env python
import subprocess
from optparse import OptionParser
import re
import time
from colorama import Fore
# -----------------------------FUNCTIONS STARTS HERE-------------------------------------------
def parsing():
    parse = OptionParser()
    parse.add_option("-m", "--mac", dest="mac", help="Used to set MAC Address")
    parse.add_option("-i", "--interface", dest="interface", help="Used to set Interface")
    (values, options) = parse.parse_args()
    if not values.interface:
        print("\n")
        print("\t", "[-]Please enter a Interface, use --help for help ")
        print("\n")
    elif not values.mac:
        print("\n")
        print("\t", "[-]Please enter a MAC, use --help for help ")
        print("\n")
    return values

def current_mac():
    current = subprocess.check_output(["ifconfig", values.interface])
    current_rejex_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(current))
    time.sleep(1)
    if current_rejex_result:
        print("\n", "\t\t\t\t\t\t", Fore.YELLOW, "[+] The current MAC address is :", Fore.GREEN ,current_rejex_result.group(0), Fore.WHITE)
    else:
        print("\t\t\t\t\t\t", Fore.YELLOW, "\n[+] Sorry no MAC address found")
        exit()

def changing_mac(mac, interface):
    if not values.interface:
        exit()
    elif not values.mac:
        exit()
    print("\n", "\t\t\t\t\t\t", Fore.YELLOW, "[+] Changing  MAC Address on ",  Fore.RED, interface, Fore.YELLOW," to ",  Fore.GREEN, mac, "\n")
    time.sleep(1)
    # Another way to use subprocess.call([]) function
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])

def new_mac():
    ifconfig_result = subprocess.check_output(["ifconfig", values.interface])
    rejex_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    time.sleep(1)
    if rejex_result:
        print("\n\t\t\t\t\t\t", Fore.YELLOW, "[+] The new MAC address is :",  Fore.GREEN, rejex_result.group(0))
    else:
        print("\t\t\t\t\t\t", Fore.YELLOW, "\n[+] Sorry no MAC address found")
    time.sleep(1)
    if str(rejex_result.group(0)) == str(values.mac):
        time.sleep(1)
        print("\n", "\t\t\t\t\t\t", Fore.GREEN, "[+] MAC address changed successfully")
    else:
        print("\n", "\t\t\t\t\t\t", Fore.YELLOW, "[+] Sorry not able to change the MAC address")

# def changing_mac_using_subprocess(mac,interface):
    # A way to use subprocess.call() function
    # subprocess.call("ifconfig " + interface + " down", shell=True)
    # subprocess.call("ifconfig " + interface + " hw ether " + mac, shell=True)
    # subprocess.call("ifconfig " + interface + " up", shell=True)
    # subprocess.call("ifconfig " + interface,shell=True)
# -----------------------------FUNCTIONS ENDS HERE-------------------------------------------

#-----------------------------CALLING A FUNCTION---------------------------------------------
values = parsing()
subprocess.call(["clear"])
current_mac()
time.sleep(1)
changing_mac(str(values.mac),str(values.interface))
time.sleep(1)
new_mac()
# changing_mac_using_subprocess(str(values.mac),str(values.interface))
# -----------------------------CALLING A FUNCTION ENDS HERE-----------------------------------
