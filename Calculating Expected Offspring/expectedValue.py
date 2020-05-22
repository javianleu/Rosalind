# Calculating Expected Offspring
# Javier Anleu Alegria
# May 21, 2020
# The idea is to calculate the expected offspring that will display the dominant
# phenotype of a trait under the assumptions of Mendelian genetics and that
# each couple will produce 2 offspring. There are 6 combinations for the parents'
# genotypes.

file = open("Calculating Expected Offspring/rosalind_iev.txt")

data = file.read()

data = data.split(" ")

couples = []

for i in data:
    couples.append(int(i))

# List containing probabilities associated to each parent combination
# - AA-AA -> P (D) = 1
# - AA-Aa -> P (D) = 1
# - AA-aa -> P (D) = 1
# - Aa-Aa -> P (D) = 0.75
# - Aa-aa -> P (D) = 0.5
# - aa-aa -> P (D) = 0

probabilities = [1,1,1,0.75,0.5,0]

# Since these are two successive independent events, then to calculate the
# expected value of offspring displaying the dominant phenotype we must add
# the expected value of a single child for all couples with itself, such that
#
# E(dominant offspring) = E(X + X) = E(2X) = 2E(X)*
#
# *The expected value can be calculated in this way because of the theorem for
# linear transformations of expected values.

ev = 0
for i in range(len(couples)):
    ev = ev + couples[i]*probabilities[i]

ev = 2*ev

print (ev)
