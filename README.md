## Python-Decorator

A Decorator is a function that modifies another function with out modifying the actual function.

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

This decorator calculates the amount of time that the add function takes to run, and the result to code would be:

```bash
This took 1.1920928955078125e-06 ms
31
```

Without the decorator, the add function would just simply return 31.

## How to write a Decorator


When writing a decorator there is the outer function, in this case it's performance.

```bash
def performance(func):
```

Then there is an inner function which is a wrapping function where something happens before the execution of the function and something happens after the execution of the function. time_taken is the wrapping function or the inner function in this Decorator.

```bash
def performance(func):
  def time_taken(*args, **kwargs):
    t1 = time()
    result = (func(*args, **kwargs))
    t2 = time()
    print(f'This took {t2-t1} ms')
    return result
  return time_taken
```

In this code we get the time before the the function is executed and the time after the function is executed. t1 is time before the function was executed and t2 was the time after we excuted the function, we subtract t1 from t2 to find how long the functon took to run.

## 2 ways to use a Decorator

The first way:

```bash
@performance
def add(x, y):
  return x+y
```

The second way:

```bash
def add(x, y):
  return x+y

t = performance(add)
print(t(10, 21))
```
