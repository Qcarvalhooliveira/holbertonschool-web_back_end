#!/usr/bin/env python3
"""Function that lists all documents in a collection"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """Return an empty list if no document in the collection"""
    if mongo_collection:
        return list(mongo_collection.find({}))
    else:
        return []
