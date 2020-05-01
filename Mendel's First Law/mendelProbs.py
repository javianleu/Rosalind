# Mendel's First Law
# Javier Anleu - 17149

# Opening and reading the file
file = open("C:/Users/javia/OneDrive - Universidad del Valle de Guatemala/UVG/3er Año/Segundo Semestre 2019/Bioinformática/Rosalind/Mendel's First Law/rosalind_iprb.txt")
props = file.read()

# Obtaining numbers
props = props.split(" ")

# Dominant Homozygotes
k = float(props[0])

# Heterozygotes
m = float(props[1])

# Recessibe Homozygotes
n = float(props[2])

# Total individuals
t = k + m + n

# Calculating the probability of obtaining recessive homozygote progeny
r = (n/t)*((n-1)/(t-1)) + (n/t)*(m/(t-1))*0.5 + (m/t)*(n/(t-1))*0.5 + (m/t)*((m-1)/(t-1))*0.25

# Complement of r
prob = 1 - r

# Output
print (prob)
