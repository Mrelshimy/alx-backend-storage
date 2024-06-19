#!/usr/bin/env python3
""" Redis Operations in python """
import redis
import uuid
from typing import Union


class Cache:
    """ Redis storing class """

    def __init__(self):
        """ Initialization method """
        _redis = redis.Redis()
        _redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method to store data in redis server """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
