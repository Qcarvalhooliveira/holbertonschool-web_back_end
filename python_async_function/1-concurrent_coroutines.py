#!/usr/bin/env python3
"""Function tht execute multiple coroutines at the same time"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that call wait_random n times"""
    coroutines = [wait_random(max_delay) for time in range(n)]
    delays = []

    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        delays.append(delay)
    return delays
