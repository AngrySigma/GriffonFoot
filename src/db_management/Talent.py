from utils.hash_func import get_name_hash


class Talent:
    def __init__(self, lang, name: str, max, checks, desc, checks_desc=None, table_link=None, example=None, spec=None, name_hash=None):
        self.lang = lang
        self.name = name
        self.max = max
        self.checks = checks
        self.desc = desc
        self.checks_desk = checks_desc
        self.table_link = table_link
        self.example = example
        self.spec = spec
        if name_hash is None:
            self.name_hash = get_name_hash(self.name)
        else:
            self.name_hash = name_hash


