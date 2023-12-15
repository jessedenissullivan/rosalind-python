from itertools import product
import numpy as np
maximum = 1
def longest_increasing_subsequence(n,pi):
    global maximum
    if n == 1: return 1
    maxEndingsHere = 1  
    for i in range(1,n):
        res = longest_increasing_subsequence(i,pi)
        if pi[i-1] < pi[n-1] and res + 1 > maxEndingsHere:
            maxEndingsHere = res + 1
    maximum = max(maximum, maxEndingsHere)
    return maxEndingsHere

if __name__=="__main__":
    input = "inputs/rosalind_lgif.txt"
    with open(input) as f:
        n = int(f.readline())
        pi = tuple(int(x) for x in f.readline().split())
    print(*longest_increasing_subsequence(n,pi))
