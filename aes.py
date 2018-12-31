import base64
import sys

from Crypto.Cipher import AES

class AESEncrypter(object):
    def __init__(self):
        BS = 16
        self.pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        self.unpad = lambda s : s[0:-ord(s[-1])]
        iv = 16 * '\x00'
        key = 'conns-secret-keyconns-secret-key'
        self.cipher = AES.new(key, AES.MODE_CBC, iv)

    def encrypt(self, raw):
        raw = self.pad(raw)
        return base64.b64encode(cipher.encrypt(raw))

    def descrypt(self, enc):
        enc = self.__b64decode(enc)
        descrypted = self.cipher.decrypt(enc)
        return self.unpad(descrypted)

    def __b64decode(self, str):
        if len(str) % 4 != 0: #check if multiple of 4
            while len(str) % 4 != 0:
                str = str + "="
        print(str)
        return base64.b64decode(str)

if __name__ == "__main__":
    enc = sys.argv[1]
    print(enc)
    encrypter = AESEncrypter()
    print(encrypter.descrypt(enc))