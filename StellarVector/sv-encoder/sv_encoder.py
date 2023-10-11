import base64 as b64

flag = b'sv{FAKE_FLAG}'

flag = b64.b16encode(flag)

for i in range(20):
	flag = b64.b64encode(flag)

for j in range(5):
	flag = b64.b16encode(flag)

flag = flag.decode()

with open('out.txt', 'w') as fh:
	fh.write(flag)

