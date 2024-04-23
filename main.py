from encrypt import encrypt_text
from decrypt import decrypt_text

def main():
    print("Welcome to DES Algorithm")
    print("Options: ")
    print("1: Encrypt a text")
    print("2: Decrypt a text")
    choice  = input("Enter your choice: ")

    if (choice == '1'):
        encrypt_text()
    elif (choice == '2'):    
        decrypt_text()
    else:
        print("You have entered a wrong choice")

main()

