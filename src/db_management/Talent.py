from src.db_management.utils.hash_func import get_name_hash
from src.db_management.utils.lang_operations import EN, RU, get_template


class Talent:
    def __init__(self):
        self.name_hash = None
        self.name = get_template()
        self.max_picked = get_template()
        self.checks = get_template()
        self.desc = get_template()
        self.checks_desc = get_template()
        self.table_link = get_template()
        self.example = get_template()
        self.spec = get_template()
        self.meta = get_template()
        self.langs_available = {EN: False, RU: False}

    def get_en_fields(self):
        return self.__dict__

    def set_lang_version(self, lang, name, max_picked, desc, checks=None, checks_desc=None,
                         table_link=None, example=None, spec=None, meta=None):
        if self.name_hash is None:
            self.name_hash = get_name_hash(name)
        self.name.update({lang: name})
        self.max_picked[lang] = max_picked
        self.desc[lang] = desc
        self.checks[lang] = checks
        self.checks_desc[lang] = checks_desc
        self.table_link[lang] = table_link
        self.example[lang] = example
        self.spec[lang] = spec
        self.meta[lang] = meta
        self.langs_available[lang] = True

    def add_talent_by_lang(self, rules_db, lang):
        args = (
            self.name_hash,
            self.name[lang],
            self.max_picked[lang],
            self.checks[lang],
            self.checks_desc[lang],
            self.desc[lang],
            self.table_link[lang],
            self.example[lang],
            self.spec[lang]
        )
        num_of_args = '?, ' * (len(args) - 1)
        sql_add_talent = f""" INSERT INTO talents_{lang} VALUES ({num_of_args}?)"""
        rules_db.execute(sql_add_talent, args)
        rules_db.commit()

    def add_talent(self, rules_db):
        for lang in (EN, RU):
            self.add_talent_by_lang(rules_db, lang)
