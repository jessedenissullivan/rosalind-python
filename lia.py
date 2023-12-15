from sys import argv
from math import comb
from pprint import pprint
from decimal import Decimal, getcontext
getcontext().prec = 50
P_hetero = Decimal(0.25)
P_homo = Decimal(0.75)
def lia(gens, individuals):
    pop = 2 ** gens
    def P(i):
        return Decimal(comb(pop, i) * (P_hetero ** i) * (P_homo ** (pop - i)))
    return sum(P(i) for i in range(individuals, pop + 1))
if __name__=="__main__":
    with open(argv[1]) as f:
        k, N = tuple(map(int, f.read().split()))
        print(round(lia(k, N), 3))