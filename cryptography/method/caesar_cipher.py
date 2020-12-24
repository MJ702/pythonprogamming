def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + key - 65) + 65)
        else:
            result += chr((ord(char) + key - 97) + 97)

    return result


text = str(input("Enter your string to encrypt data: "))
key = int(input("Enter you key values: "))
ciphertext = encrypt(text, key)
print("Cipher: " + ciphertext)

