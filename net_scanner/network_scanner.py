#! /usr/bin/env python3

import scapy.all as scapy
import optparse
import argparse
#

def netscan(ip):
    # scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    # arp_request.show()
    # arp_request.pdst = ip
    # arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # to create packet
    # broadcast.show()

    arp_request_broadcast = broadcast / arp_request  # combination of two packet
    # arp_request_broadcast.show()
    ans = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]  # for sending the dest packet
    target_list = []
    for element in ans:  ## print(ans.summary())
        # print(element[1].psrc+"\t"+element[1].hwsrc)
        target_dict = {"mac": element[1].psrc, "IP": element[1].hwsrc}
        target_list.append(target_dict)
    return target_list


def prints(res_list):
    print("----------------------------------")
    print("IP\t\t\tAT Mac Address")
    print("----------------------------------")
    for client in res_list:
        print(client["mac"] + "\t\t" + client["IP"])
    # print(ans.summary())

    # print(unans.summary())
    # print(arp_request_broadcast.summary())
    # scapy.ls(scapy.Ether())


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="netscans", help="IP TO SCAN")
    (option, arguments) = parser.parse_args()
    if not option.netscans:
        parser.error("please enter ip range for scanning")
    return option

# by using argparser module
def get_argspar():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="netscans", help="IP TO SCAN")
    option = parser.parse_args()
    if not option.netscans:
        parser.error("please enter ip range for scanning")
    return option

options = get_args()
oode = get_argspar()

# scan_res = netscan(options.netscans)
scan_res = netscan(oode.netscans)
prints(scan_res)
