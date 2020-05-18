# Transcribing DNA into RNA
# Javier Anleu - 17149


# Opening DNA strand file
dnaF = open("Transcribing DNA into RNA/rosalind_rna.txt", "r")
# Reading DNA strand file
if dnaF.mode == 'r':
    dna = dnaF.read()

# Closing file
dnaF.close()

# RNA string
rna = ""

# Going through the strand
for i in dna:
    if i == "T":
        rna = rna + "U"
    elif i != "\n":
        rna = rna + i


# Output
print (rna)
