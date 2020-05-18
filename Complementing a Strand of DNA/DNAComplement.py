# Complementing A Strand of DNA
# Javier Anleu - 17149

# Opening DNA strand file
dnaF = open("Complementing a Strand of DNA/rosalind_revc.txt", "r")
# Reading DNA strand file
if dnaF.mode == 'r':
    dna = dnaF.read()

# Closing file
dnaF.close()

# Function to reverse string
# Obtained from: https://www.journaldev.com/23647/python-reverse-string#python-reverse-string-using-slicing
def reverseSlicing(s):
    return s[::-1]

# DNA complement strand
dnaC = ""

# Iterating DNA strand to generate complement
for i in dna:
    if i == "A":
        dnaC = dnaC + "T"
    elif i == "C":
        dnaC = dnaC + "G"
    elif i == "G":
        dnaC = dnaC + "C"
    elif i == "T":
        dnaC = dnaC + "A"

# Reversing sequence
dnaC = reverseSlicing(dnaC)

# Output
print (dnaC)
