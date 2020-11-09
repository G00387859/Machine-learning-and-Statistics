number = list(range(10))

def square(n):
    return n*n
def mapall(f,l):
    return[f(i) for i in l]
print(mapall(square, number))
