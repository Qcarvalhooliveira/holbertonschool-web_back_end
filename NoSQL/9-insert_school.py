#!/usr/bin/env python3
"""Function that inserts a new document in a collection based on kwargs"""

from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """Returns the new _id"""
    return mongo_collection.insert_one(kwargs).inserted_id
