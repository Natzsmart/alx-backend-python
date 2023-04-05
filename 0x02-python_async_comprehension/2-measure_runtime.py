#!/usr/bin/env python3

'''
This is the solution to Task 2.
'''

import asyncio
import time
from importlib import import_module as put

async_comprehension = put('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    This function executes async_comprehension() 4 times
    and measures the total runtime.
    '''
    start = time.time()
    await asyncio.gather(*(async_comprehension() for h in range(4)))
    return time.time() - start

