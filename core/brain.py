import sqlite3

class Brain:
    def __init__(self, user_id):
        self.user_id = user_id
        self.conn = sqlite.connect("wabbi.db")
        self.cursor = self.conn.cursor()
        self._setup()

    def _setup(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS profiles (
                user_id TEXT PRIMARY KEY,
                wins INTEGER DEFAULT 0,
                losses INTEGER DEFAULT 0,
                mood TEXT DEFAULT 'neutral',
                study_hours INTEGER DEFAULT 0
            )                
        """)
        self.conn.commit()
        self.cursor.execute("INSERT OR IGNORE INTO profiles (user_id) VALUES (?)", (self.user_id,))
        self.conn.commit()

    def get(self, key):
        self.cursor.execute(f"SELECT {key} FROM profiles WHERE user_id = ?", (self.user_id,))
        row = self.cursor.fetchone()
        return row[0] if row else None
    
    def set(self, key, value):
        self.cursor.execute(f"UPDATE profiles SET {key} = ? WHERE user_id = ?", (value, self.user_id))
        self.conn.commit()