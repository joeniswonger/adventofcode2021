# Part 1
with open('day2.txt', 'r') as f:
    ls = [x.strip() for x in f]

horizontal = 0
depth = 0

for item in ls:
    if 'forward' in item:
        horizontal += int(item[-1])
    elif 'down' in item:
        depth += int(item[-1])
    else:
        depth -= int(item[-1])

print(horizontal * depth)

# Part 2

with open('day2.txt', 'r') as f:
    ls = [x.strip() for x in f]

aim = 0
horizontal = 0
depth = 0

for item in ls:
        if 'forward' in item:
            horizontal += int(item[-1])
            if aim == 0:
                pass
            else:
                depth += int(item[-1]) * aim
        elif 'down' in item:
            aim += int(item[-1])
        else:
            aim -= int(item[-1])
            
print(horizontal * depth)
