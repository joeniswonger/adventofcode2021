# Part 1
with open('day1.txt','r') as f:
    ls = [int(x) for x in f]

counter = 0

for i in range(len(ls)-1):
    if ls[i] < ls[i+1]:
        counter += 1
        
    else:
        pass

print(counter)

# Part 2
with open('day1.txt','r') as f:
    ls = [int(x) for x in f]

counter = 0

for i in range(len(ls)-1):
    if sum(ls[i:i+3]) < sum(ls[i+1:i+4]):
        counter += 1
        
    else:
        pass

print(counter)
