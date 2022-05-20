#! /usr/bin/env python2

import subprocess
import optparse
import re


def get_args():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mac")
    parser.add_option("-m", "--mac", dest="mac_add", help="New mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("please enter interface value")
    elif not options.mac_add:
        parser.error("Please enter mac address")
    return options


def change_mac(interface, mac_add):
    # subprocess.call("ifconfig " + interface + " down", shell=True)
    # subprocess.call("ifconfig " + interface + " hw ether " + mac_add, shell=True)
    # subprocess.call("ifconfig " + interface + " up", shell=True)
    # subprocess.call("ifconfig", shell=True)
    print("[+] Changing MAC address for " + interface + " to " + mac_add)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw" , "ether", mac_add])
    subprocess.call(["ifconfig", interface, "up"])


def get_currentmac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_regex = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_regex:
        return mac_regex.group(0)
    else:
        print("Could not read mac")



options = get_args()

currentmac = get_currentmac(options.interface)
print("Current mac is " + str(currentmac))
change_mac(options.interface, options.mac_add)
currentmac = get_currentmac(options.interface)
print(currentmac)
print(options.mac_add)
if currentmac == options.mac_add:
    print("Changed to " + options.mac_add)
else:
    print("did not get changed ")

subprocess.call(["ifconfig", options.interface])
