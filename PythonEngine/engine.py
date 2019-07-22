#!/usr/bin/python3


# 引擎脚本,用于调用不同扫描模块或者直接调用正则处理漏洞文件
class Engine:
    def __init__(self):
        module_sql = __import__("lib.mysql")
        self.MySql = module_sql.mysql.MySql

        module_crypt = __import__("lib.rsa_crypt")
        self.Rsa = module_crypt.rsa_crypt.Rsa()

    def crypt_file(self, filepath, output):
        self.Rsa.enc_file(filepath, output)

    def decrypt_file(self, filepath):
        return self.Rsa.dec_str(filepath)

    def test_sql(self):
        mysql = self.MySql("127.0.0.1", 3306, "root", "1234", "python-sql")
        ins_str = "INSERT INTO vulnerability_detail SET name = 'bug1',description = '描述'," \
                  "company = '能信安' "
        mysql.run_sql(ins_str)

        sel_str = "SELECT * FROM vulnerability_detail"
        data = []
        mysql.run_sql_value(sel_str, data)
        print(data)

    def run_regex(self, regex_str):
        print("run python regex!")

    def run_module(self, module_name):
        context = globals().copy()
        exec(self.decrypt_file("lib/" + module_name), context)


if __name__ == "__main__":
    engine = Engine()
    engine.crypt_file("../DynamicLoad/load_test.py", "./lib/load_test")
    # engine.run_module("load_test")
    # engine.run_module("module1")
    # engine.run_module("module2")
