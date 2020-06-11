# Independent Alleles
# Javier Anleu Alegria
# June 11th, 2020
# The purpose of this exercise is to determine the probability that, given a
# number k of generations, we can calculate the probability that at least a
# number x of the offspring will be heterozygous for two traits.


file = open("Independent Alleles/rosalind_lia.txt")
data = file.read()

data = data.split(" ")

k = int(data[0])
x = int(data[1])

# n represents the total number of offspring in a given generation
n = 2**k

# We can model the probability that at least a number x of the offspring will be
# heterozygous for both traits using the binomial distribution. The dichotomous
# experiment would consider a heterozygous offspring as a success, with a
# probability of success of 0.25 (based on the Punnet squares for both traits).

# Probability of success
p = 0.25


# Importing library to calculate probability with the binomial distribution
from scipy.stats import binom

# Since we must calculate the probability that at least x offspring are
# completely heterozygous, we must use the cumulative distribution function for
# x-1 and the complement of that probability will give us the probability we
# seek.
probs = 1 - binom.cdf(k=x-1, n=n, p=p)

print(probs)
