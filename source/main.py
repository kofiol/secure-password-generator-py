import secrets
import string
import colorama
from colorama import just_fix_windows_console
just_fix_windows_console()
import hashlib
import json
# from database import Database

with open('hashes.json') as file:
    data = json.load(file)

print("this is a password generator that never repeats itself!")

symbols_amount = int(input("now select the amount of symbols you want to generate (we recommend 15-25 symbols): "))

alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(symbols_amount))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break

hash_object = hashlib.sha256()
hash_object.update(password.encode('utf-8'))
hash = hash_object.hexdigest()

# db = Database('hashes.db')
# db.add_new_hash(hash)

# make real checking if the password is strong or not and implement function to remake the password again if it is not strong
# add database thing so it actually never repeats
# maybe will do json for now because just easier

print(colorama.Fore.GREEN + password + colorama.Style.RESET_ALL)
print(colorama.Fore.RED + hash)
print(colorama.Fore.BLUE + data['1'] + colorama.Style.RESET_ALL)

