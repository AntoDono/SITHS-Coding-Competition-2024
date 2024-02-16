import random
import string

import os
import sys
sys.path.append(os.path.abspath("./"))
from utils.utils import writeProblem

problem_start = 9
MODULO = 1000000000
max_index = 100000
# max_random_index_range = 10
max_random_index_range = 90
cases = 6

fib = [0, 1]

for i in range(2, 90):
    fib.append(fib[-2] + fib[-1])

tests = []
answers = []

for i in range(cases):

    ans = 0
    current_case = []

    amt_nums = random.randint(1, max_index)
    print(amt_nums)

    for j in range(amt_nums):
        index = random.randint(0, max_random_index_range - 1)
        current_case.append(str(index + 1))
        ans += fib[index] % MODULO

    tests.append([str(len(current_case)),  "\n" + (' '.join(current_case))])
    ans %= MODULO
    answers.append(ans)
    print("done")


writeProblem(os.getcwd() + "/Fibonacci On Steroids", tests, answers, problem_start)
