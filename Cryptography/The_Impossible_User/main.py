from Crypto.Cipher import AES
from flask import Flask, request
from secret import flag, aes_key, secret_key

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.config['DEBUG'] = False
flag_user = 'impossible_flag_user'

class AESCipher():
    def __init__(self):
        self.key = aes_key
        self.cipher = AES.new(self.key, AES.MODE_ECB)
        self.pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) \
                             * chr(AES.block_size - len(s) % AES.block_size)
        self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    def encrypt(self, plaintext):
        return self.cipher.encrypt(bytes(self.pad(plaintext), "ascii")).hex()

    def decrypt(self, encrypted):
        return self.unpad(self.cipher.decrypt(bytes.fromhex(encrypted)))

@app.route("/")
def main():
    return "%s" % open(__file__).read()

@app.route("/encrypt")
def encrypt():
    try:
        user = request.args.get('user')
        print(user)
        if user == flag_user:
            return 'No cheating!'
        return AESCipher().encrypt(user)
    except Exception as e:
        print(e)
        return 'Something went wrong!'

@app.route("/get_flag")
def get_flag():
    try:
        if AESCipher().decrypt(request.args.get('user')) == flag_user:
            return flag
        else:
            return 'Invalid user!'
    except:
        return 'Something went wrong!'

if __name__ == "__main__":
  app.run()

#
# 247CTF{

"44b03ac6f9bf915b57090ff37e00980949815e08ab00dbc96cb571ec8f2dd2fa0a9671b7dc8981280322d21b0521d50105975c1cff3b3d90249d817f06270a20"