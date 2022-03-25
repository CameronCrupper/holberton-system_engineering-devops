#!/usr/bin/python3
"""
export data in the JSON format continuing task 0
"""
from json import dumps
import requests
from sys import argv

def gather_tasks(response, employee):
    """
    Gather tasks for employee
    """
    e_task = list()

    for task in response:
        if task.get('userId') == employee.get('id'):
            t_data = {
                'username': employee.get('username'),
                'task': task.get('title'),
                'completed': task.get('completed'),
            }

            e_task.append(t_data)

    return e_task


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users'.format(api=api_url)
    todo_uri = '{api}/todos'.format(api=api_url)
    file = 'todo_all_employees.json'

    user_res = requests.get(user_uri).json()
    todo_res = requests.get(todo_uri).json()
    u_task = dict()

    for user in user_res:
        u_id = user.get('id')

        user_task = gather_tasks(todo_res, {
            'id': u_id,
            'username': user.get('username')
        })

        u_task[u_id] = user_task

    with open(file, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps(u_task))
