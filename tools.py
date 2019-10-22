import csv
import json
import os
import requests
import sys


def make_directory(file_name):
    '''If it does not exists, make empty directory for given file.'''
    directory = os.path.dirname(file_name)
    if directory:
        os.makedirs(directory, exist_ok=True)


def save_html(url, file_name, force_trasnfer=False):
    '''Content on given url saves into file with given name.'''
    try:
        print('Saving {} ...'.format(url), end='')
        sys.stdout.flush()
        if os.path.isfile(file_name) and not force_trasnfer:
            print('It was saved before.')
            return
        r = requests.get(url)
        r.encoding = 'UTF-8'
    except requests.exceptions.ConnectionError:
        print('Site does not exists')
    else:
        make_directory(file_name)
        with open(file_name, 'w', encoding='UTF-8') as f:
            f.write(r.text)
            print('Saved.')


def file_content(file_name):
    '''Returns string with content of a file with given name.'''
    with open(file_name, encoding='utf-8') as f:
        return f.read()


def write_csv(dictionaries, field_names, file_name):
    '''From list of dictionaries create CSV file with head.'''
    make_directory(file_name)
    with open(file_name, 'w', encoding='utf-8') as csv_f:
        writer = csv.DictWriter(csv_f, fieldnames=field_names)
        writer.writeheader()
        for dictionary in dictionaries:
            writer.writerow(dictionary)


def write_json(object, file_name):
    '''from given object create JSON file.'''
    make_directory(file_name)
    with open(file_name, 'w', encoding='utf-8') as json_f:
        json.dump(object, json_f, indent=4, ensure_ascii=False)
        