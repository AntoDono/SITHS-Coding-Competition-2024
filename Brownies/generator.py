import random
import string

import os
import sys
sys.path.append(os.path.abspath("./"))
from utils.utils import writeProblem

def solve(brownies):
    res = []
    for i in brownies:
        if brownies.count(i) > 1:
            continue
        else:
            res.append(i)
    return sum(res)

input_data = []
output_data = []

length = random.randint(1, 1000)

for j in range(15):

    brownies = []
    sb = ""
    for i in range(length):
        w = random.randint(1, 1000)
        brownies.append(w)
        sb += str(w) + " "

    input_data.append([f"{len(brownies)}\n{sb}"])
    output_data.append(solve(brownies=brownies))

writeProblem(os.getcwd() + "/Brownies", input_data, output_data)
    # print(f"Test Case {i}: Input: '{test_case}' | Expected Output: '{expected}'")
