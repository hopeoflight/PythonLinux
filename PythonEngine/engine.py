#!/usr/bin/python3
import json


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
    def get_id(style):
        return json.dumps(Engine.__Vul.get_id(style), ensure_ascii=False)

    @staticmethod
    def get_type(vul_id):
        return json.dumps(Engine.__Vul.get_type(vul_id), ensure_ascii=False)

    @staticmethod
    def get_content(vul_id=None, style=None):
        return json.dumps(Engine.__Vul.get_content(vul_id, style), ensure_ascii=False)


if __name__ == "__main__":
    # Engine.crypt_file("../DynamicLoad/load_test.py", "./lib/load_test")
    # Engine.run_module("load_test")
    # Engine.run_module("module1")
    # Engine.run_module("module2")
    print(Engine.get_content())
    pass
