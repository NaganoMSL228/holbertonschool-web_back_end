#!/usr/bin/env python3
"""
Module for async functions - wait_random
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds and returns it.

    Args:
        max_delay (int): Maximum delay in seconds (default: 10)

    Returns:
        float: The random delay value
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
