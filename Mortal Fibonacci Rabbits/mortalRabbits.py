# Mortal Fibonnaci Rabbits
# Javier Anleu Alegria
# May 17th, 2020.
# This exercise intends to calculate the remaining rabbits in a population after
# n months, assuming that the rabbits reach maturity in one month and die after
# m months.

# Opening file
file = open("Mortal Fibonacci Rabbits/rosalind_fibd.txt")
data = file.read()

data = data.split(" ")

# Number of months for simulation
n = int(data[0])

# Rabbit lifespan
m = int(data[1])

print("Number of months for the simulation:",n)
print("Lifespan of rabbits in months:",m)

# Initial list
rabbits = [1,1]

count = 2
# Main cycle
while (count < n):
    # First case, where only the initial rabbits can reproduce
    if (count < m):
        rabbits.append(rabbits[-2] + rabbits[-1])

    # Case for the first death
    elif (count == m or count == m+1):
        rabbits.append((rabbits[-2] + rabbits[-1]) - 1)
        
    # Case for all remaining rabbits
    else:
        rabbits.append((rabbits[-2] + rabbits[-1]) - (rabbits[-(m+1)]))
    count += 1

print ("Total pairs of rabbits:\n",rabbits[-1])
