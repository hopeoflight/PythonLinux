#!/usr/bin/python3
# coding=UTF-8
# python 加载另外的python脚本的方法演示
# 1. eval 用来直接运行python表达式
# 2. exec 用来在内存中执行python脚本
# 3. __import__(module_name) 动态加载python模块


# 不带参数执行的python脚本,可以直接读取文件加载
# exec语句用来执行储存在字符串或文件中的Python语句
# exec(expr, args)
# exec 没有返回值,被执行的python脚本的变量全部存储在args这个dict中
def load_txt(path):
    code = ""
    with open(path, 'r') as file:
        code = file.read()

    context = globals().copy()
    exec(code, context)
    print("----->DynamicLoad area: %d" % context["area"](5))


# python 加载模块,可以加载编译生成的 prc 文件
def load_module(path):
    class_name = "TestClass"
    module_name = path
    method = "echo"

    module = __import__(module_name)
    c = getattr(module, class_name)
    obj = c()
    print("----->obj.echo:")
    obj.echo()
    mth = getattr(obj, method)
    print("----->mth:")
    mth()


load_txt("load_test.py")
# load_module("load_test")
