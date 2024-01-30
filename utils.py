def writeProblem(wd, input_data, output_data):
    if (len(input_data) != len(output_data)):
        Exception("Input and output data length does not match!")
    with open(wd, 'w') as f:
        for index, _ in enumerate(input_data):
            line = ""
            for i in input_data[index]:
                line += str(i) + " "
            line += "\n"
            line += str(output_data[index]) + "\n"
            f.write(line)

def writeAnswer():
    pass

writeProblem('test.txt', [[1,2,3],[4,5,6]], [1,2])