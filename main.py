import pwn
import requests as req

conn = pwn.remote('85a1e8053b4c05b0.247ctf.com', 50221)

for i in range(500):
    pre_line = conn.recvuntil(b'What is the answer to ', drop=False)
    line = conn.recv()
    n1, n2 = line[:-3].split(b" + ")
    conn.send(str(int(n1) + int(n2)) + "\r\n")

flag = conn.recv()
print(flag)