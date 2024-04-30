#!/usr/bin/env python3
""" MongoDB Operation with Python by using pymongo """


def list_all(mongo_collection):
    """ List all the documents in Python """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
