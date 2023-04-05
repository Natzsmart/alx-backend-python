#!/usr/bin/env python3

'''
This is the solution to Task 1 module.
'''

from typing import List
from importlib import import_module

async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    This function creates a list of 10 floats generated asynchronously from async_generator().
    '''
    return [k async for k in async_generator()]

