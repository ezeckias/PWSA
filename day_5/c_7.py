def zips(list1,both = []):
    if (len(list1) != 0):
        sub_arr = []
        next_arr = []
        for c in list1:
            if len(c) != 0:
                sub_arr.append(c[0])
                next_arr.append(c[1:])
        if sub_arr != []:
            both.append(sub_arr)
        return zips(next_arr,both)
    else:
        return both

def sum_list(list1):
    return list1[0] + list1[1]

# print(list(map(sum_list, zip([1,2,3,4,5],[6,7,8,9,0,4]))))
print(zips([[31,2,43,4,5],[6,7,8,9,0],[6,17,8,9,0]]))



