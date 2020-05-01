# Counting Point Mutations
# Javier Anleu - 17149

# Opening file
file = open("C:/Users/javia/OneDrive - Universidad del Valle de Guatemala/UVG/3er Año/Segundo Semestre 2019/Bioinformática/Rosalind/Counting Point Mutations/rosalind_hamm.txt")
sequences = file.read()

# Separating sequences
sequences = sequences.split("\n")

# Point mutation counter
pointMuts = 0

# Going over the sequences
for i in range(len(sequences[0])):
    if sequences[0][i] != sequences[1][i]:
        pointMuts += 1

# Output
print(pointMuts)
