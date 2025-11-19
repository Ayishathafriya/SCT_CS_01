def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# User input
message = input("Enter your message: ")
shift_value = int(input("Enter shift value (e.g., 3): "))

# Encryption
encrypted_message = caesar_encrypt(message, shift_value)
print("Encrypted message:", encrypted_message)

# Decryption
decrypted_message = caesar_decrypt(encrypted_message, shift_value)
print("Decrypted message:", decrypted_message)
