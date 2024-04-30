#!/usr/bin/env python3
""" MongoDB Operations with Python by using pymongo """


def insert_school(mongo_collection, **kwargs):
    """ Insert a new document in a collection that based on kwargs """
    return mongo_collection.insert(kwargs)
