from flask import Flask, session, request
from Crypto.Cipher import AES
import os

aes_key = bytes.fromhex("11223344556677889900aabbccddeeff")
iv = bytes.fromhex("11223344556677889900aabbccddeeff")
flag = b"247CTF{" + 32*b"0" + b"}"

class AESCipher:
    def __init__(self):
        self.pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * chr(
            AES.block_size - len(s) % AES.block_size
        )
        self.used_ivs = set()

    def encrypt(self, raw):
        iv = session.get("IV")
        if iv in self.used_ivs:
            return "Too predictable!"
        self.used_ivs.add(iv)
        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(self.pad(raw + flag))
        session["IV"] = encrypted[-AES.block_size :]
        return encrypted.hex()


app = Flask(__name__)
app.config["DEBUG"] = False
custom_cipher = AESCipher()


@app.before_request
def before_request():
    if session.get("IV") is None:
        session["IV"] = os.urandom(16)


@app.route("/")
def main():
    return "%s" % open(__file__).read()


@app.route("/flag_format")
def flag_format():
    return """The flag format for this challenge is non-standard.

        The flag to obtain for this challenge (stored in the flag variable) is 32-HEX only.

        Once you obtain this flag, submit your solution in the regular 247CTF{32-HEX} format."""


@app.route("/encrypt")
def encrypt():
    try:
        return custom_cipher.encrypt(
            bytes.fromhex(request.args.get("plaintext"))[: AES.block_size * 2]
        )
    except:
        return "Something went wrong!"


if __name__ == "__main__":
    app.run()
