#!/usr/bin/env python3
'''Task 1 module solution.
'''
from typing import List
from importlib import import_module

async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This function creates a list of 10 floats generated asynchronously from async_generator().
    """
    finish = [k async for k in async_generator()]
    return finish
