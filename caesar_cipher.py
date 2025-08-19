def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            ascii_offset = ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)

        # Encrypt lowercase letters
        elif char.islower():
            ascii_offset = ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)

        # Leave numbers, spaces, and special characters unchanged
        else:
            result += char

    # If mode is decrypt, reverse the shift
    if mode == "decrypt":
        return caesar_cipher(text, -shift, "encrypt")
    return result


def main():
    print("=== Caesar Cipher Encryption/Decryption ===")

    text = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))
    mode = input("Choose (E)ncrypt or (D)ecrypt: ").strip().lower()

    if mode.startswith("e"):
        encrypted = caesar_cipher(text, shift, "encrypt")
        print(f"\nEncrypted Message: {encrypted}")

    elif mode.startswith("d"):
        decrypted = caesar_cipher(text, shift, "decrypt")
        print(f"\nDecrypted Message: {decrypted}")

    else:
        print("Invalid choice! Please enter E or D.")


if __name__ == "__main__":
    main()
