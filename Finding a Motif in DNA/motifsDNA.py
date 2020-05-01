# Finding a Motif in DNA
# Javier Anleu - 17149

# Opening and reading file
file = open("C:/Users/javia/OneDrive - Universidad del Valle de Guatemala/UVG/3er Año/Segundo Semestre 2019/Bioinformática/Rosalind/Finding a Motif in DNA/rosalind_subs.txt")
data = file.read()

# Obtaining sequence and motif
data = data.split("\n")
dna = data[0]
motif = data[1]

# Motif length
lm = len(motif)

# Output list
loci = []

# Reading sequence
for i in range(0,len(dna)):
    if dna[i]==motif[0]:
        if dna[i:i+lm]==motif:
            loci.append(i+1)

# Output string
output = ""
for i in loci:
    output = output + str(i) + " "

# Output
print (output)
