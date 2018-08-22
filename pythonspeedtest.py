import time
from math import sqrt
import random

starttime = time.time()
counter = 0
for i in range(10000000):
    a = sqrt(random.random())
    counter += 1
print(time.time() - starttime)
