numbers = [13,24,35,44,65,6,7,78,9,9,10]

def check(x):
    if x > 5:
        return True
    else:
        return False

def my_filter(f,list1):
    if len(list1) == 0:
        return []
    elif len(list1) >= 1:
        if f(list1[0]) == True:
            return [list1[0]] + my_filter(f,list1[1:])

print(my_filter(check,numbers))
