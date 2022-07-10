# assume top row is rth row and then column as usual
def star_pattern(r, c):
    if r == 0:
        return
    if c < r:
        print("*", end=" ")
        star_pattern(r, c + 1)
    else:
        print()
        star_pattern(r - 1, 0)


# just reverse the printing,instead of printing first call the function first
def normal_triangle(r, c):
    if r == 0:
        return
    if c < r:
        normal_triangle(r, c + 1)
        print("*", end=" ")
    else:
        normal_triangle(r - 1, 0)
        print()


star_pattern(4, 0)
normal_triangle(4, 0)
