def mortal_fib(m, n):
    initial = tuple(0 for i in range(m))
    def fib_triplet(g):
        if g == initial:
            return (1,) + tuple(initial[:-1])
        else:
            return (sum(g[1:]),) + tuple(g[:-1])

    step = initial
    print(f"Initial generation: {step}")
    for i in range(n):
        step = fib_triplet(step)
        print(f"{i}: {step} = {sum(step)}")
    return sum(step)

print(f"The number of bunnies left is {mortal_fib(17, 96)}")