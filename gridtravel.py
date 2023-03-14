def grid_travel(i, j):
    if i == 0 or j == 0:
        return 1
    if i < 0 or j < 0:
        return 0
    return grid_travel(i - 1, j) + grid_travel(i, j - 1)


# 3*3 grid
# print(grid_travel(2, 2))


def grid_travel_dp(i, j, dp):
    if i == 0 or j == 0:
        return 1
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = grid_travel_dp(i - 1, j, dp) + grid_travel_dp(i, j - 1, dp)
    return dp[i][j]


dp_1 = [[-1 for j in range(3)] for i in range(3)]
print(grid_travel_dp(2, 2, dp_1))


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

# print(grid_travel_path_list2("", 2, 2))
