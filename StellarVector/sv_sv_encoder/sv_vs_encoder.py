import base64 as b64

def magic_shuffle(poor_string):
	assert type(poor_string) == bytes, 'Magicians only use bytestrings'

	magic_string = b''

	for c in poor_string:
		
		mask = 0b11
		b0 = c & mask
		b1 = (c >> 2) & mask
		b2 = (c >> 4) & mask
		b3 = (c >> 6) & mask

		magic_char = bytes([bi + 32 for bi in [b1, b3, b0, b2] ])
		print(f'{magic_char = }')

		magic_string += magic_char

	return magic_string


flag = b'sv{FAKE_FLAG}'

flag = magic_shuffle(flag)
flag = b64.b16encode(flag)

print(f'{flag = }')
