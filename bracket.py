
# create a list of all permutations from 1 to 2^n-1
def permutations(n):
    if n == 1:
        return [[1]]
    else:
        perm = []
        for p in permutations(n-1):
            for i in range(n):
                perm.append(p[:i] + [n] + p[i:])
        # add 1 to every element in perm
        return perm

def check_if_valid(permutation):
    while len(permutation)>1:
        good, permutation = simulate_round(permutation)
        if not good:
            return False
    return True
            
def simulate_round(bracket):
    good = True
    new_bracket = [-1 for _ in range(len(bracket)//2)]
    # for loop for each number between 0 and len(bracket )

    for i in range(0, len(bracket), 2):
        if bracket[i]<bracket[i+1]:
            new_bracket[i//2] = bracket[i]
        else:
            good=False
            return (good, new_bracket)
    return good, new_bracket
    
for n in range(1,5):
    perm = permutations(2**n-1)
    for i in range(len(perm)):
        for j in range(len(perm[i])):
            perm[i][j] += 1
    # add 1 to every sublist of perm
    perm = [ [1] + p for p in perm ]
    valid_ones = [p for p in perm if check_if_valid(p)]
    print("n="+str(n),valid_ones[:3])
    print(len(valid_ones))

