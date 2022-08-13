import sqlite3

EN = 'en'
RU = 'ru'
DATABASE_PATH = r'databases/rules.db'


def create_skills_tables(rules_db, langs):
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


def create_talents_table(rules_db, langs):
    for lang in langs:
        sql_create_skills_table = f"""CREATE TABLE IF NOT EXISTS talents_{lang} (
                                            name_hash text PRIMARY KEY, 
                                            name text NOT NULL, 
                                            max text, 
                                            checks text, 
                                            checks_description text, 
                                            description text, 
                                            table_link text, 
                                            example text, 
                                            spec text);"""
        rules_db.execute(sql_create_skills_table)


if __name__ == '__main__':
    rules_db = sqlite3.connect(DATABASE_PATH)
    create_talents_table(rules_db, (EN, RU))
    rules_db.close()
