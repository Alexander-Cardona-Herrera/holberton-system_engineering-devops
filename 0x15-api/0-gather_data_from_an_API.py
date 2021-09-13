#!/usr/bin/python3
"""
    Module for the intregration of REST APIs.
"""

import requests
import sys


if __name__ == "__main__":
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(sys.argv[1])).json()
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(sys.argv[1])).json()

    first_name = name.get('name')
    total = len(response)
    count = 0
    for tasks in response:
        completed = list(tasks.values()).count(True)
        count = count + completed
    print("Employee {} is done with tasks({}/{}): "
          .format(first_name, count, total))
    for tasks in response:
        completed = list(tasks.values()).count(True)
        if (completed == 1):
            print("\t {}".format(tasks.get('title')))
