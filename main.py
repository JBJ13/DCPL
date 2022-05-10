file = open(input("Data line: "))
data = file.readlines()
limes = int(data[0].split("=")[1].strip())
file.close()

data_line = []
temp = ""
for i in data[1:]:
    temp += str(i.replace("\n", "").replace("\t", "").replace(" ", ""))
for i in temp.split(","):
    data_line.append(int(i))
for i in range(limes - len(data_line)):
    data_line.append(0)

markers = [0, 0, 0, 0]  # A, B, C, D

file = open(input("File: "))
data = file.readlines()
file.close()
program = ""
for i in data:
    program += i.replace("\n", "").replace("\t", "").replace(" ", "")
temp = []
for i in str(program).split(";"):
    temp.append(i)
program = temp[:-1]
del temp, file, data

# markers move:
ins = -1
string = ""
while ins < len(program) - 1:
    ins += 1

    if program[ins][0] == "D" or program[ins][0] == "d":
        if program[ins][1] != ":":
            print("Unknown operation: ", program[ins][1], " in: ", ins, " command")
            break
        if len(program[ins]) <= 2:
            continue
        for i in program[ins][2:]:
            if i == ">":
                markers[3] += 1
            elif i == "<":
                markers[3] -= 1
            elif i == "^":
                markers[3] = data_line[markers[3]]
            else:
                print("Unknown operation: ", i, " in: ", ins, " command")
                break
        if limes <= markers[3] and markers[0] >= 0:
            print("Marker D out of range in ins: ", ins)
            break

    elif program[ins][0] == "C" or program[ins][0] == "c":
        if program[ins][1] != ":":
            print("Unknown operation: ", program[ins][1], " in: ", ins, " command")
            break
        if len(program[ins]) <= 2:
            continue
        for i in program[ins][2:]:
            if i == ">":
                markers[2] += 1
            elif i == "<":
                markers[2] -= 1
            elif i == "^":
                markers[2] = data_line[markers[2]]
            else:
                print("Unknown operation: ", i, " in: ", ins, " command")
                break
        if limes <= markers[2] and markers[0] >= 0:
            print("Marker C out of range in ins: ", ins)
            break

    elif program[ins][0] == "B" or program[ins][0] == "b":
        if program[ins][1] != ":":
            print("Unknown operation: ", program[ins][1], " in: ", ins, " command")
            break
        if len(program[ins]) <= 2:
            continue
        for i in program[ins][2:]:
            if i == ">":
                markers[1] += 1
            elif i == "<":
                markers[1] -= 1
            elif i == "^":
                markers[1] = data_line[markers[3]]
            else:
                print("Unknown operation: ", i, " in: ", ins, " command")
                break
        if limes <= markers[1] and markers[0] >= 0:
            print("Marker B out of range in ins: ", ins)
            break

    elif program[ins][0] == "A" or program[ins][0] == "a":
        if program[ins][1] != ":":
            print("Unknown operation: ", program[ins][1], " in: ", ins, " command")
            break
        if len(program[ins]) > 2:
            for i in program[ins][2:]:
                if i == ">":
                    markers[0] += 1
                elif i == "<":
                    markers[0] -= 1
                elif i == "^":
                    markers[0] = data_line[markers[3]]
                else:
                    print("Unknown operation: ", i, " in: ", ins, " command")
                    break
            if limes <= markers[0] and markers[0] >= 0:
                print("Marker A out of range in ins: ", ins)
                break

        # opcodes
        opcode = data_line[markers[0]]
        if opcode == 0:
            data_line[markers[1]] += 1

        elif opcode == 1:
            data_line[markers[1]] -= 1

        elif opcode == 2:
            data_line[markers[1]] = 0

        elif opcode == 3:
            data_line[markers[1]] = data_line[markers[2]] + data_line[markers[3]]

        elif opcode == 4:
            data_line[markers[1]] = data_line[markers[2]] - data_line[markers[3]]

        elif opcode == 5:
            data_line[markers[1]] = data_line[markers[2]] * data_line[markers[3]]

        elif opcode == 6:
            data_line[markers[1]] = data_line[markers[2]] // data_line[markers[3]]

        elif opcode == 7:
            data_line[markers[1]] = data_line[markers[2]] % data_line[markers[3]]

        elif opcode == 8:
            data_line[markers[1]] = data_line[markers[2]] ** data_line[markers[3]]

        elif opcode == 9:
            if data_line[markers[1]] < 0: ins = data_line[markers[2]] - 1

        elif opcode == 10:
            if data_line[markers[1]] <= 0: ins = data_line[markers[2]] - 1

        elif opcode == 11:
            if data_line[markers[1]] == 0: ins = data_line[markers[2]] - 1

        elif opcode == 12:
            if data_line[markers[1]] > 0: ins = data_line[markers[2]] - 1

        elif opcode == 13:
            if data_line[markers[1]] >= 0: ins = data_line[markers[2]] - 1

        elif opcode == 14:
            if data_line[markers[1]] < data_line[markers[2]]: ins = data_line[markers[3]] - 1

        elif opcode == 15:
            if data_line[markers[1]] <= data_line[markers[2]]: ins = data_line[markers[3]] - 1

        elif opcode == 16:
            if data_line[markers[1]] == data_line[markers[2]]: ins = data_line[markers[3]] - 1

        elif opcode == 17:
            if data_line[markers[1]] > data_line[markers[2]]: ins = data_line[markers[3]] - 1

        elif opcode == 18:
            if data_line[markers[1]] >= data_line[markers[2]]: ins = data_line[markers[3]] - 1

        elif opcode == 19:
            markers[0] = markers[1]

        elif opcode == 20:
            markers[1] = markers[2]

        elif opcode == 21:
            markers[2] = markers[1]

        elif opcode == 22:
            markers[3] = markers[1]

        elif opcode == 23:
            print(chr(data_line[markers[1]]), end="")

        elif opcode == 24:
            print(data_line[markers[1]], end="")

        elif opcode == 25:
            string = input()

        elif opcode == 26:
            if len(string) > 0:
                data_line[markers[1]] = ord(string[0])
                string = string[1:]
            else:
                data_line[markers[1]] = 0

        elif opcode == 27:
            data_line[markers[1]] = int(input(), end="")

        elif opcode == 28:
            ins = data_line[markers[1]] - 1

        elif opcode == 29:
            data_line[markers[0]] = data_line[markers[1]]

        elif opcode == 30:
            data_line[markers[1]] = data_line[markers[2]]

        elif opcode == 31:
            data_line[markers[2]] = data_line[markers[1]]

        elif opcode == 32:
            data_line[markers[3]] = data_line[markers[1]]

        else:
            pass

    else:
        print("Unknown marker: ", program[ins][0], " in: ", ins, " command")
        break
