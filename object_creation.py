class Gimzo:
    def __init__(self):
        print(f"Gimzo id: {id(self)}")


# it proves that object is created first then assignment happens, and the
# assignment varible is just a reference to object
# x = Gimzo()


def func(a):
    """checking how mutable variable as arguemnt works in python, it does
    shallow copy of variable so referencing to same object, hence not a good
    idea to pass it as argument or be careful when doing so."""
    print(id(a))
    # this creates the shallow copy of b but the index at which [3, 4] is in b
    # is not copies and it reference to same [3, 4] so if value at refereces
    # itself is changed then the list inside changes but if list inside list is
    # changes then it gets reflected in both.
    a = list(a)
    a[-1][0] = 4
    print(a)
    print(id(a))


b = [1, 2, [3, 4]]
print(id(b))
func(b)
# we can see that b is also changed, so passing mutable variable as arguemnt
# and then modifying it inside the function is not a great idea of that mutable
# variable has to be use in future too.
print(b)
