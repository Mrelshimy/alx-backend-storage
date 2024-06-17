#!/usr/bin/env python3
""" Mongodb list all collection docs """
import pymongo


def list_all(mongo_collection):
    """ List all docs function """

    docs = []
    for doc in mongo_collection.find():
        docs.append(doc)
    return docs
