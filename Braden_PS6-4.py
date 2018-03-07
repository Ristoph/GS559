import sys
import math
import random

def rand_walk_dev(steps):
    dist = 0
    loc = [0]
    locabs = [0]
    for step_num in range(steps):
        dist += random.randint(-1,1)
        loc.append(dist)
        locabs.append(int(math.fabs(dist)))
    return max(locabs)

def avg_100walks(steps):
    dev = []
    devsum = 0
    for i in range(100):
        newdev = rand_walk_dev(steps)
        dev.append(newdev)
        devsum += newdev
    avgdev = devsum/100
    return avgdev



step_count = int(sys.argv[1])
print avg_100walks(step_count)

# 10 steps result: 2
# 1000 steps: 31
# 10000 steps: 102