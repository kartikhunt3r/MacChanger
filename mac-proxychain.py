#!/usr/bin/env python3 

import optparse
import subprocess
import time
import re
from click import argument, option
import random

class colors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(colors.OKGREEN,colors.BOLD,"""
 
░█████╗░██████╗░██████╗░██╗░██████╗██╗░░██╗██╗░░░██╗░█████╗░
██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██║░░██║╚██╗░██╔╝██╔══██╗
███████║██║░░██║██████╔╝██║╚█████╗░███████║░╚████╔╝░███████║
██╔══██║██║░░██║██╔══██╗██║░╚═══██╗██╔══██║░░╚██╔╝░░██╔══██║
██║░░██║██████╔╝██║░░██║██║██████╔╝██║░░██║░░░██║░░░██║░░██║
╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

███████████████████████████████████████████████████
█▄─▀█▀─▄██▀▄─██─▄▄▄─███─▄▄▄─█─█─██▀▄─██▄─▄█▄─▀█▄─▄█
██─█▄█─███─▀─██─███▀███─███▀█─▄─██─▀─███─███─█▄▀─██
▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▀▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀                                                                
                                                 
                                                @kartikhunt3r


""",colors.ENDC)


def getarguments():

    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface" ,help="Interface To Change Its MAC Address")
    parser.add_option("-t", "--time", dest="time" ,type="int" ,help="time duration between changing each MAC address")
    (option, argument) = parser.parse_args()
    if not option.interface:
        parser.error(colors.WARNING+"[-] Please specify the interface. use --help for more information."+colors.ENDC)
    elif not option.time:
        parser.error(colors.WARNING+"[-] Please specify a time duration. use --help for more information."+colors.ENDC)
    else:
        return option

def mac_changer(intr,mac):

    print(colors.BOLD+colors.OKGREEN +
        "[+] Changing MAC Address for " + intr + " to " + mac+" ..."+colors.ENDC+"\n")
    time.sleep(option.time/2)

    subprocess.call(["ifconfig", intr, "down"])
    subprocess.call(["ifconfig", intr, "hw", "ether", mac])
    subprocess.call(["ifconfig", intr, "up"])

def rand_mac():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )

def getCurrentMAC(interface):

    ifconfig_results = str(subprocess.check_output(["ifconfig",interface]))

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_results)

    if mac_address_search_result:
        return mac_address_search_result.group(0)

    else:
        print(colors.BOLD,colors.WARNING,"[-] Could not read the MAC address",colors.ENDC)




option = getarguments()

while True:

    time.sleep(option.time/2)

    random_mac = rand_mac()


    mac_changer(option.interface,random_mac)

    current_mac = getCurrentMAC(option.interface)

    if current_mac==random_mac:
        print(colors.OKBLUE,colors.BOLD,"[+] MAC address is changed Successfully changed to "+current_mac)

    else:
        print(colors.FAIL,colors.BOLD,"[-] MAC address is not changed")
