import sqlite3
from os.path import join
from src.db_management.utils.lang_operations import EN, RU

LANGS = (EN, RU)
DATABASE_PATH = join('databases', 'rules.db')


def create_skill_tables(rules_db, langs):
    for lang in langs:
        sql_create_skills_table = f"""CREATE TABLE IF NOT EXISTS skills_{lang} (
                                            en_name_hash text PRIMARY KEY, 
                                            name text NOT NULL, 
                                            char text NOT NULL, 
                                            description text, 
                                            "table" text, 
                                            example text, 
                                            specs text, 
                                            meta text);"""
        rules_db.execute(sql_create_skills_table)


def create_talent_table(rules_db, langs):
    for lang in langs:
        sql_create_skills_table = f"""CREATE TABLE IF NOT EXISTS talents_{lang} (
                                            name_hash text PRIMARY KEY, 
                                            name text NOT NULL, 
                                            max_picked text, 
                                            checks text, 
                                            checks_description text, 
                                            description text, 
                                            table_link text, 
                                            example text, 
                                            spec text);"""
        rules_db.execute(sql_create_skills_table)


if __name__ == '__main__':
    with sqlite3.connect(DATABASE_PATH) as rules_db:
        create_talent_table(rules_db, LANGS)
