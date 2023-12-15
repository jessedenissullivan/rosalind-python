from itertools import permutations
import sys

if __name__=="__main__":
    with open('answers/rosalind_perm.txt', 'w') as f:
        sys.stdout = f
        n = 5
        perms = list(permutations(range(n)))
        print(len(perms))
        for p in perms:
            print("{} {} {}".format(*p))