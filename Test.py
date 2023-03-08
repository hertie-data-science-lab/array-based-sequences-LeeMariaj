from Encryption import encrypt
from Decryption import decrypt

message = "This is a Sample Message"

coded = encrypt(message, 5)
print("Secret: ", coded)

answer = decrypt(coded, 5)
print("Message: ", answer)