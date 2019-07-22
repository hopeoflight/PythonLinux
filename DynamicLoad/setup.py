#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import argparse
from distutils.core import setup
from Cython.Build import cythonize


def compile_os(filepath, build_dir, build_tmp_dir):
    setup(
        ext_modules=cythonize([filepath]),
        script_args=["build_ext", "-b", build_dir, "-t", build_tmp_dir]
    )


def main(args):
    if os.path.isfile(args.path):
        build_dir = ("./build" if args.build_dir is None else args.build_dir)
        build_tmp_dir = ("./tmp" if args.build_tmp_dir is None else args.build_tmp_dir)
        compile_os(args.path, build_dir, build_tmp_dir)
    else:
        print("cannot find file: %s" % args.path)


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="help info")
    parse.add_argument("-p", required=True, help="python file path or dir", dest="path")
    parse.add_argument("-b", help="build director path", dest="build_dir")
    parse.add_argument("-t", help="build tmp director path", dest="build_tmp_dir")

    # print(parse.parse_args())
    main(parse.parse_args())
