#!/usr/bin/python3
# encoding=utf-8
import argparse


def main(arg):
    print("--address {0}".format(arg.code_address))  # args.address会报错，因为指定了dest的值
    print("--flag {0}".format(arg.flag))  # 如果命令行中该参数输入的值不在choices列表中，则报错
    print("--port {0}".format(arg.port))  # prot的类型为int类型，如果命令行中没有输入该选项则报错
    print("-l {0}".format(arg.log))  # 如果命令行中输入该参数，则该值为True。因为为短格式"-l"指定了别名"--log"，所以程序中用args.log来访问


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="it's usage tip.", description="help info.")
    parser.add_argument("--address", default=80, help="the port number.", dest="code_address")
    parser.add_argument("--flag", choices=['.txt', '.jpg', '.xml', '.png'], default=".txt", help="the file type")
    parser.add_argument("--port", type=int, required=True, help="the port number.")
    parser.add_argument("-l", "--log", default=False, action="store_true", help="active log info.")

    args = parser.parse_args()
    main(args)

# 分别运行如下命令:
# python3 argparse_arg.py
# python3 argparse_arg.py --help
# python3 argparse_arg.py --port 80
# python3 argparse_arg.py --port 80 --flag apk
# python3 argparse_arg.py --port 80 -l

# 原型:
# ArgumentParser(prog=None,usage=None, description=None, epilog=None, parents=[], formatter_class=argparser.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True)
# 其中的参数都有默认值，当运行程序时由于参数不正确或者当调用parser.print_help()方法时，会打印这些描述信息。一般只需要传递参数description。
# add_argument(name or flags... [, action] [, nargs] [, const] [, default] [, type] [, choices] [, required] [, help] [, metavar] [, dest])
# 其中的常用参数解释如下：
# name or flags: 命令行参数名或者选项，如-p, --port
# action:
# 　　　　store: 默认的action模式，存储值到指定变量
# 　　　　store_const: 存储值在参数的const部分指定，常用来实现非布尔的命令行flag
# 　　　　store_true/store_false: 布尔开关。store_true的默认值为False，若命令行有输入该布尔开关则值为True。store_false相反
# 　　　　append: 存储值到列表，该参数可以重复使用
# 　　　　append_const: 存储值到列表，存储值在参数的const部分指定
# 　　　　count: 统计参数简写的输入个数
# 　　　　version: 输出版本信息，然后退出脚本
# nargs: 命令行参数的个数，一般用通配符表示： ？表示只用一个，*表示0到多个，+表示1到多个
# default: 默认值
# type: 参数的类型，默认是string类型，还可以是float、int和布尔等类型
# choices: 输入值的范围
# required: 默认为False，若为True则表示该参数必须输入
# help: 使用的帮助提示信息
# dest: 参数在程序中的对应的变量名称，如：add_argument("-a", dest="code_name")，在脚本中用parser.code_name来访问该命令行选项的值