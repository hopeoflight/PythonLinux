#!/usr/bin/python3
from scapy.all import *


def get_mac_by_ip(ip):
    ans,unmans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip))
    for snd, rcv in ans:
        list_mac = rcv.sprintf("%Ether.src% - %ARP.psrc%")
        print(list_mac)


if __name__ == "__main__":
    get_mac_by_ip("127.0.0.1")
