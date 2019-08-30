marks = [2,9,3,5,1,33,6,3,3,4,2]
marks2 = [56,34,23,1,2,3]


def filter(list1,list2,f):
    inter = []
    for n in list1:
        if f(list2,inter, n) == True:
                inter.append(n)
    return inter


def search(list1,element):
    decision = False
    for n in list1:
        if n == element:
            decision = True
    return decision


def cond(list1,inter,n):
    if search(list1, n) == True:
        # remove duplicates
        if search(inter, n) == False:
            return True
        else:
            return False
    else:
        return False


def find(list1,list2,f):
    return filter(list1,list2,f)

print(find(marks,marks2,cond))