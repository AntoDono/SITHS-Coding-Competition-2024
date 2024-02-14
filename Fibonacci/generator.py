import random
import string

import os
import sys
sys.path.append(os.path.abspath("./"))
from utils.utils import writeProblem

problem_start = 7
MODULO = 1000000000
max_index = 100000000
# max_random_index_range = 10
max_random_index_range = 100000
cases = 1

fib = [0, 1]

for i in range(2, 100000 + 1):
    fib.append(fib[-2] + fib[-1])

tests = []
answers = []

for i in range(cases):

    ans = 0
    current_case = []

    for j in range(random.randint(1, max_index)):
        index = random.randint(0, max_random_index_range - 1)
        current_case.append(str(index + 1))
        ans += fib[index] % MODULO

    tests.append([str(len(current_case)),  "\n" + (' '.join(current_case))])
    ans %= MODULO
    answers.append(ans)
    print("done")


writeProblem(os.getcwd() + "/Fibonacci", tests, answers, problem_start)
