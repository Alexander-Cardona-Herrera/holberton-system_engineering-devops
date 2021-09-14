#!/usr/bin/python3
"""
    Module to export to csv.
"""

import json
import requests
import sys


if __name__ == "__main__":
    name = requests.get("https://jsonplaceholder.typicode.com/users").json()
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    final_dict = {}
    for user_id in name:
        all_tasks = []
        for tasks in response:
            if user_id.get('id') == tasks.get('userId'):
                all_tasks.append({"username": user_id.get('username'),
                                  "task": tasks.get(
                    'title'), "completed": tasks.get('completed')})
            final_dict[user_id.get("id")] = all_tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(final_dict, f)
