class B:
    __count = 0

    def __init__(self):
        B.__count += 1

    def __del__(self):
        B.__count -= 1


a = B()
print(B._B__count)

def gen(n):
    while n != 0:
        yield n-1
        n-=1

# g = gen(4)

for i in gen(4):
    print(i)