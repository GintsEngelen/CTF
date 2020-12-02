import requests


def send_request(plaintext):
    response = requests.get("https://1b59caf791ee3eb8.247ctf.com/encrypt", params={"plaintext": plaintext})
    return response.text


def xor_strings(string1, string2):
    bytestring1 = bytes.fromhex(string1)
    bytestring2 = bytes.fromhex(string2)
    return bytes([a ^ b for a, b in zip(bytestring1, bytestring2)]).hex()


def remove_block2_first_hexes(plaintext):
    return plaintext[:32] + plaintext[34:]


