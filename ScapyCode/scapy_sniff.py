# !/usr/bin/python3
from scapy.all import *
try:
    import scapy_http.http
except ImportError:
    from scapy.layers import http


# 抓取数据包并且将数据包保存为 pcap 类型的文件
def save_package(filepath):
    package = sniff(iface="ens33", count=10)
    wrpcap(filepath, package, append=True)


# 循环抓包,并输出内容
def show_src_dest_ip():
    # while True:
    sniff(iface="ens33", count=5, prn=lambda x: x.sprintf("{IP:%IP.src% -> %IP.dst%\n}"))


# 抓取http数据包,输出内容
def resolve_http_pkg(pkg):
    if "HTTP Request" in pkg:
        print("========>HTTP REQUEST<========")
        print(pkg["HTTP Request"].Headers)
    elif "HTTP Response" in pkg:
        print("========>HTTP RESPONSE<========")
        print(pkg["HTTP Response"].Headers)
    else:
        print("========>TCP<========")
        print(pkg["IP"].src, pkg["IP"].sport, '->', pkg["IP"].dst, pkg["IP"].dport, pkg["TCP"].flags)

    return


def sniff_http_pkg():
    sniff(iface="ens33", filter="tcp and port 80", prn=resolve_http_pkg)


if __name__ == "__main__":
    # show_src_dest_ip()
    sniff_http_pkg()
