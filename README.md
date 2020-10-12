# Python-Decorators

Decorators are functions that modify another function or give it extra features.

example:

```bash
from time import time

def performance(func):
  def time_taken(*args, **kwargs):
    t1 = time()
    result = (func(*args, **kwargs))
    t2 = time()
    print(f'This took {t2-t1} ms')
    return result
  return time_taken


@performance
def add(x, y):
  return x+y


print(add(10, 21))
```

This decorator calculates the amount of time that the add function to run and the result to this could would be:

```bash
This took 1.1920928955078125e-06 ms
31
```
