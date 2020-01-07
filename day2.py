 
def int_code(code):
    instruction_pointer = 0

    while True:
        cmd = code[instruction_pointer:instruction_pointer+4]

        if cmd[0] == 1:
            code[cmd[3]] = code[cmd[1]] + code[cmd[2]]
        elif cmd[0] == 2:
            code[cmd[3]] = code[cmd[1]] * code[cmd[2]]
        elif cmd[0] == 99:
            break
        else:
            print("Error!")
            break
        
        instruction_pointer += 4

    return code
    


for noun in range(0,99):
    for verb in range(0,99):
        inp = open('inp_day2', "r")

        line = str(inp.readline())
        inpt = line.split(',')

        inpt = list(map(int, inpt))

        inpt[1] = noun
        inpt[2] = verb

        inpt = int_code(inpt) 

        if inpt[0] == 19690720:
            print("Found it")
            print(inpt)

        inp.close()
