#!/usr/bin/python3
# encoding=utf-8
import getopt
import sys

# 主要用到了模块中的函数：
# options, args = getopt.getopt(args, shortopts, longopts=[])
# 参数args：一般是sys.argv[1:]。过滤掉sys.argv[0]，它是执行脚本的名字，不算做命令行参数。
# 参数shortopts：短格式分析串。例如："hp:i:"，h后面没有冒号，表示后面不带参数；p和i后面带有冒号，表示后面带参数。
# 参数longopts：长格式分析串列表。例如：["help", "ip=", "port="]，help后面没有等号，表示后面不带参数；ip和port后面带冒号，表示后面带参数。
# 返回值options是以元组为元素的列表，每个元组的形式为：(选项串, 附加参数)，如：('-i', '192.168.0.1')
# 返回值args是个列表，其中的元素是那些不含'-'或'--'的参数。
# 运行命令如：python3 getopt_arg.py -i 192.168.0.1 -p 80 123,a v

def main(argv):
    try:
        options, args = getopt.getopt(argv, "hp:i:", ["help", "ip=", "port="])
    except getopt.GetoptError:
        sys.exit()

    for option, value in options:
        if option in ("-h", "--help"):
            print("help")
        if option in ("-i", "--ip"):
            print("ip is: {0}".format(value))
        if option in ("-p", "--port"):
            print("port is: {0}".format(value))

    print("error args: {0}".format(args))


if __name__ == '__main__':
    main(sys.argv[1:])
