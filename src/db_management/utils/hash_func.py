import hashlib


def get_name_hash(name):
    obj = hashlib.md5(name.encode('utf-8'))
    return obj.hexdigest()
