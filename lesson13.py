# Lesson 13 - asyncio

import asyncio
import time

async def job(name, delay):
    print(f'{name}, start')
    await asyncio.sleep(delay)
    print(f'{name} end')
    return name

async def main():
    start = time.time()
    results = await asyncio.gather(job('A', 1), job('B', 1), job ('C', 1))
    print(results)
    elapsed = time.time() - start
    print(f"elapsed: {elapsed:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())