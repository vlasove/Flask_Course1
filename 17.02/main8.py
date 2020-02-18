def SuperFunc(*args):
    print(type(args))
    print(sum(args))


def KfUNC(**kwargs):
    print(type(kwargs))
    print(kwargs)

SuperFunc(1,2,3,4,5,12,312,312,3)
KfUNC(A = 2, B = 3)