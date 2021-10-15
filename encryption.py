import rsa

keys_list = {}

publicKey, privateKey = rsa.newkeys(512)

keys_list[publicKey] = privateKey
message = "ankit"

enc = rsa.encrypt(message.encode(), publicKey)

print("origibal String: ", message)
print("encrypted String: ", enc)

decMessage = rsa.decrypt(enc, privateKey).decode()

print("decrypted message: ", decMessage)