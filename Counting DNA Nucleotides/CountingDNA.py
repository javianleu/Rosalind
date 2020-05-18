# Countint DNA Nucleotides
# Javier Anleu - 17149

# Opening DNA strand file
dnaF= open("Counting DNA Nucleotides/rosalind_dna.txt", "r")

# Reading DNA strand file
if dnaF.mode == 'r':
    dna = dnaF.read()

# Closing file
dnaF.close()

# Printing DNA strand just to make sure we got it
print (dna)

# Nucleotide counters
a = 0
c = 0
g = 0
t = 0

# Going through the strand
for i in dna:
    if i == "A":
        a += 1
    elif i == "C":
        c += 1
    elif i == "G":
        g += 1
    elif i == "T":
        t += 1

# Output
print (str(a) + " " + str(c) + " " + str(g) + " " + str(t))
