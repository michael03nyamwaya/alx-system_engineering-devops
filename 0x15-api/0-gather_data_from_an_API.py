#!/usr/bin/python3
"""returns information about TODO list progress of a given employee"""
import requests
from sys import argv

if __name__ == "__main__":
    """Identifies a user to display completed task info"""
    endpoint = 'https://jsonplaceholder.typicode.com/'
    userId = argv[1]
    user = requests.get(endpoint + 'users/{}'.format(userId)).json()
    userTodos = requests.get(endpoint + 'users/{}/todos'.format(userId)).json()
    completed = []

    for task in userTodos:
        if task.get('completed'):
            completed.append(task.get('title'))
    print('Employee {} is done with tasks({}/{}):'
          .format(user.get('name'), len(completed), len(userTodos)))
    for task in completed:
        print('\t', task)
