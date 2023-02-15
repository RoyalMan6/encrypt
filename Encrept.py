from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

plainDir = 'plain.txt'

with open(plainDir) as file:
    data = file.read.replace('n','')

message = data
plainT = message

keyPair= RSA.generate(1000)

pkey = keyPair.export_key()
print(pkey.decode('ascii')+'\n')
