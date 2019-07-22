#!/usr/bin/python3
import sys
import random
import os


def encode(s):
    return [bin(ord(c)).replace('0b', '') for c in s]


def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


class Crypt:
    @staticmethod
    def gen_key():
        c = list(range(256))
        random.shuffle(c)
        return c

    @staticmethod
    def gen_key_by_str(key_str):
        fk = bytes("nesum112314", encoding="utf-8")
        fk_len = len(fk)
        key_byte = bytes(key_str, encoding="utf-8")
        key_len = len(key_byte)
        buff = []
        for i in range(key_len):
            c = i % fk_len
            fo = key_byte[i] ^ fk[c]
            buff.append(fo)
        return buff

    @staticmethod
    def save_key_file(k, f):
        fo = open(f, 'wb')
        fo.write(bytes(k))
        fo.close()

    @staticmethod
    def get_key(f):
        fi = open(f, 'rb')
        k = fi.read()
        fi.close()
        return k

    @staticmethod
    def crypt_file(fi, fo, key_file):
        k = Crypt.get_key(key_file)
        f = open(fi, 'rb')
        fc = f.read()
        fe = open(fo, 'wb')
        file_len = len(fc)
        buff = []
        for i in range(file_len):
            c = i % len(k)
            fo = fc[i] ^ k[c]
            buff.append(fo)
        fe.write(bytes(buff))
        f.close()
        fe.close()

    @staticmethod
    def get_crypt_file_byte(file, key):
        f = open(file, 'rb')
        fc = f.read()
        file_len = len(fc)
        key_len = len(key)
        buff = []
        for i in range(file_len):
            c = i % key_len
            fo = fc[i] ^ key[c]
            buff.append(fo)
        return bytes.decode(bytes(buff))

    @staticmethod
    def crypt_save_file(file, out_file, key):
        f = open(file, 'rb')
        fc = f.read()
        file_len = len(fc)
        key_len = len(key)
        buff = []
        for i in range(file_len):
            c = i % key_len
            fo = fc[i] ^ key[c]
            buff.append(fo)

        fo = open(out_file, "wb")
        fo.write(bytes(buff))
        fo.close()

    @staticmethod
    def crypt_dir(d, key_file):
        """
        encrypt a directory assigned by <d>
        """
        file_list = os.listdir(d)
        file_count = len(file_list)
        for i in range(file_count):
            f = os.path.join(d, file_list[i])
            neof = f + '.crypt'
            Crypt.crypt_file(f, neof, key_file)
            print('Progress:%d/%d' % (i + 1, file_count))
        print('Directory <%s> has been encrypted/decrypted.' % d)


if __name__ == '__main__':
    args = sys.argv
    arg_num = len(args)

    if arg_num == 2:
        neokey = Crypt.gen_key()
        Crypt.save_key_file(neokey, args[1])
        print('Key file has been generated:%s' % (args[1]))
        exit(0)

    if arg_num == 3:
        Crypt.crypt_dir(args[1], args[2])
        exit(0)

    if len(args) != 4:
        print('Usage:simplecrypt.py <input file> <output file> <key file>')
        exit(-1)
    Crypt.crypt_file(args[1], args[2], args[3])
    print('Done!')
