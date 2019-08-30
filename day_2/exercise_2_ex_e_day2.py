numbers = list(range(1000))

def isPrime(num):
    output = True
    for x in range(2,num):
        if num % x == 0 and num !=x:
            output = False
    return output

def theFilter(data,f):
    result = []
    for x in data:
        result.append(x)
    return result

filtered2 = theFilter(numbers,isPrime)

print(filtered2)

#filtered = list(filter(isPrime,numbers))
#print(filtered)