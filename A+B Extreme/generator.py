import sys
import os
import random
sys.path.append(os.path.abspath("./"))
from utils.utils import writeProblem

cases = 15

input_data = []
output_data = []

for i in range(cases):
    a = random.randint(-1000000000, 1000000000)
    b = random.randint(-1000000000, 1000000000)
    c = a + b

    input_data.append([a, b])
    output_data.append(c)

writeProblem(os.getcwd() + "/A+B", input_data, output_data)
