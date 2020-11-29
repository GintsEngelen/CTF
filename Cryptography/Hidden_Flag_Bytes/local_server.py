from Crypto.Cipher import AES
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = False

aes_key = bytes.fromhex("11223344556677889900aabbccddeeff")
iv = bytes.fromhex("11223344556677889900aabbccddeeff")
flag = b"247CTF{" + 32*b"0" + b"}"

class AESCipher():
    def __init__(self):
        self.pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * bytes([AES.block_size - len(s) % AES.block_size])

    def encrypt(self, plaintext):
        return AES.new(aes_key, AES.MODE_CBC, iv).encrypt(self.pad(plaintext + flag)).hex()

@app.route("/")
def main():
    return "%s" % open(__file__).read()

@app.route("/encrypt")
def encrypt():
    try:
        plaintext = request.args.get('plaintext')
        full_plaintext = bytes.fromhex(plaintext) + flag
        print(full_plaintext)
        print("my plaintext = ", plaintext)
        print("full plaintext = ", bytes.fromhex(plaintext) + flag)
        print(AESCipher().encrypt(bytes.fromhex(plaintext)))
        return AESCipher().encrypt(bytes.fromhex(plaintext))
    except Exception as e:
        print(e)
        return 'Something went wrong!'

if __name__ == "__main__":
    app.run()
