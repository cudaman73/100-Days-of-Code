def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4,5,6,7,89,90))

def calculate(n, **kwargs):
    print(n + kwargs["add"])
    print(n * kwargs["mult"])


calculate(2, add=3, mult=5)
