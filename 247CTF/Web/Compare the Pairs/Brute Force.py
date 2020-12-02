import hashlib
import re

def isTargetHashFound(digest):
    return re.match("0e[0-9]{30}", digest.hex())


def nat():
    n = 0
    while True:
        yield n
        n = n + 1

for i in nat():
    if isTargetHashFound(hashlib.md5(bytes("f789bbc328a3d1a3" + str(i) , "ascii")).digest()):
        print("cracked input: ", i)
        break

