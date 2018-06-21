#What will be the output of following code.
#answer :- error , corrected code below

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
#print a.f(), b.f()
#print a.g(), b.g()
print(a.f(), b.f())
print(a.g(), b.g())
