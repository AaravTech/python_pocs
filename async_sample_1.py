import random
from time import sleep
import asyncio


def task(pid):
    """Synchronous non-deterministic task."""
    sleep(random.randint(0, 2))
    print('Task %s done' % pid)


async def task_coro(pid):
    """Coroutine non-deterministic task"""
    wait_time = random.randint(0, 12)
    print("Waiting %d sec" % wait_time)
    await asyncio.sleep(wait_time)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


async def asynchronous():
    tasks = [task_coro(i) for i in range(1, 10)]
    await asyncio.gather(*tasks)


print('Synchronous:')
#synchronous()

print('Asynchronous:')
asyncio.run(asynchronous())
