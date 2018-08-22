import time

starttime = time.time()
counter = 0
for i in range(10000000):
    a = 89 ** 13
    counter += 1
print(time.time() - starttime)
