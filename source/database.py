import sqlite3


def connect_db():
    return sqlite3.connect('hashes.db')


def create_table():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hashes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                hash TEXT UNIQUE
            )
        ''')
        conn.commit()


def hash_exists(hash):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM hashes WHERE hash = ?', (hash,))
        return cursor.fetchone() is not None


def add_hash(hash):
    with connect_db() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO hashes (hash) VALUES (?)', (hash,))
            conn.commit()
        except sqlite3.IntegrityError:
            pass


create_table()
