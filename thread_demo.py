# coding: utf-8

import time
import random
import asyncio
import gevent

def a():
  for i in range(5):
    print(f"Function a: {i}")
    time.sleep(random.random())

def b():
  for i in range(5):
    print(f"Function b: {i}")
    time.sleep(random.random() * 2)

async def c():
  for i in range(5):
    print(f"Function c: {i}")
    await asyncio.sleep(random.random())
  return "Function c completed"

async def d():
  for i in range(5):
    print(f"Function d: {i}")
    await asyncio.sleep(random.random() * 2)
  return "Function d completed"

def e():
  for i in range(5):
    print(f"gevent ee: {i}")
    gevent.sleep(random.random())
  return "gevent e completed"

def f():
  for i in range(5):
    print(f"gevent f: {i}")
    gevent.sleep(random.random() * 2)
  return "gevent f completed"

async def main():
  result = await asyncio.gather(c(), d())
  print(result)

def gevent_main():
  g_e = gevent.spawn(e)
  g_f = gevent.spawn(f)
  g_list = [g_e, g_f]
  result = gevent.joinall(g_list)
  print(result)

if __name__ == "__main__":
  start_time = time.time()
  a()
  b()
  end_time = time.time()
  print(f"Total time: {end_time - start_time}")
  start_time = time.time()
  asyncio.run(main())
  end_time = time.time()
  print(f"Total time: {end_time - start_time}")
  start_time = time.time()
  gevent_main()
  end_time = time.time()
  print(f"Total time: {end_time - start_time}")