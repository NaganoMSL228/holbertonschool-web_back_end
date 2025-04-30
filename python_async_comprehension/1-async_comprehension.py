#!/usr/bin/env python 3
"""
Async Comprehension module
"""
from typing import List
from .0-async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    return [num async for num in async_generator()]
