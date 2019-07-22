#!/usr/bin/python3


class Engine:
    __keygen = "nesum lite scan"

    def __init__(self):
        module_sql = __import__("lib.mysql")
        self.MySql = module_sql.mysql.MySql

        module_crypt = __import__("lib.key_crypt")
        self.Crypt = module_crypt.key_crypt.Crypt

    def crypt_file(self, filepath, output):
        keygen = self.Crypt.gen_key_by_str(self.__keygen)
        self.Crypt.crypt_save_file(filepath, output, keygen)

    def decrypt_file(self, filepath):
        keygen = self.Crypt.gen_key_by_str(self.__keygen)
        return self.Crypt.get_crypt_file_byte(filepath, keygen)

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
    engine.run_module("load_test")
    engine.run_module("module1")
    engine.run_module("module2")
