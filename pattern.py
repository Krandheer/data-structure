def star_pattern(r, c):
    if r == 0:
        return
    if c < r:
        print("*", end=" ")
        star_pattern(r, c + 1)
    else:
        print()
        star_pattern(r - 1, 0)


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
