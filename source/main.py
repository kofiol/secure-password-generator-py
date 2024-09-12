import secrets
import string
import colorama
from colorama import just_fix_windows_console
just_fix_windows_console()
import hashlib
import database


with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read().splitlines()


print("this is a password generator that never repeats itself! it also adds a word to the end or the start of the password so you can easily organize and even memorize it!")


symbols_amount = int(input("now select the amount of symbols you want to generate (we recommend 15-25 symbols): "))

alphabet = string.ascii_letters + string.digits + string.punctuation


while True:
    additional_word = secrets.choice(dictionary)
    if 3 <= len(additional_word) <= 7:
        break


symbols_amount = max(1, symbols_amount - len(additional_word))


while True:
    password = ''.join(secrets.choice(alphabet) for i in range(symbols_amount))
    password = password + additional_word if secrets.choice([True, False]) else additional_word + password
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c in string.punctuation for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break


while True:
    hash_object = hashlib.sha256()
    hash_object.update(password.encode('utf-8'))
    hash = hash_object.hexdigest()
    if database.hash_exists(hash):
        print(f"looks like the hash is already present in the database, generating a new one.")
        while True:
            additional_word = secrets.choice(dictionary)
            if 3 <= len(additional_word) <= 7:
                break


        symbols_amount = int(input("now select the amount of symbols you want to generate (we recommend 15-25 symbols): ")) - len(additional_word)
        symbols_amount = max(1, symbols_amount)  
        password = ''.join(secrets.choice(alphabet) for i in range(symbols_amount))
        password = password + additional_word if secrets.choice([True, False]) else additional_word + password
    else:
        print(f"the password is not present in the database, you can use it.")
        break


print("your password is: " + colorama.Fore.GREEN + password + colorama.Style.RESET_ALL)
print("advise: better save it on paper or at least in a reliable password manager!")


database.add_hash(hash)

