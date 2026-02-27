import sqlite3

def init_db():
    conn = sqlite3.connect('realty.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def is_new_ad(link):
    conn = sqlite3.connect('realty.db')
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM ads WHERE link = ?', (link,))
    result = cursor.fetchone()
    if not result:
        cursor.execute('INSERT INTO ads (link) VALUES (?)', (link,))
        conn.commit()
        conn.close()
        return True
    conn.close()
    return False