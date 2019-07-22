# 解析 pcap 数据包程序
# !/usr/bin/python3
from scapy.all import *


# 使用 sniff 解析 pcap 文档
def resolve_sniff(filepath):
    package = sniff(offline=filepath)
    print("----->package<-----")
    print(package)
    print("----->package index<-----")
    print(package[0])
    print("----->package.show<-----")
    print(package[0].show())
    print("----->package IP fields<-----")
    print(package[0]["IP"].fields)


# 使用 rdcap 解析 dcap 文档
def resolve_rdpcap(filepath):
    package = rdpcap(filepath)
    print("----->package<-----")
    print(package)
    print("----->package index<-----")
    print(package[0])
    print("----->package.show<-----")
    print(package[0].show())
    print("----->package IP fields<-----")
    print(package[0]["IP"].fields)


if __name__ == "__main__":
    resolve_rdpcap("test.pcap")
