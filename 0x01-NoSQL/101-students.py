#!/usr/bin/env python3
""" MongoDB Operations with Python by using pymongo """


def top_students(mongo_collection):
    # sourcery skip: inline-immediately-returned-variable
    """ Returns all students that sorted by average score """
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
