#!/usr/bin/python3
import py_compile
import compileall
import argparse
import os

# 通过 python Shell 也可以生成 .pyc
# python -m py_compile ***.py
# python -O -m py_compile ***.py


# 用于将单个文件编译成.pyc文件
def compile_pyc_file(filepath):
    py_compile.compile(filepath)


# 用于批量编译成.pyc 文件
def compile_pyc_dir(dirpath):
    compileall.compile_dir(dirpath)


def main(path):
    if os.path.isfile(path):
        compile_pyc_file(path)
    elif os.path.isdir(path):
        compile_pyc_dir(path)
    else:
        print("cannot find dir or file:%s" % path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage="it's usage tip.", description="help info.")
    parser.add_argument("--path", required=True, help="file or dir path")
    args = parser.parse_args()
    main(args.path)
