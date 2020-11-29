with open("my_magic_bytes.jpg.enc", "rb") as enc_jpg:
    enc = enc_jpg.read()

jpeg_magic_numbers = [b"\xFF\xD8\xFF\xDB",
                 b"\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01",
                 b"\xFF\xD8\xFF\xEE",
                 b"\xFF\xD8\xFF\xE1\xAA\xAA\x45\x78\x69\x66\x00\x00"]

possible_keys = []


def xor_bytestrings(string1, string2):
    return bytes([a ^ b for a, b in zip(string1, string2)])


for magic_number in jpeg_magic_numbers:
    possible_keys.append(xor_bytestrings(magic_number, enc[:len(magic_number)]))


def decrypt_xor(key, encrypted_file):
    key_length = len(key)
    decrypted_file = []
    for (i, current_byte) in enumerate(encrypted_file):
        key_index = i % key_length
        decrypted_file.append(key[key_index] ^ current_byte)
    return bytes(decrypted_file)


for key in possible_keys:
    decrypted_file = decrypt_xor(key, enc)
    with open(key.hex(), "wb") as whatever:
        whatever.write(decrypted_file)
