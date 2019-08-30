marks = [2,9,3,5,1,33,6,3,3,4,2]
marks2 = [56,34,23,1,2,3]
# find the maximum

# maximum
def max_list(list1):
    sum_total = 0
    for n in list1:
        sum_total = sum_total + n
    return sum_total

# average
def average_list(list1):
    return max_list(list1) / len(list1)
    

# Problem 3
def midle_list(list1):
    return list1[int(len(list1)/2)]

# delete function
def remove_element(list1,position):
    new_list = []
    # insert the left part
    for n in list1[:position]:
        new_list.append(n)
    # insert the left part
    left_position = position + 1
    for x in list1[left_position:]:
        new_list.append(x)
    return new_list

# problem 4
def first(list1, k):
    for i in list1[:k]:
        print(i)
#first(marks,4)


# Ploblem 5
def duplicate_list(list1):
    list_new = []
    for n in list1:
        if n not in list_new:
            list_new.append(n)
    return list_new
#print(duplicate_list(marks))


def search(list1,element):
    decision = False
    for n in list1:
        if n == element:
            decision = True
    return decision


# Ploblem 6
def union(list1,list2):
    union_list = duplicate_list(list1)
    for n in list2:
        if search(list1, n) == False:
            union_list.append(n)
    return union_list
#print(union(marks,marks2))        
    
#Ploblem 7
def intersection(list1,list2):
    inter = []
    for n in list1:
        if search(list2, n) == True:
            # remove duplicates
            if search(inter, n) == False:
                inter.append(n)
    return inter
#print(intersection(marks,marks2))  

#Problem 8
def different(list1,list2):
    different = []
    inter_list = intersection(list1,list2)
    
    for n in list1:
        if search(inter_list,n) == False:
            different.append(n)
    return different
#print(different(marks,marks2))


#Problem 9
def symetric(list1,list2):
    symetric_list = []
    union_list = union(list1,list2)
    intersection_list = intersection(list1,list2)
    #list 1
    for n in union_list:
        if search(intersection_list,n) == False:
            symetric_list.append(n)
    return symetric_list

#print(symetric(marks,marks2))


# Ploblem 10
def shift(k,c):
    c = c.lower()
    characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    # find the position
    position = 0
    for i in range(len(characters)):
        if characters[i] == c:
            position = i
 
    pos = (position + k)%len(characters)
    return characters[pos] 

# Ploblem 11
def caesar(k,c):
    shifted = ''
    for v in c:
        shifted = shifted + shift(k, v)
    return shifted
#print(caesar(-4,caesar(4,'january is awesome IM THE BEST')))
# print(caesar(4,'january is awesome IM THE BEST'))

#print(max_list(marks))
#print(average_list(marks))
#print(midle_list(marks))

#duplicate_list(marks)