EN = 'en'
RU = 'ru'


def get_other_lang(lang):
    if lang is EN:
        return RU
    else:
        return EN


def get_template():
    return {EN: None, RU: None}