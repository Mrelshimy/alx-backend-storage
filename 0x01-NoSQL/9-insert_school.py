#!/usr/bin/env python3
""" Mongodb insert to collection """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ insert all docs to coll function """

    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
