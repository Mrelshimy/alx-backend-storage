#!/usr/bin/env python3
""" Mongodb update collection documents module """
import pymongo


def update_topics(mongo_collection, name, topics):
    """ Mongodb update collection documents fn """

    mongo_collection.update_many({"name": name}, {'$set': {"topics": topics}})
