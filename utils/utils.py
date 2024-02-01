import os 

def writeProblem(wd, input_data, output_data):
    if (len(input_data) != len(output_data)):
        Exception("Input and output data length does not match!")

    try:
        os.mkdir(f"{wd}/input")
        os.mkdir(f"{wd}/output")
    except FileExistsError:
        pass
    
    for index, _ in enumerate(input_data):
        i = input_data[index]
        o = output_data[index]

        with open(f"{wd}/input/{1+index}.txt", 'w') as f:

            line = ""
            for j in i:
                line += str(j) + " "
            line += "\n"
            f.write(line)
            f.close()

        with open(f"{wd}/output/{1+index}.txt", 'w') as f:

            f.write(str(o))
            f.close()

if __name__ == "__main__":
    writeProblem(os.getcwd(),[[1,2,3],[4,5,6]], [1,2])
