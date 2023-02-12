def grid_travel(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_travel(m - 1, n) + grid_travel(m, n - 1)


# 	grid_traveller(a,b)=grid_traveller(b,a), implement dp on this ?


print(grid_travel(3, 3))
