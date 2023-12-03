with open('inputs/rosalind_mend.txt') as f:
    vals = f.read().split()
    homoD = int(vals[0])
    heter = int(vals[1])
    homoR = int(vals[2])
    pop = homoD + heter + homoR
    pop2 = pop - 1 
    popA = pop * 2
    popD = 2 * homoD + heter
    popR = 2 * homoR + heter



print(
        # dominant p1
        (homoD/pop)*((homoD-1)/pop2)*(4/4) +
        (homoD/pop)*(heter/pop2)*(4/4) +
        (homoD/pop)*(homoR/pop2)*(4/4) +

        # heter p1
        (heter/pop)*(homoD/pop2)*(4/4) +
        (heter/pop)*((heter-1)/pop2)*(3/4) +
        (heter/pop)*(homoR/pop2)*(2/4) + 

        # recessive p1
        (homoR/pop)*(homoD/pop2)*(4/4) +
        (homoR/pop)*(heter/pop2)*(2/4) +
        (homoR/pop)*((homoR-1)/pop2)*(0/4) 
)