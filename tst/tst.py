import random
import datetime
import time


ct = datetime.datetime.now()

cts = int(time.mktime(ct.timetuple()))

random.seed(cts)
print("Random number with seed 10 : ", random.randint(-10, 10))
print(datetime.datetime.now())

print(cts)
