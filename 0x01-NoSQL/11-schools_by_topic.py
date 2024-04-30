#!/usr/bin/env python3
""" MongoDB Operations with Python by using pymongo """


def schools_by_topic(mongo_collection, topic):
    """ return list of school having a specific topic """
    documents = mongo_collection.find({"topics": topic})
    return list(documents)
