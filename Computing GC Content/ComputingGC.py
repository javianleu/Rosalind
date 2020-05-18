# Computing GC Content
# Javier Anleu - 17149

# Opening and reading of file (to string)
file = open("Computing GC Content/rosalind_gc.txt")
sequences = file.read()

# Removing linespaces
sequences = sequences.split("\n")

seqs = ""
for i in sequences:
    seqs = seqs + i

# Separating the sequences
seqs = seqs.split(">Rosalind_")

# Removing blank strings from the sequence list
for i in seqs:
    if i == "":
        seqs.remove(i)


# Computing GC Content of every sequence
gcContent = []
count = 0
for i in seqs:
    count = 0
    for j in range(4, len(i)):
        if i[j] == "C" or i[j] == "G":
            count += 1
    gc = (count/(len(i)-4))*100
    gcContent.append(gc)

# Determining sequence with highest GC Content
output ="Rosalind_" + str(seqs[gcContent.index(max(gcContent))][0:4])

# Output
print(output)
print(max(gcContent))
