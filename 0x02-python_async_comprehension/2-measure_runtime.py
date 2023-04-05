#!/usr/bin/env python3
'''Task 2 module solution.
'''
import asyncio
import time
from importlib import import_module as use


async_comprehension = use('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''This function executes async_comprehension() 4 times and measures the total runtime.
    '''
    start_times = time.time()
    await asyncio.gather(*(async_comprehension() for h in range(4)))
    return time.time() - start_times
