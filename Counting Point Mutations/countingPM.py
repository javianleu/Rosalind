# Counting Point Mutations
# Javier Anleu - 17149

# Opening file
file = open("Counting Point Mutations/rosalind_hamm.txt")
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
