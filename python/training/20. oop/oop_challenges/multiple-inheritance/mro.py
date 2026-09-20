class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


class Pepito:
    pass


class E(D, Pepito):
    pass


print(E.mro())
