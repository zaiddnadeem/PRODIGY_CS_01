def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def display_menu():
    print("\n" + "=" * 40)
    print("      CAESAR CIPHER TOOL")
    print("=" * 40)
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")
    print("=" * 40)


while True:
    display_menu()

    choice = input("Enter your choice (1-3): ")

    if choice in ["1", "2"]:
        text = input("\nEnter your message: ")

        while True:
            try:
                shift = int(input("Enter shift value (1-25): "))
                if 1 <= shift <= 25:
                    break
                print("Shift must be between 1 and 25.")
            except ValueError:
                print("Please enter a valid number.")

        if choice == "1":
            result = caesar_cipher(text, shift, "encrypt")
            print("\nEncrypted Message:", result)

        else:
            result = caesar_cipher(text, shift, "decrypt")
            print("\nDecrypted Message:", result)

    elif choice == "3":
        print("\nThank you for using Caesar Cipher Tool!")
        break

    else:
        print("\nInvalid choice. Please try again.")
