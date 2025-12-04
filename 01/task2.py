code = 0
curr = 50
total_pins = 100
file_name = 'input.txt'

value_list = list()

with open(file_name, 'r') as file:
    for line in file:
        rotation = line[0]
        digits = line[1:]

        if rotation=='L':
            value_list.append(int('-'+str(digits)))
        else:
            value_list.append(int(digits))

for value in value_list:
    spins = abs(value) // total_pins
    rest = abs(value) % total_pins

    if spins > 0:
         print(f'Fullspins: {spins}')
         code += spins

    if ((curr+value) % total_pins) == 0:
        print('Stopped at 0')
        code +=1
    
    if (curr!=0) and (((value < 0) and (rest > curr)) or ((value > 0) and (rest > (total_pins-curr)))):
        print(f'Pass by zero with spin')
        code +=1

    curr += value
    curr = curr % total_pins
    
print(code)