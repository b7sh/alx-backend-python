#!/usr/bin/env python3
'''
Write a coroutine called async_generator
that takes no arguments.
The coroutine will loop 10 times,
each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
Use the random module.
'''
from random import uniform
from typing import Generator
from asyncio import sleep


async def async_generator() -> Generator[float, None, None]:
    'yield a random number between 0 and 10'
    for number in range(10):
        yield uniform(0, 10)
