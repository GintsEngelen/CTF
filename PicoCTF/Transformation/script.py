with open("enc",'r') as f:
    data = f.read()
    flag = ""
    for character in data:
        first_char = chr(ord(character) >> 8)
        second_char = chr(ord(character) - (ord(first_char) << 8))
        flag += first_char
        flag += second_char
print(flag)

