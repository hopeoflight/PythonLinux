#!/usr/bin/python3
from scapy.all import *


# 发送简单数据包,每隔一秒发送一次,总共发送五次
def send_package(src,dst,data):
    pkt = IP(src=src, dst=dst)/TCP(sport=12345, dport=12345)/data
    send(pkt, inter=1, count=5)


if __name__ == "__main__":
    send_package("192.168.25.129","192.168.51.221","Hello World!")
