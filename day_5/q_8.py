# a = range(3)
# for i in a:
#     print('hello')
# print(next(a))


def collate(number):
    while number != 1:
        if number % 2 == 0:
            number = number/2
            yield number
        else:
            number = (3*number)+1
            yield number

# datas = collate(13)

# for x in datas:
#     print(x)

def multiples(number):
    n = 1
    while True:
        n=n+1
        num = n * number
        yield num

# g = multiples(17)

# for c in g:
#     print(c)