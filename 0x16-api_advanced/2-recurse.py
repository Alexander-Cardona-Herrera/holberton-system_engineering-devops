#!/usr/bin/python3
"""
    Module to read from an api the list of all hot articles.
"""

import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ function that recibe the tittle of the subreddit
        an return the total number of hot articles. """

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/94.0.4606.61 Safari/537.36"}
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=100".format(
            subreddit), headers=headers)
    res = response.json()

    if response.status_code is not 200:
        return None
    else:
        for post in res.get("data").get("children"):
            hot_list.append((post.get("data").get("title")))
        after = res.get("data").get("after")
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
