#!/usr/bin/env python3
"""Last task module"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """Wait for a random amount of time, n times"""
    return [await wait_random(max_delay) for _ in range(n)]
