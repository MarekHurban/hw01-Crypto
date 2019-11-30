from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import random
import sys

def xorBytes(i1, i2):
    xorInt = int.from_bytes(i1, "big") ^ int.from_bytes(i2, "big")
    return xorInt.to_bytes(16, "big")

# returns AES encrypted key in CBC mode
# docs for used functions can be found at https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
def aesEncrypt(key, iv):
    encKey = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()).encryptor()
    return encKey

# ANSI X9.31 - variables are named as in assignment
def ansiX9_31(aes, v, dt):
    i = aes.update(dt)
    r = aes.update(xorBytes(i, v))
    v = aes.update(xorBytes(r, i))
    return [r, v]

# we have to treat key and seed as hex not ascii char
def transform(s):
    intArr = []
    for i in s:
        intArr.append(int(i))
    return bytes(bytearray(intArr))

# ecryption key (reversed UCO)
v = "4439394439394439" # (secret)
k = reversed(v) # (secret)
v = transform(v)
k = transform(k)
iv = int.to_bytes(random.getrandbits(128), 16, "big") # (secret)
dt = 0x0
dt = dt.to_bytes(16, "big")
aes = aesEncrypt(k, iv)
# v, k, dt have to be 128-bit


# ANSI X9.31
# every iteration generates 128-bits long random array
with open("F.bin", 'wb') as outFile:
    for _ in range((10 ** 9) // 128):
        resultList = ansiX9_31(aes, v, dt)   
        outFile.write(resultList[0])
        v = resultList[1]
        dt = int.from_bytes(dt, "big")
        dt += 1
        dt = dt.to_bytes(16, "big")


# random bytes generated by build in function for comparison of results
outByteArr = bytearray()
random.seed(443939)
for _ in range((10**9) // 32):
    outByteArr.extend(bytearray(random.randint(0, 2147483647).to_bytes(4, "big")))
    # value 2147483647 is used as RANDMAX (maxInt) in C rand() function from assignment

with open("F2.bin", 'wb') as outFile:
    outFile.write(outByteArr)