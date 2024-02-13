class Gimzo:
    def __init__(self):
        print(f"Gimzo id: {id(self)}")

# it proves that object is created first then assignment happens, and the
# assignment varible is just a reference to object
x = Gimzo()
