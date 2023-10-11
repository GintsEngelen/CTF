import base64 as b64

with open('out.txt', 'r') as f:
    outputted_flag = f.read()

    encoded_flag = bytes(outputted_flag, 'utf-8')

    for i in range(5):
        encoded_flag = b64.b16decode(encoded_flag)

    for j in range(20):
        encoded_flag = b64.b64decode(encoded_flag)

    flag = b64.b16decode(encoded_flag)

    print(flag)
