import copy
import itertools

def generate_subsets(s):
    subsets = []
    for i in range(len(s)):
        subset = itertools.combinations(s, i+1)
        for _subset in subset:
            subsets.append(_subset)
    return subsets

def check_subsets(s, i, j):

    s_i = sum(s[i])
    s_j = sum(s[j])

    if s_i == s_j:
        #print(subsets[i], subsets[j], s_i, s_j)
        return False

    l_i = len(s[i])
    l_j = len(s[j])

    if l_i > l_j and s_i < s_j:
        #print(subsets[i], l_i, s_i, subsets[j], l_j, s_j)
        return False
    elif l_j > l_i and s_j < s_i:
        #print(subsets[i], l_i, s_i, subsets[j], l_j, s_j)
        return False 

    return True
    
def check_set(s):
    subsets = generate_subsets(s)
    for i in range(len(subsets)):
        for j in range(i+1, len(subsets)):
            if not check_subsets(subsets, i, j):
                return False
    return True

def listor(l):
    for ll in l:
        if ll:
            return True
    return False

def adjust_set(s, i, j):
    orig_s = copy.copy(s)
    s[i] += -2
    s[j] += 1
    print(s, check_set(s))
    if check_set(s):
        return s, True
    else:
        return orig_s, False

def minimize_set(s):
    orig_s = s
    while True:
        all_updated = []
        for i in range(len(s)):
            for j in range(len(s)):
                if i != j:
                    s, updated = adjust_set(s, i, j)
                    all_updated.append(updated)

        if not listor(all_updated):
            break
    print(s)
    return s
        

min_set = minimize_set([3, 6, 7, 8])

#min_set = minimize_set([11, 17, 20, 22, 23, 24])

print(sum(min_set))
print(check_set(min_set))
