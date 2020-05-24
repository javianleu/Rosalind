# Finding a Shared Motif
# Javier Anleu Alegria
# May 21, 2020
# The idea is to find the longest common substring of a number of sequences.
# Algorithm based on https://github.com/sharno/Rosalind/blob/master/Finding%20a%20Shared%20Motif.py

file = open("Finding a Shared Motif/rosalind_lcsm.txt")

data = file.read()

data = data.split("\n")

seqs = []
current = ""

for i in data:
    if i!="":
        if i[0]==">":
            seqs.append(current)
            current = ""
        else:
            current = current + i

if current != "":
    seqs.append(current)

seqs.remove("")

print(seqs)



#Shortest sequence
shortSeq = seqs[seqs.index(min(seqs, key=len))]


# Cycle over the shortest sequence
motif = ""
for i in range(len(shortSeq)):
    n = 0
    found = True
    while found:
        # Cycling over all sequences to identify the next base to add to motif
        for j in seqs:
            if shortSeq[i:i+n] not in j or n>1000:
                found = False
                break
        if found:
            motif = max(shortSeq[i:i+n], motif, key=len)
        n += 1

print (motif)
