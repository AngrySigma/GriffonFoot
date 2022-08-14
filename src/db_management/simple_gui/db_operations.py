import sqlite3
import PySimpleGUI as sg
from src.db_management.utils.lang_operations import EN, RU
from src.db_management.Talent import Talent


def get_talent_field(lang, name, new_size=(25, 1), is_Multiline=False):
    field = None
    if not is_Multiline:
        field = sg.InputText(size=new_size, key=f"{lang}_{name}")
    else:
        field = sg.Multiline(size=new_size, key=f"{lang}_{name}")
    result = [
        sg.Text(f"{name}"),
        field
    ]
    return result


def get_column(lang):
    column = [[sg.Text(f"Input {lang} talent")]]
    fields = Talent().get_en_fields()
    for field in fields:
        if field == 'name_hash':
            continue
        if field in ('desc', 'check_desc', 'example'):
            column.append(get_talent_field(lang, field, (25, 5), True))
            continue
        column.append(get_talent_field(lang, field))
    column.append([sg.Button(f'submit {lang}', enable_events=True)])
    return column


def add_talent_to_db(lang, values, talent):
    talent.set_lang_version(
        lang,
        values[f"{lang}_name"],
        values[f"{lang}_max_picked"],
        values[f"{lang}_desc"],
        values[f"{lang}_checks"],
        values[f"{lang}_checks_desc"],
        values[f"{lang}_table_link"],
        values[f"{lang}_example"],
        values[f"{lang}_spec"],
        values[f"{lang}_meta"]
    )
    with sqlite3.connect(r'../databases/rules.db') as rules_db:
        talent.add_talent_by_lang(rules_db, lang)


def main():
    layout = [
        [sg.Button('add new talent')],
        [sg.Column(get_column(EN), size=(300, 500)),
        sg.VSeperator(),
        sg.Column(get_column(RU), size=(300, 500)),]
    ]

    talent = Talent()

    # Create the window
    window = sg.Window("Demo", layout).Finalize()

    # Create an event loop
    while True:
        event, values = window.read()

        if event == 'add new talent':
            talent = Talent()

        if event == 'submit en':
            if talent.langs_available[EN] is False:
                add_talent_to_db(EN, values, talent)
                en_name = 'en_name'
                print(f'talent {values[en_name]} added to db')
            else:
                sg.Popup(f'{EN} version is already added for this talent')

        if event == 'submit ru':
            if talent.langs_available[RU] is False:
                add_talent_to_db(RU, values, talent)
                ru_name = 'ru_name'
                print(f'talent {values[ru_name]} added to db')
            else:
                sg.Popup(f'{RU} version is already added for this talent')

        if event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == "__main__":
    main()
