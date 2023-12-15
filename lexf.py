import itertools
if __name__=="__main__":
    input = "inputs/rosalind_lexf.txt"
    with open(input) as f:
        alphabet = f.readline().split()
        n = int(f.readline())
    print(
        "\n".join(
            [
                "".join(items)
                for items in 
                sorted(
                    itertools.product(alphabet, repeat=n)
                )
            ]
        )
    )