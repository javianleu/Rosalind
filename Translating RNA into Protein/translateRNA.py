# Translating RNA into Protein
# Javier Anleu - 17149

# Open and read file
file = open("C:/Users/javia/OneDrive - Universidad del Valle de Guatemala/UVG/3er Año/Segundo Semestre 2019/Bioinformática/Rosalind/Translating RNA into Protein/rosalind_prot.txt")
mRNA = file.read()

# Length of RNA sequence
l = len(mRNA)

# String for the protein sequence
pep = ""

print ("Translating...")
# For loop for translation.
# It goes over the RNA sequence in steps of 3 (last parameter of range)
for i in range(0,l,3):
    if mRNA[i]=="U":

        if mRNA[i+1]=="U":
            if mRNA[i+2]=="U" or mRNA[i+2]=="C":
                pep = pep + "F"
            else:
                pep = pep + "L"

        elif mRNA[i+1]=="C":
            pep = pep + "S"

        elif mRNA[i+1]=="A":
            if mRNA[i+2]=="U" or mRNA[i+2]=="C":
                pep = pep + "Y"
            else:
                break

        elif mRNA[i+1]=="G":
            if mRNA[i+2]=="U" or mRNA[i+2]=="C":
                pep = pep + "C"
            elif mRNA[i+2]=="G":
                pep = pep + "W"
            else:
                break

    elif mRNA[i]=="C":

        if mRNA[i+1]=="U":
            pep = pep + "L"

        elif mRNA[i+1]=="C":
            pep = pep + "P"

        elif mRNA[i+1]=="A":
            if mRNA[i+2]=="U" or mRNA[i+2]=="C":
                pep = pep + "H"
            else:
                pep = pep + "Q"

        elif mRNA[i+1]=="G":
            pep = pep + "R"

    elif mRNA[i]=="A":

        if mRNA[i+1]=="U":
            if mRNA[i+2]=="G":
                pep = pep +"M"
            else:
                pep = pep + "I"

        elif mRNA[i+1]=="C":
            pep = pep + "T"

        elif mRNA[i+1]=="A":
            if mRNA[i+2]=="U" or mRNA[i+2]=="C":
                pep = pep + "N"
            else:
                pep = pep + "K"

        elif mRNA[i+1]=="G":
            if mRNA[i+2]=="U" or mRNA[i+2]=="C":
                pep = pep + "S"
            else:
                pep = pep + "R"

    else:

        if mRNA[i+1]=="U":
            pep = pep + "V"

        elif mRNA[i+1]=="C":
            pep = pep + "A"

        elif mRNA[i+1]=="A":
            if mRNA[i+2]=="U" or mRNA[i+2]=="C":
                pep = pep + "D"
            else:
                pep = pep + "E"

        else:
            pep = pep + "G"


# Output
print("Completed.")
print (pep)
print(len(pep))
