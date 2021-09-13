#!/usr/bin/python3
"""
    Module to export to csv.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(sys.argv[1])).json()
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(sys.argv[1])).json()

    first_name = name.get('username')
    user_id = name.get('id')
    total = len(response)
    all_tasks = []
    for tasks in response:
        all_tasks.append([str(user_id), str(first_name),
                         str(tasks.get('completed')), str(tasks.get('title'))])

    with open('{}.csv'.format(sys.argv[1]), 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        writer.writerows(all_tasks)
