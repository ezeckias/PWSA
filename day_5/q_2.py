

def combine(list1,list2):
    if len(list1) == 1:
        return list2.append(list1[0])
    elif len(list1) == 0:
        return list2
    else:
        list2.append(list1[0])
        combine(list1[1:],list2)
    return list2


def du(l):
    if len(l) == 0 or len(l) == 1:
        return l
    else:
        if l[0] in l[1:]:
            return du(l[1:])
        else:
            return [l[0]] + du(l[1:])

print(combine([1,2,3,4,6],[4,6,7,8,5]))
print(du(combine([1,2,3,4,6],[4,6,7,8,5])))


















# def combine(l1,l2):
#     if len(l1) == 0 and len(l2) == 0:
#         return l1+l2
#     else:
#         # element = l1 +l2
#         out = []
#         if (l1[0] not in l1[1:]) and (l1[0] not in l2[1:]):
#             out.append(l1[0])
#         if (l2[0] not in l1[1:]) and (l2[0] not in l2[1:]):
#             out.append(l2[0])
#         return out + combine(l1[1:],l2[1:])

# print(combine([1,2,3,4,6],[4,6,7,8,5]))