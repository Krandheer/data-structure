def star_pattern(r, c):
    if r == 0:
        return
    if c < r:
        print("*", end=" ")
        star_pattern(r, c + 1)
    else:
        print()
        star_pattern(r - 1, 0)


star_pattern(4, 0)
