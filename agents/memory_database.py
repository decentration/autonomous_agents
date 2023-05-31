import sqlite3
import numpy as np

class MemoryDatabase:
    def __init__(self, db_name='memory_database.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS memories (
            id TEXT PRIMARY KEY,
            content TEXT NOT NULL,
            timestamp TIMESTAMP NOT NULL,
            importance INTEGER NOT NULL,
            embedding BLOB NOT NULL
        );
        ''')
        self.conn.commit()

    def insert_memory(self, memory):
        cursor = self.conn.cursor()
        cursor.execute('''
        INSERT INTO memories (id, content, timestamp, importance, embedding)
        VALUES (?, ?, ?, ?, ?)
        ''', (memory.id, memory.content, memory.timestamp, memory.importance, memory.embedding.tobytes()))

        self.conn.commit()

    def get_memories(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM memories')
        memories = []

        for row in cursor.fetchall():
            id, content, timestamp, importance, embedding = row
            memory = Memory(id=id, content=content, timestamp=timestamp, importance=importance, embedding=np.frombuffer(embedding, dtype=np.float32))
            memories.append(memory)

        return memories

    def close(self):
        self.conn.close()
