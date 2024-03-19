#!/usr/bin/env python3
"""
Cache Module
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a random key."""
        key = str(uuid.uuid4())
        self._redis.set(name=key, value=data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
                                            str, bytes, int, float, None]:
        """Retrieve and optionally convert data from Redis by key."""
        value = self._redis.get(name=key)
        if value is not None and fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string from Redis."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from Redis."""
        return self.get(key, fn=int)
