import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

task = asyncio.ensure_future(print_yielded_values())
