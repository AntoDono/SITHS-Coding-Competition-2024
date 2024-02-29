import random
import os
import sys
sys.path.append(os.path.abspath("./"))
from utils.utils import writeProblem

start_case = 7
num_cases = 8

maxn = 100000
maxm = 100000
maxv = 1000

def solve(n, m, s):

    if m > n:
        Exception("n must be larger than m")

    start = False
    elements = 0
    volume = 0
    maxVolume = 0

    for index, v in enumerate(s):

        if (not start):

            elements += 1
            volume += v
            if (elements == m):
                maxVolume = volume
                start = True
        else:
            
            volume -= s[index-m] # get rid of the oldest bottle
            volume += v # adds the current bottle

            maxVolume = max(volume, maxVolume)

            if (index + 1 >= len(s)):
                break

    return maxVolume
        
inputs = []
outputs = []

for i in range(num_cases):
    
    n = random.randint(1, maxn)
    m = random.randint(1, min(n, maxm))

    s = []

    for j in range(n):
        s.append(random.randint(1, maxv))

    ans = solve(n, m, s)

    inputs.append([f"{n}\n{m}\n", (' '.join(str(k) for k in s)) ])

    outputs.append(ans)

    # print(f"n: {n} m: {m} s: {s} ans: {ans}")
    print(f"Done with test case {start_case + i}")

writeProblem(os.getcwd()+"\Wa-ter Those", inputs, outputs, start_case)

