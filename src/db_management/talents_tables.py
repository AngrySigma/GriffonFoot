import sqlite3
from Talent import Talent
from rules_db import *


def add_talent(rules_db, talent: Talent):
    sql_add_talent = f""" INSERT INTO talents_{talent.lang} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    rules_db.execute(sql_add_talent, (talent.name_hash, talent.name, talent.max, talent.checks, talent.checks_desk, talent.desc, talent.table_link, talent.example, talent.spec))
    rules_db.commit()


if __name__ == "__main__":
    talent = Talent(EN, 'test talent', 1, 'test checks', 'test desc')
    rules_db = sqlite3.connect(DATABASE_PATH)
    add_talent(rules_db, talent)
    rules_db.close()
