class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro()) 
# Output: [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]