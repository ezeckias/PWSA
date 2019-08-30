def du(l):
    if len(l) == 0 or len(l) == 1:
        return l
    else:
        if l[0] in l[1:]:
            return du(l[1:])
        else:
            return [l[0]] + du(l[1:])







print(du([5,33,5]))