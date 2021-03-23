import random # random number generator

ones = 0 # side of die that has one spot
twos = 0 # side of die that has two spots
threes = 0 # side of die that has three spots
fours = 0 # side of die that has four spots
rolls = 1000 # number of trials

for i in range(0, rolls): # i is the trial runs, range is from 0 to how many trials there are
    dice = random.randint(1,4) # randomly selects numbers between 1 and 4
    if dice == 1:
        ones += 1 # if the die number selected is 1, the code will add one to the total times 1 was rolled 
    elif dice == 2:
        twos += 1 # if the die number selected is 2, the code will add one to the total times 2 was rolled 
    elif dice == 3:
        threes += 1 # if the die number selected is 3, the code will add one to the total times 3 was rolled 
    elif dice == 4:
        fours += 1 # if the die number selected is 4, the code will add one to the total times 4 was rolled 

print('1 was rolled', ones, 'times.') # prints out how many times 1 was rolled out of a thousand rolls
print('2 was rolled', twos, 'times.') # prints out how many times 2 was rolled out of a thousand rolls
print('3 was rolled', threes, 'times.') # prints out how many times 3 was rolled out of a thousand rolls
print('4 was rolled', fours, 'times.') # prints out how many times 4 was rolled out of a thousand rolls
print('The total number of rolls was', rolls,'.') # makes sure the program does a thousand trials
