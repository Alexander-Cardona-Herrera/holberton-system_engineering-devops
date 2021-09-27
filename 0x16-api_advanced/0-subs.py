#!/usr/bin/python3
"""
    Module to read from an api the number of suscribers.
"""

import json
import requests


def number_of_subscribers(subreddit):
    """ function that recibe the tittle of the subreddit
        an return the total number of subscribers. """

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/94.0.4606.61 Safari/537.36"}
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(
            subreddit), headers=headers)
    res = response.json()

    if response.status_code is not 200:
        print(response.status_code)
        return 0
    else:
        return res.get("data").get("subscribers")
