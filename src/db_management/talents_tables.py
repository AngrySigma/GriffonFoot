import sqlite3
from Talent import Talent
from rules_db import *
from utils.lang_operations import EN, RU


if __name__ == "__main__":
    new_talent = Talent()
    new_talent.set_lang_version(EN, 'nibba', 1, 'just strong back', 'athletics')
    new_talent.set_lang_version(RU, 'васян', 1, 'просто сильная спина', 'атлетика')
    with sqlite3.connect(DATABASE_PATH) as rules_db:
        new_talent.add_talent(rules_db)

