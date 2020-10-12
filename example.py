from time import time

def performance(func):
  def time_taken(*args, **kwargs):
    t1 = time()
    result = func(*args, **kwargs)
    t2 = time()
    print(f'This took {t2-t1} ms')
    return result
  return time_taken


@performance
def add(x, y):
  return x+y


print(add(10, 21))
