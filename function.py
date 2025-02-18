import random

chars = "qwertyuiop[]asdfghjkl;'zxcvbnm,./1234567890-=_+{}|:"
password = ""
print("How long should the password be?")
def ConsoleText():
    while True:
        password = ""
        try:
            length = int(input("How long?: "))
            while len(password) < length:
                password += random.choice(chars)
            print(password)
        except ValueError:
            print("Invalid value, try again")
