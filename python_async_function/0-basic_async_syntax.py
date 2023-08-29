#!/usr/bin/env python3
"""Coroutine that takes in an integer argument"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Function that returns the delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
