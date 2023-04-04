#!/usr/bin/env python3
'''Task 1 Let's execute multiple coroutines at the same time with async.
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times. This defines a new asynchronous function named wait_n. It takes two arguments, n and max_delay, both integers, and returns a list of floats.
    '''
    delay = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(delay)
