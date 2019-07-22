#!/usr/bin/python3
import Crypto.Cipher as Cipher
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_v1_5_cipper
from Crypto.Signature import PKCS1_v1_5 as PKCS1_v1_5_sign
from Crypto.Hash import SHA512


class Rsa:
    """RSA加解密签名类
    """
    __pub_key = "-----BEGIN PUBLIC KEY-----\n" \
                "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0vyW/eNq8ABjycQA/ADv" \
                "RRNYYdSIM5T7zBNwExYOybZZhuQzAdTioQ32CnerkaEpeyliHQNcSSD7hN0xgS4i" \
                "jdCPpndzrUmHyCyzx5W7XSyV/vPbmbxi2pOys5p2H9J5aE6bw/HOfHo9/7oIzDtc" \
                "9vwh8Jc0D0rES/WFsVo8Gkml97laQD1MKH5R2zwM57k+XxITPiTlZLvMU2UCEQ9I" \
                "UipdKNSVNohaaxsle+TD66IlzvJT/9woe+Gx9J3HqutGtcKjxxV7u40Pn8N56dRM" \
                "ERUjAk4KhhHv4PLILdmEBFjlE9Iobtqwq2jVHxiZzsTM3Q6SOZ3Q7jaHtzAZcU/Z" \
                "LQIDAQAB" \
                "\n-----END PUBLIC KEY-----"
    __pri_key = "-----BEGIN RSA PRIVATE KEY-----\n" \
                "MIIEowIBAAKCAQEA0vyW/eNq8ABjycQA/ADvRRNYYdSIM5T7zBNwExYOybZ" \
                "ZhuQzAdTioQ32CnerkaEpeyliHQNcSSD7hN0xgS4ijdCPpndzrUmHyCyzx5W7XSyV/vPbmbxi2pOys5p2H9J5aE6bw" \
                "/HOfHo9/7oIzDtc9vwh8Jc0D0rES/WFsVo8Gkml97laQD1MKH5R2zwM57k+XxITPiTlZLvMU2UCEQ9IUipdKNSVNoh" \
                "aaxsle+TD66IlzvJT/9woe+Gx9J3HqutGtcKjxxV7u40Pn8N56dRMERUjAk4KhhHv4PLILdmEBFjlE9Iobtqwq2jVH" \
                "xiZzsTM3Q6SOZ3Q7jaHtzAZcU/ZLQIDAQABAoIBACOz3pEj9KqcRkaURl5egh68QU58uneQFHPaLjLsnp//nXK4FvG" \
                "OZrM+O45V5dCE5xISVKn4MZumWymGjKQBfJNm4YgX2plOQg3bkqiJa+U+cDtuZJDFUi0OpUTDNI35/dVqx+0GdByYS" \
                "vmFL4vv17FrxQqDa6nSyxjXeUIjtNv1n33VSS5qoOl+zxy7NXmEvManv+vg0dFLJ1d9SUgGKXurJE4GyX0ZeOyo5i6" \
                "25hM3gh/E+w0pDRekBlqZH6kkvgiWNrBdwQ638A2ma3Nez6Z3upticAqt4yhD4N3tdq6AyIToFnKBFpLuzF9BUUF48" \
                "Wg24eZEwRnKBMOe4S6PZTkCgYEA0yu8GuWMTHL0CnAsuAnWiVTEfJFPEMleRaCu99HrO+k98cT5EhBeIYRRNm52iHj" \
                "o8s7apRxBNE+HHMz61jq2W5vtt2DBFDS59UpDBkGryf5jqM/ODWejBcc5/PesucB/0X2FyDfgXPUTtBwK/qKmfF5Nc" \
                "tx4MPI9zbltsNm1MrcCgYEA/8bYwGZgUC02m+pt4NSZ2QTX2PsGuqh0XVEk6sazu9nhqbxV9dUSfdOt78zRJsMoP2+" \
                "nhde84ZkNkzOPUNxeTbsLL+4Bo5R3oHXyXkk7OoeasRx0LtylWZeNF87vsjZhG/Nbw70bFMj/sETlPmc1YMP/0M5Vy" \
                "tyNPD0cGArfHzsCgYBsw5roE5EWkyKk+a/evpp0M2fcbQ9XKxBWNnPICqPpQLH6A6Txq+J/yuH1ciG1GumIngg5gHs" \
                "JEWka6WzMyILCXmaqy7fGy314HF63Kz3rFQ6JlTag6t8pi7qPU5XwOnjbEpbEUBtMZaJXYxY6ntW3Ou8TGQEC3NH+U" \
                "uJvc0KDswKBgE5jLYiBl6DaynKsPPJ7lY7aGiCohh5shAUZWjwNm4XFt5AiZSHLJDilyBfG6I59nvcaC/hL7tog4vU" \
                "rBxAcCVa/LSWKRrxQQv1NSHM29EzyxCjldIHsI0y60oXqaLFwUwCS65uoeAU9uIbYBn3CeaxnRR5ELizWvP4qKFMB+" \
                "fGDAoGBAIgCtpaypGAqFg02aFaZTtuGR8gSwLlaYAUWvD8dspDqoPgFspqS88wqVTqSn4U0fYvrRGU4x4i9FTg1La9" \
                "ijUQb72DOwJLjbI2ksiMeuvIm9bdO4DH0jGl1P6SPrd4GuB3SA47e9HNYabFerBrMmRmHCT4P21C52W4BosfN+tb6-" \
                "\n----END RSA PRIVATE KEY-----"

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
        else:
            self.pub_key = RSA.importKey(Rsa.__pub_key)

        if pri_key:
            self.pri_key = pri_key
        elif pri_s_key:
            self.pri_key = RSA.importKey(pri_s_key)
        elif pri_file:
            self.pri_key = RSA.importKey(open(pri_file).read())
        else:
            self.pri_key = RSA.importKey(Rsa.__pri_key)

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
            if key:
                rsa_key = RSA.importKey(key)
            else:
                rsa_key = self.pub_key

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
            if key:
                rsa_key = RSA.importKey(key)
            else:
                rsa_key = self.pri_key

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

    def dec_str(self, file_in, key=None):
        return bytes.decode(self.dec_bytes(open(file_in, 'rb').read(), key))

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
    # Rsa.gen_key(2048)
    # rsa = Rsa(pub_file="public_pem")
    # rsa.enc_file("../DynamicLoad/load_test.py", "load_test")
    # rsa = Rsa(pri_file="private_pem")
    # print(rsa.dec_str("load_test"))
    pass


if __name__ == '__main__':
    main()
