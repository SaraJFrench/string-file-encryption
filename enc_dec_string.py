from cryptography.fernet import Fernet

file=open('key.key', 'rb')
key = file.read()
file.close()


#encode
message = "my secret message"
encoded = message.encode()

f = Fernet(key)
encrypted = f.encrypt(encoded)
#print(encrypted)

#get key
file=open('key.key', 'rb')
key2=file.read()
file.close

#decrypt
f2=Fernet(key)
decrypted=decrypted=f2.decrypt(encrypted)

print(decrypted)
