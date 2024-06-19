#!/usr/bin/env python3
""" Redis Operations in python """
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """ Redis storing class """

    def __init__(self):
        """ Initialization method """
        self._redis = redis.Redis(host="localhost", port=6379)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method to store data in redis server """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable])\
            -> Union[str, bytes, int, float]:
        """ Return Key value to original format using fn """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """ Function to return int value of value"""
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """ Function to return string value of value"""
        value = self._redis.get(key)
        return int(int(value.decode('utf-8'))
                    if int(value.decode('utf-8')) else 0)
