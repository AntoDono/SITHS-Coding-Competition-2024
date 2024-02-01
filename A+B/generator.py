import sys
import os
import random
sys.path.insert(0, os.path.abspath('..'))

from utils.utils import writeProblem

cases = 10

input_data = []
output_data = []

for i in range(cases):
    a = random.randint(-500000, 500000)
    b = random.randint(-500000, 500000)
    c = a + b

    input_data.append([a, b])
    output_data.append(c)

writeProblem(os.getcwd(), input_data, output_data)
