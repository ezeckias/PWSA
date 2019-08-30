def zip(list1,list2,both = []):
    if (len(list1) != 0) and (len(list2) != 0):
        both.append([list1[0],list2[0]])
        return zip(list1[1:],list2[1:],both)
    else:
        return both

def sum_list(list1):
    return list1[0] + list1[1]

print(list(map(sum_list, zip([1,2,3,4,5],[6,7,8,9,0,4]))))
# print(zip([1,2,3,4,5],[6,7,8,9,0,4]))













# from functools import reduce

# def sum_list2(list1, acc):
#     acc.append(list1[0] + list1[1])
#     return acc


# def reduce(f,l,acc):
#     if l == []:
#         return  acc
#     elif len(l) == 1:
#         return f(l[0], acc)
#     else:
#         return reduce(f,l[1:],f(l[0], acc))