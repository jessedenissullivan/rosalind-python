from itertools import permutations
import sys

if __name__=="__main__":
    with open('answers/rosalind_perm.txt', 'w') as f:
        sys.stdout = f
        n = 6
        perms = list(permutations(range(1,n+1)))
        print(len(perms))
        for p in perms:
            print(" ".join(map(str,p)))