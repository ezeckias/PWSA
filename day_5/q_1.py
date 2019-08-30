def du(l):
    if len(l) == 0 or len(l) == 1:
        return l
    else:
        if l[0] in l[1:]:
            return du(l[1:])
        else:
            return [l[0]] + du(l[1:])

def find(l,s):
    both = l+s
    return du(both)

print(find([1,2,3,4,6],[4,6,7,8,5]))
