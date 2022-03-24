#!/usr/bin/python3
"""
export data in the CSV format
"""

import requests
import csv
from sys import argv

if __name__ == '__main__':
    try:
        employ_id = int(argv[1])
    except ValueError:
        exit()


    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=employ_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)
    file = '{employ_id}.csv'.format(employ_id=employ_id)

    res = requests.get(user_uri).json()

    user = res.get("username")

    res = requests.get(todo_uri).json()

    with open(file, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for elem in res:
            status = elem.get('completed')

            title = elem.get('title')

            writer.writerow([employ_id, user, status, title])
