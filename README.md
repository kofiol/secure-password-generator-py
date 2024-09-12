# Secure Password Generator (in Python)

**This is a very secure password generator that never repeats itself because it saves SHA256 hashes of every password it generates and checks if this password already exists in the database. Still in development.**

This code uses the "secrets" library to generate secure passwords and will use SQLite or PostgreSQL to store hashes of passwords, but now it uses JSON to store hashes which is not really secure.

Maybe I will make the database remote and public so anyone can generate storng passwords that never have been used (or at least they are not in the database)

Also I may add passwords from breaches or rainbow tables so you can also check if your password is not secure not only because of the symbols content/count but rather on it's simplicity and if it was used too many times.
