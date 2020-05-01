# Transcribing DNA into RNA
# Javier Anleu - 17149


# Opening DNA strand file
dnaF = open("C:/Users/javia/OneDrive - Universidad del Valle de Guatemala/UVG/3er Año/Segundo Semestre 2019/Bioinformática/Rosalind Problems/venv/Transcribing DNA into RNA/rosalind_rna.txt", "r")
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