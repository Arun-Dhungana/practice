# Comparing size of array and list and list takes a huge chunk of memory
import numpy as np
import sys
import time
from datetime import datetime

# for size
l = range(100)
print(sys.getsizeof(1) * len(l))
arr = np.arange(100)
print(arr.nbytes)
print(arr.itemsize)

# for processing time
SIZE = 100000
l1 = range(SIZE)
l2 = range(SIZE)
a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# time taken by list
# nowa = datetime.now()
# print(nowa.year, nowa.day, nowa.month, nowa.hour, nowa.minute, nowa.second)
start = time.time()
result = [(x + y) for x, y in zip(l1, l2)]
print(f"list took {(time.time()-start)*1000}ms")

# array
start = time.time()
result = a1 + a2
print(f"array took {(time.time()-start)*1000}ms")
