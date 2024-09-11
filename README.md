# Secure Password Generator (in Python)
**This is a very secure password generator that never repeats itself because it saves SHA256 hashes of every password it generates and checks if this password already exists in the database. Still in development.**

This code uses the "secrets" library to generate secure passwords and will use SQLite or PostgreSQL to store hashes of passwords, but now it uses JSON to store hashes which is not really secure.
