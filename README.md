# Secure Password Generator (in Python)

**This is a very secure password generator that never repeats itself because it saves SHA256 hashes of every password it generates and checks if this password already exists in the database. Still in development.**

This code uses the "secrets" library to generate secure passwords and it uses SQLite to store SHA256 hashes of passwords, which are generated using the "hashlib" library

Maybe I will add passwords from breaches or rainbow tables so you can also check if your password is not secure not only because of the symbols content/count but rather on it's simplicity and if it was used too many times.
