# Consensus and Profile
# Javier Anleu - 17149

file = open("Consensus and Profile/rosalind_cons.txt")
sequences = file.read()

# Sequence processing

# Removal of \n
sequences = sequences.split("\n")

# Reconstructing string without \n
seq = ""
for i in sequences:
    seq = seq + i
sequences = seq

# Removal of first header to obtain all sequences using split
sequences = sequences[10:len(sequences)]

# Splitting sequences
sequences = sequences.split(">Rosalind_")

# Removing id of sequence
for i in range(len(sequences)):
    # Checking whether the id is single or double digit
    single = False
    try:
        int(sequences[i][2])
    except:
        single = True
    # Extracting pure sequence
    if single == True:
        sequences[i] = sequences[i][4:len(sequences[i])]
    else:
        sequences[i] = sequences[i][4:len(sequences[i])]

# Profile matrix
profile = []
# Obtaining nucleotide frequencies in transposed matrix
for i in range(len(sequences[0])):
    # Nucleotid counters
    a = 0
    c = 0
    g = 0
    t = 0
    for j in range(len(sequences)):
        if sequences[j][i]=="A":
            a += 1
        elif sequences[j][i]=="C":
            c += 1
        elif sequences[j][i]=="G":
            g += 1
        else:
            t += 1
    temp = [a, c, g, t]
    profile.append(temp)

# Obtaining common ancestor strand
sequence = ""
for i in range(len(profile)):
    if profile[i].index(max(profile[i]))==0:
        sequence = sequence + "A"
    elif profile[i].index(max(profile[i]))==1:
        sequence = sequence + "C"
    elif profile[i].index(max(profile[i]))==2:
        sequence = sequence + "G"
    else:
        sequence = sequence + "T"

# Printing matrix for output
matrix = "A: "
for i in range(len(profile)):
    matrix = matrix + str(profile[i][0]) + " "
matrix = matrix + "\nC: "
for i in range(len(profile)):
    matrix = matrix + str(profile[i][1]) + " "
matrix = matrix + "\nG: "
for i in range(len(profile)):
    matrix = matrix + str(profile[i][2]) + " "
matrix = matrix + "\nT: "
for i in range(len(profile)):
    matrix = matrix + str(profile[i][3]) + " "

# Output
print (sequence)
print (matrix)
