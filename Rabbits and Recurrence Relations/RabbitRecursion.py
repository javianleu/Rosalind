# Rabbits and Recurrence Relations
# Javier Anleu - 17149

# Opening DNA strand file
rabbitF = open("Rabbits and Recurrence Relations/rosalind_fib.txt", "r")
# Reading DNA strand file
if rabbitF.mode == 'r':
    rabbits = rabbitF.read()


# Closing file
rabbitF.close()

# Obtaining n and k values
rabbits = rabbits.split(" ")
n = int(rabbits[0])
k = int(rabbits[1])

# Setting initial parameters for my variables
fn = 0
fn1 = 1
fn2 = 1
f1 = 1
f2 = 1

# Algorithm for rabit reproduction
for i in range(0,n):
    if i <= 1:
        fn = 1
    elif i <= 2:
        fn = 1 + k
        fn1 = k
    else:
        fn = fn2*k + fn1 + fn2
        fn1 = fn2*k
        fn2 = fn - fn1


# Output
print (fn)
