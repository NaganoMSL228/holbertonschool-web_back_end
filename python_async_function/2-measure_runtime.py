#!/usr/bin/env python3
"""
Measure runtime module
"""
import asyncio
import time
from typing import Union

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per coroutine.

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay for each wait_random call

    Returns:
        float: Average execution time per coroutine (total_time / n)
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
