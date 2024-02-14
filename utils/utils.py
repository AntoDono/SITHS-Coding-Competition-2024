import os 
import shutil  
import time

def writeProblem(wd, input_data, output_data, start_index=0):
    if (len(input_data) != len(output_data)):
        Exception("Input and output data length does not match!")

    try:
        os.mkdir(f"{wd}/input")
        os.mkdir(f"{wd}/output")
        os.mkdir(f"{wd}/problem")
    except FileExistsError:
        pass
    
    for index, _ in enumerate(input_data):
        i = input_data[index]
        o = output_data[index]

        with open(f"{wd}/input/input{index+start_index}.txt", 'w') as f:

            line = ""
            for j in i:
                line += str(j) + " "
            line = line[:-1]
            line += "\n"
            f.write(line)
            f.close()

        with open(f"{wd}/output/output{index+start_index}.txt", 'w') as f:

            f.write(str(o))
            f.close()

    shutil.move(f"{wd}/input", f"{wd}/problem")
    shutil.move(f"{wd}/output", f"{wd}/problem")   
    # shutil.make_archive(f"{wd}/problem", "zip", wd)
    

if __name__ == "__main__":
    writeProblem(os.getcwd(),[[1,2,3],[4,5,6]], [1,2])
