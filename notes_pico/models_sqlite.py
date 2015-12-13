import uorm


db = uorm.DB("sqlite.db")


class Note(uorm.Model):

    __db__ = db
    __table__ = "note"
    __pkey__ = "timestamp"
    __schema__ = """
        CREATE TABLE note(
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP PRIMARY KEY,
        archived INT NOT NULL DEFAULT 0,
        content TEXT NOT NULL
        )
    """

    @classmethod
    def public(cls):
        return cls.execute("""
            SELECT * FROM note
            WHERE archived=0
            ORDER BY timestamp
        """)
