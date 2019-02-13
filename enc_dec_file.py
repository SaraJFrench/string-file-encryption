#encrypt
from cryptography.fernet import Fernet

file=open('key.key', 'rb')


key = file.read()
file.close
with open('secretFile.txt', 'rb') as f:
    data=f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open('secretFile.encrypted', 'wb') as f:
    f.write(encrypted)







#decrypt

from cryptography.fernet import Fernet

file=open('key.key', 'rb')
key = file.read()
file.close

with open('secretFile.encrypted', 'rb') as f:
    data=f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open('secretFile.decrypted', 'wb') as f:
    f.write(encrypted)
