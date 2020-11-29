import requests


def send_request(plaintext):
    response = requests.get("https://ebbae3ff35e2d3af.247ctf.com/encrypt", params={"plaintext": plaintext})
    return response.text


def xor_strings(string1, string2):
    bytestring1 = bytes.fromhex(string1)
    bytestring2 = bytes.fromhex(string2)
    return bytes([a ^ b for a, b in zip(bytestring1, bytestring2)]).hex()


def remove_block2_first_hexes(plaintext):
    return plaintext[:32] + plaintext[34:]


# first unknown byte is last byte of plaintext block 5
# Every time a new hex of the flag is known, remove the first hex of block 2, and in the case of known_plaintext,
# append the newly known hex at the end. Add the new flag hex to flag_hex
chosen_plaintext = "0" * 32 + "11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddee"
known_plaintext = "0" * 32 + "11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddee"
flag_hex = ""

for i in range(40):
    cypher = send_request(chosen_plaintext)

    cypher4 = cypher[32 * 3: 32 * 4]
    known_plain5 = known_plaintext[32 * 4: 32 * 5 - 2]
    cypher5 = cypher[4 * 32: 5 * 32]

    for j in range(256):
        # We are guessing what the last character of block5 could possibly be (only unknown char of block 5)
        # By 'assuming' it is a certain value, we gain a possible plain5
        # Because we known cypher4, we can determine what the input5 would be IF our guess is correct
        # Now, we want input2 to be the same as possible_input5, which we can easily do because we know cypher 1,
        # and so we just need to choose plain2 in such a way that input2 equals possible_input5.
        # If cypher2 == cypher5, we know that our guess was correct.
        # we can now take 'possible_last_hex', and add that to the flag_hex. Then perform all operations specified
        # above chosen_plaintext and known_plaintext.
        # possible_last_hexes = "32"
        possible_last_hexes = "0" * (2 - len(hex(j)[2:])) + hex(j)[2:]

        possible_plain5 = known_plain5 + possible_last_hexes
        possible_AES_input5 = xor_strings(cypher4, possible_plain5)

        cypher1 = cypher[0:32]
        plain2 = xor_strings(possible_AES_input5, cypher1)

        second_plaintext = chosen_plaintext[0:32] + plain2 + chosen_plaintext[64:]

        # SENDING THE SECOND REQUEST

        cypher = send_request(second_plaintext)
        cypher2 = cypher[1 * 32: 2 * 32]

        if cypher5 == cypher2:
            flag_hex += possible_last_hexes
            chosen_plaintext = remove_block2_first_hexes(chosen_plaintext)
            known_plaintext = remove_block2_first_hexes(known_plaintext) + possible_last_hexes
            break

    print(bytes.fromhex(flag_hex).decode("ascii"))
