def grid_travel(m, n):
    if m == 1 or n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_travel(m - 1, n) + grid_travel(m, n - 1)


# print(grid_travel(3, 3))


def grid_travel_path(p, m, n):
    if m == 1 and n == 1:
        print(p)
        return
    if m > 1:
        grid_travel_path(p + 'D', m - 1, n)
    if n > 1:
        grid_travel_path(p + 'R', m, n - 1)
    return p


# a = grid_travel_path("", 2, 2)
# print(a)


def grid_travel_path_list(p, m, n, ans):
    # last line return statement is what makes value to be returned after all execution,
    if m == 1 and n == 1:
        ans.append(p)
        return
    if m > 1:
        grid_travel_path_list(p + 'D', m - 1, n, ans)
    if n > 1:
        grid_travel_path_list(p + 'R', m, n - 1, ans)

    return ans


# print(grid_travel_path_list("", 2, 2, []))

def grid_travel_path_list2(p, m, n):
    # last line return statement is what makes value to be returned after all execution,
    # returning list without passing list in function calls
    if m == 1 and n == 1:
        return [p]
    result = []
    if m > 1:
        result = result + grid_travel_path_list2(p + 'D', m - 1, n)
    if n > 1:
        result = result + grid_travel_path_list2(p + 'R', m, n - 1)

    return result


print(grid_travel_path_list2("", 2, 2))
