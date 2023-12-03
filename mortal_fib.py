months = 6
lifespan = 3

pre_pop = [0]
post_pop = []
for m in range(months):
    print(f"{m+1}: (0: {pre_pop.count(0)}) - (1: {pre_pop.count(1)}) - (2: {pre_pop.count(2)}) - (total: {len(pre_pop)})")
    for (i, p) in enumerate(pre_pop):
        if p > 0: post_pop += [0]
        post_pop += [pre_pop[i]+1]
    post_pop = list(filter(lambda p: p < lifespan, post_pop))
    # print(f"{m}: ({len(pre_pop)}: {pre_pop})\n-> ({len(post_pop)}: {post_pop})")
    print('-'*80)
    pre_pop = post_pop
    post_pop = []

table = {}
def fib(n):
    if n in table: return table[n]
    if n < 0: ret = 0
    else:
        match n:
            case 0: ret = 1
            case 1: ret = 1
            case _: ret = 
    table[n] = ret
    return ret

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))