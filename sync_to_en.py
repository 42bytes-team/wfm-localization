import copy
import json
import os
from collections import OrderedDict
from pprint import pformat, pprint


def sync_to_en():
    """
    Synchronizing the structure of the locale files with `en` locale file.
    Missing keys from `en`-locale will be added to all the available locales.
    Order of keys will be maintained
    :return:
    """
    locales = {
        'en': None,
        'to_sync': []
    }
    for _root, dirs, files in os.walk('locales'):
        for locale_file in files:
            if '.json' not in locale_file:
                continue
            name, ext = locale_file.split('.')
            if name == 'en':
                locales['en'] = locale_file
            else:
                locales['to_sync'].append(locale_file)
    pprint(locales)
    if locales['en'] is None:
        print('En file was not found')
        return

    # Synchronize
    # Load en.json file
    with open(os.path.join('locales', locales['en'])) as _file:
        en_locale = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(_file.read())

    # Format en.json file
    with open(os.path.join('locales', locales['en']), 'w', encoding="utf-8") as _file:
        en_locale_dump = json.JSONEncoder(indent=2, ensure_ascii=False).encode(en_locale)
        _file.write(en_locale_dump)

    for locale_file in locales['to_sync']:
        updated_locale_data = copy.deepcopy(en_locale)
        unknown_keys = []
        with open(os.path.join('locales', locale_file)) as _file:
            for key, value in json.JSONDecoder(object_pairs_hook=OrderedDict).decode(_file.read()).items():
                if key in en_locale:
                    updated_locale_data[key] = value
                else:
                    unknown_keys.append(key)
            if len(unknown_keys) > 0:
                print(f'Locale: {locale_file}, unknown keys detected:\n{pformat(unknown_keys)}')

        locale_dump = json.JSONEncoder(indent=2, ensure_ascii=False).encode(updated_locale_data)
        with open(os.path.join('locales', locale_file), 'w', encoding="utf-8") as _file:
            _file.write(locale_dump)


if __name__ == '__main__':
    sync_to_en()
