def mymap(f,list1):
    result = []
    for i in list1:
        result.append(f(i))
    return result



def calculate(list1,c):
    return mymap(c,list1)

def g(x):
    return x * x

numbers = [1,2,3,4,5,6]
print(calculate(numbers,g))
#print(calculate(numbers,g))