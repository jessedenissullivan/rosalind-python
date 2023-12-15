with open("inputs/rosalind_iev.txt") as f:
    distributions = map(int, f.read().split())

base_probabilities = [1, 1, 1, 0.75, 0.5, 0]
print(
    2 * sum(
        [a * b for a, b in zip(distributions, base_probabilities)]
    )
)