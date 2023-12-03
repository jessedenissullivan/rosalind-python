from pprint import pprint
with open("answer.txt") as f:
    my_answers = set(map(lambda x: tuple(x.split()), f.readlines()))

with open("answer.correct.txt") as f:
    his_answers = set(map(lambda x: tuple(x.split()), f.readlines()))

print("Incorrectly generated answers:")
pprint(my_answers - his_answers)

print("\nIncorrectly ommitted answers:")
pprint(his_answers - my_answers)