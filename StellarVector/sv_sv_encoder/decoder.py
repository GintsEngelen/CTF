import base64 as b64

def magic_shuffle(poor_string):
    assert type(poor_string) == bytes, 'Magicians only use bytestrings'

    magic_string = b''

    for i in range(0, len(poor_string), 4):
        four_chars = poor_string[i:i+4]
        
        print(four_chars)
        print("\r\n")

        mask = 0b11
        b0 = (four_chars[3] & mask) << 4
        b1 = (four_chars[2] & mask) << 0 
        b2 = (four_chars[1] & mask) << 6
        b3 = (four_chars[0] & mask) << 2

        magic_char = bytes(b0 | b1 | b2 | b3)
        print(f'{magic_char = }')

        magic_string += magic_char

    return magic_string


flag = b'20212323212122232221232320212323202020232321232122212123202020232121212323212321212020232021222320202323232123212120202323212321232121222120202321212322202021232021232220202123212020232321222223212321212120232020202320202023202021222020212223212123'

flag = b64.b16decode(flag)
flag = magic_shuffle(flag)


print(f'{flag = }')
