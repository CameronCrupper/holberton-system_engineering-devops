#!/usr/bin/python3
"""
export data in the JSON format
"""

import requests
from json import dumps
from sys import argv

if __name__ == '__main__':
    try:
        employ_id = int(argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=employ_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)
    file = '{employ_id}.json'.format(employ_id=employ_id)

    user_res = requests.get(user_uri).json()

    todo_res = requests.get(todo_uri).json()

    task = list()

    for elem in todo_res:
        data = {
            'task': elem.get('title'),
            'completed': elem.get('completed'),
            'username': user_res.get('username')
        }

        task.append(data)

    with open(file, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps({employ_id: task}))
