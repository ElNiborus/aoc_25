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
            value_list.append(int('-'+digits))
        else:
            value_list.append(int(digits))
        

for value in value_list:
    curr += value
    if (curr % total_pins) == 0:
        code +=1
