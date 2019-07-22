#!/usr/bin/python3
import Crypto.Cipher as Cipher
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_v1_5_cipper
from Crypto.Signature import PKCS1_v1_5 as PKCS1_v1_5_sign
from Crypto.Hash import SHA512


class Rsa:
    """RSA加解密签名类
    """

    def __init__(self, cip_lib=PKCS1_v1_5_cipper, sign_lib=PKCS1_v1_5_sign, hash_lib=SHA512,
                pub_file=None, pri_file=None, pub_s_key=None, pri_s_key=None, pub_key=None, pri_key=None,
                reversed_size=11):

        # 加解密库
        self.ciper_lib = cip_lib
        self.sign_lib = sign_lib
        self.hash_lib = hash_lib

        # 公钥密钥
        if pub_key:
            self.pub_key = pub_key
        elif pub_s_key:
            self.pub_key = RSA.importKey(pub_s_key)
        elif pub_file:
            self.pub_key = RSA.importKey(open(pub_file).read())

        if pri_key:
            self.pri_key = pri_key
        elif pri_s_key:
            self.pri_key = RSA.importKey(pri_s_key)
        elif pri_file:
            self.pri_key = RSA.importKey(open(pri_file).read())

        # 分块保留长度
        self.block_reversed_size = reversed_size

    @staticmethod
    def gen_key(bit_len=1024, public="public_pem", private="private_pem"):
        rsa = RSA.generate(bit_len)

        private_pem = rsa.exportKey()
        with open(private, 'wb') as f:
            f.write(private_pem)

        public_pem = rsa.publickey().exportKey()
        with open(public, 'wb') as f:
            f.write(public_pem)

    # 根据key长度计算分块大小
    def get_block_size(self, rsa_key):
        bs = 0
        try:
            # RSA仅支持限定长度内的数据的加解密，需要分块
            # 分块大小
            reserve_size = self.block_reversed_size
            key_size = rsa_key.size() + 1
            print("----->key:%d" % key_size)
            if (key_size % 8) != 0:
                raise RuntimeError('RSA 密钥长度非法')

            # 密钥用来解密，解密不需要预留长度
            if rsa_key.has_private():
                reserve_size = 0

            bs = int(key_size / 8) - reserve_size
        except Exception as err:
            print('计算加解密数据块大小出错', rsa_key, err)
        return bs

    # 返回块数据
    def block_data(self, data, rsa_key):
        bs = self.get_block_size(rsa_key)
        for i in range(0, len(data), bs):
            yield data[i:i + bs]

    # 加密
    def enc_bytes(self, data, key=None):
        text = b''
        try:
            rsa_key = self.pub_key
            if key:
                rsa_key = key

            cipher = self.ciper_lib.new(rsa_key)
            for dat in self.block_data(data, rsa_key):
                cur_text = cipher.encrypt(dat)
                text += cur_text
        except Exception as err:
            print('RSA加密失败', data, err)
        return text

    def enc_file(self, file_in, file_out, key=None):
        with open(file_out, 'wb') as f:
            f.write(self.enc_bytes(open(file_in, 'rb').read(), key))

    # 解密
    def dec_bytes(self, data, key=None):
        text = b''
        try:
            rsa_key = self.pri_key
            if key:
                rsa_key = key

            cipher = self.ciper_lib.new(rsa_key)
            for dat in self.block_data(data, rsa_key):
                if type(self.ciper_lib) == Cipher.PKCS1_v1_5:
                    cur_text = cipher.decrypt(dat)
                else:
                    cur_text = cipher.decrypt(dat, '解密异常')
                text += cur_text
        except Exception as err:
            print('RSA解密失败', data, err)
        return text

    def dec_file(self, file_in, file_out, key=None):
        with open(file_out, 'wb') as f:
            f.write(self.dec_bytes(open(file_in, 'rb').read(), key))

    # RSA签名
    def sign_bytes(self, data, key=None):
        signature = ''
        try:
            rsa_key = self.pri_key
            if key:
                rsa_key = key

            h = self.hash_lib.new(data)
            signature = self.sign_lib.new(rsa_key).sign(h)
        except Exception as err:
            print('RSA签名失败', '', err)
        return signature

    # RSA签名验证
    def sign_verify(self, data, sig, key=None):
        try:
            rsa_key = self.pub_key
            if key:
                rsa_key = key
            h = self.hash_lib.new(data)
            self.sign_lib.new(rsa_key).verify(h, sig)
            ret = True
        except (ValueError, TypeError):
            ret = False
        return ret


def main():
    # Rsa.gen_key(1024)
    # rsa = Rsa(pub_file="public_pem")
    # rsa.enc_file("../DynamicLoad/load_test.py", "load_test")
    # rsa = Rsa(pri_file="private_pem")
    # rsa.dec_file("load_test", "load_test.py")
    pass


if __name__ == '__main__':
    main()
