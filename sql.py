import sqlite3


class work_with_sqlite:
    def __init__(self,
                 name):
        self.name = name

    def delete_all(self):
        db = sqlite3.connect(self.name)
        sql = db.cursor()
        sql.execute("""DELETE
         FROM
         score 
         where 
         count >0""")

    def write(self,
              masiv):
        x = masiv
        db = sqlite3.connect(self.name)
        sql = db.cursor()

        work_with_sqlite(self.name).delete_all()
        sql.execute(f"INSERT INTO"
                    f" score(count)"
                    f" VALUES({int(x)})")
        db.commit()

    def take_record(self):
        db = sqlite3.connect(self.name)
        sql = db.cursor()
        na = sql.execute("""SELECT
         count
         FROM 
         score""").fetchall()[-1][0]
        db.commit()
        return (na)
