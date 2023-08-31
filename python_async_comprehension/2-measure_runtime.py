#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Function that measure the total runtime and return it"""
    start_time = time.time()
    await asyncio.gather(async_comprehension())
    end_time = time.time()

    return end_time - start_time
