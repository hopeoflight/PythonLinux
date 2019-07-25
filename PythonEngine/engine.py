#!/usr/bin/python3
import json
import os
import argparse


# 引擎脚本,用于调用不同扫描模块或者直接调用正则处理漏洞文件
class Engine:

    __MySql = __import__("lib.mysql").mysql.MySql
    __Rsa = __import__("lib.rsa_crypt").rsa_crypt.Rsa()
    __Vul = __import__("lib.vulnerability").vulnerability.Vulnerability

    @staticmethod
    def crypt_file(filepath, output):
        Engine.__Rsa.enc_file(filepath, output)

    @staticmethod
    def decrypt_file(filepath):
        return Engine.__Rsa.dec_str(filepath)

    # @staticmethod
    # def test_sql():
    #     mysql = Engine.__MySql("127.0.0.1", 3306, "root", "1234", "python-sql")
    #     ins_str = "INSERT INTO vulnerability_detail SET name = 'bug1',description = '描述'," \
    #               "company = '能信安' "
    #     mysql.run_sql(ins_str)
    #
    #     sel_str = "SELECT * FROM vulnerability_detail"
    #     data = []
    #     mysql.run_sql_value(sel_str, data)
    #     print(data)

    @staticmethod
    def run_regex(regex_str):
        print("run python regex!")

    @staticmethod
    def run_module(module_name):
        context = globals().copy()
        exec(Engine.decrypt_file("lib/" + module_name), context)

    @staticmethod
    def insert(vul_id, style, secret_type, secret_key, content):
        Engine.__Vul.insert(vul_id, style, secret_type, secret_key, content)

    @staticmethod
    def get_index(vul_id=None, style=None):
        return json.dumps(Engine.__Vul.get_index(vul_id, style), ensure_ascii=False)

    @staticmethod
    def get_id(style=None):
        return json.dumps(Engine.__Vul.get_id(style), ensure_ascii=False)

    @staticmethod
    def get_type(vul_id=None):
        return json.dumps(Engine.__Vul.get_type(vul_id), ensure_ascii=False)

    @staticmethod
    def get_content(vul_id=None, style=None):
        return json.dumps(Engine.__Vul.get_content(vul_id, style), ensure_ascii=False)

    @staticmethod
    def save_vul(v_list):
        for v in v_list:
            Engine.insert(v["nneId"], v["type"], 0, "", json.dumps(v))

    @staticmethod
    def save_vul_file(file):
        if not os.path.exists(file):
            print("cannot find file %s" % file)
            return

        with open(file, 'rb') as f:
            content = f.read()
        if len(content) == 0:
            return

        Engine.save_vul(eval(content))


def main(args):
    if args.arg_type == "module":
        if not args.py_module:
            print("please input module name!")
        else:
            Engine.run_module(args.py_module)
    elif args.arg_type == "append":
        if not args.flaw_id or not args.flaw_type or not args.flaw_content:
            print("cannot get flaw id or flow type or flaw content,please input!")
        else:
            Engine.insert(args.flaw_id, int(args.flaw_type), int(args.secret_type), args.secret_key, args.flaw_content)
    elif args.arg_type == "append_file":
        if not args.flaw_file:
            print("please input flaw file path!")
        else:
            Engine.save_vul_file(args.flaw_file)
    elif args.arg_type == "index":
        print(Engine.get_index(args.flaw_id, int(args.flaw_type) if args.flaw_type else None))
    elif args.arg_type == "id":
        print(Engine.get_id(int(args.flaw_type) if args.flaw_type else None))
    elif args.arg_type == "type":
        print(Engine.get_type(args.flaw_id))
    elif args.arg_type == "content":
        print(Engine.get_content(args.flaw_id, int(args.flaw_type) if args.flaw_type else None))
    else:
        print("invalid arg type")


if __name__ == "__main__":
    # Engine.crypt_file("../DynamicLoad/load_test.py", "./lib/load_test")
    # Engine.run_module("load_test")
    # Engine.run_module("module1")
    # Engine.run_module("module2")
    # print(Engine.get_content(vul_id="test1"))
    # Engine.save_vul_file("vulnerable")

    parser = argparse.ArgumentParser(usage="python3 engine.py [TYPE OPTION] [OPTION]...",
                                     description="run engine must input [TYPE OPTION].")
    parser.add_argument("-t",
                        required=True,
                        choices=['module', 'append', 'append_file', 'index', 'id', 'type', 'content'],
                        dest="arg_type")
    parser.add_argument("-m", help="input module name", dest="py_module")
    parser.add_argument("-i", help="input flaw id", dest="flaw_id")
    parser.add_argument("-s", help="input flaw type", dest="flaw_type")
    parser.add_argument("-st", default="0", help="input secret type", dest="secret_type")
    parser.add_argument("-sk", default="", help="input secret key", dest="secret_key")
    parser.add_argument("-c", help="input flaw content", dest="flaw_content")
    parser.add_argument("-f", help="input file path", dest="flaw_file")
    main(parser.parse_args())
