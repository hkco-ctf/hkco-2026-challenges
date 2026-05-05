from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad

key = bytes.fromhex('6ea9c53b30804bff3422f9ebfa7ff6f750e99625b7d0d0fd0b7dd71de16ec231')
with open("secret.enc", "rb") as f:
    data = f.read()

iv = data[-16:]
ciphertext = data[:-16]

cipher = AES.new(key, AES.MODE_CBC, iv)

decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
print(decrypted_data.decode('utf-8'))
