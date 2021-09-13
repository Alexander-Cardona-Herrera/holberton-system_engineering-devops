#!/usr/bin/python3
"""
    Module to export to csv.
"""

import json
import requests
import sys


if __name__ == "__main__":
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(sys.argv[1])).json()
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(sys.argv[1])).json()

    all_tasks = []
    for tasks in response:
        all_tasks.append({"task": tasks.get('title'), "completed": tasks.get(
            'completed'), "username": name.get('username')})
    user_dict = {"{}".format(sys.argv[1]): all_tasks}
    print(user_dict)
    with open('{}.json'.format(sys.argv[1]), 'w') as f:
        json.dump(user_dict, f)
