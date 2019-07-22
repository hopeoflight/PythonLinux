#!/usr/bin/python3
# 使用 sys.argv 可以直接获取命令行输入的参数,输入的参数会list,可以进行遍历
import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path)
