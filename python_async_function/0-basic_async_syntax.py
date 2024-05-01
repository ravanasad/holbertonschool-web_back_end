#!/usr/bin/env python3
"""Basic async syntax in Python"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    """Wait for a random amount of time"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
