from collections import defaultdict
def fib(n, k):
    match n:
        case 0: 
            return 0
        case 1: 
            return 1
        case n: 
            return fib(n-1, k) + (k * fib(n-2, k)) 
print(fib(31,4))