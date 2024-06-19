#!/usr/bin/env python3
""" Redis Operations in python """
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count calls method """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function to increase key value
        each time method is called"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Call history method """
    key = method.__qualname__
    key1 = key + ":inputs"
    key2 = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper method to store input and
        output of the called method """
        self._redis.rpush(key1, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(key2, output)
        return output
    return wrapper


class Cache:
    """ Redis storing class """

    def __init__(self):
        """ Initialization method """
        self._redis = redis.Redis(host="localhost", port=6379)
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method to store data in redis server """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """ Return Key value to original format using fn """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """ Function to return int value of value"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Function to return int value of value"""
        value = self._redis.get(key)
        return int(value.decode("utf-8")) if int(value.decode("utf-8")) else 0
