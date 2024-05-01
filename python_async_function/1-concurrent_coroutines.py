#!/usr/bin/env python3
"""Concurrent coroutines in Python"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


def wait_n(n: int, max_delay: int) -> List[float]:
    """Wait for a random amount of time, n times"""
    return [asyncio.run(wait_random(max_delay)) for _ in range(n)]
