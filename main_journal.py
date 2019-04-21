import main_journal

import os


def load(name):
    # TODO: populate file from list if it exists or an empty list if not
    return []


def save(name, journal_data):

    filename = os.path.abspath(os.path.join('./journal/', name + '.jrl'))
    print(f'...Saving to:  {filename}')
    fout = open(filename, 'w')
    for entry in journal_data:
        fout.write(entry)
    fout.close()


def add_entry(text, journal_data):
    return journal_data.append(text)
