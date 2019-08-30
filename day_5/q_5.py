list1 = [1]

def count(list1, total = 0):
    if list1 == []:
        return total
    else:
        return count(list1[1:], total+1)

print(count(list1))
