# A Brief Introduction to Graph Theory
# Javier Anleu Alegria
# May 21, 2020
# The exercise consists in identifying which sequences are connected to one another
# based on the substrings either at the start or end of the sequence. The idea
# would be to form a graph.

# Opening the file
file = open("A Brief Introduction to Graph Theory/rosalind_grph.txt")
data = file.read()

data = data.split("\n")

for i in data:
    if i == "":
        data.remove(i)

names = []
seqs = []

for i in range(len(data)):
    if i%2==0:
        names.append(data[i][1:])
    else:
        seqs.append(data[i])


# print (names)
# print (seqs)

print ("Processing...")

# Import of module to find all common substrings
import py_common_subseq as commonSubs

# Definition of function for array of common substrings
def commonSubstrings(s1, s2):
    sorted = []
    common = commonSubs.find_common_subsequences(s1,s2)
    for i in common:
        if i != "":
            sorted.append(i)
    sorted.sort(key=len)
    sorted.reverse()
    return sorted

    # Construction of Common Substrings Matrix
commonsMatrix = []
for i in range(len(names)):
    seq = []
    for j in range(len(names)):
        if i!=j:
            seq.append(commonSubstrings(seqs[i],seqs[j]))
        else:
            seq.append([-1])
    commonsMatrix.append(seq)


# Corroboration prints
# for i in commonsMatrix:
#     print (i)

# Construction of Adjacency Matrix
adjacencyMatrix = []

for i in range(len(names)):
    s = []
    for j in range(len(names)):
        s.append(0)
    adjacencyMatrix.append(s)

for i in range(len(names)):
    for j in range(len(names)):
        for k in range(len(commonsMatrix[i][j])):
            if i!=j:
                # print (i,j)
                if seqs[i].endswith(commonsMatrix[i][j][k]) and seqs[j].startswith(commonsMatrix[i][j][k]):
                    adjacencyMatrix[i][j] = 1
                    break
                # else:
                #     print ("No match", k)
    #         else:
    #             seq.append(0)
    # adjacencyMatrix.append(seq)

# for i in adjacencyMatrix:
#     print (i)

print ("\nAnswer:\n")
for i in range(len(names)):
    for j in range(len(names)):
        if adjacencyMatrix[i][j]==1:
            print (names[i], names[j])
