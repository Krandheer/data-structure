def grid_travel(i, j):
    if i == 0 or j == 0:
        return 1
    if i < 0 or j < 0:
        return 0
    return grid_travel(i - 1, j) + grid_travel(i, j - 1)


# 3*3 grid
# print(grid_travel(1, 1))


def grid_travel_dp(i, j, dp):
    if i == 0 or j == 0:
        return 1
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = grid_travel_dp(i - 1, j, dp) + grid_travel_dp(i, j - 1, dp)
    return dp[i][j]


# dp_1 = [[-1 for j in range(3)] for i in range(3)]
# print(grid_travel_dp(2, 2, dp_1))


def grid_travel_bottom_up(i, j, dp):
    for i in range(i + 1):
        for j in range(j + 1):
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                left = 0
                up = 0
                if i >= 1:
                    left = dp[i - 1][j]
                if j >= 1:
                    up = dp[i][j - 1]
                dp[i][j] = left + up
    return dp[i][j]


dp_1 = [[-1 for j in range(3)] for i in range(3)]
# print(grid_travel_bottom_up(2, 2, dp_1))


def grid_travel_path(p, m, n):
    if m == 1 and n == 1:
        print(p)
        return
    if m > 1:
        grid_travel_path(p + "U", m - 1, n)
    if n > 1:
        grid_travel_path(p + "L", m, n - 1)
    return p


# a = grid_travel_path("", 2, 2)
# print(a)


def grid_travel_path_list(p, m, n, ans):
    # last line return statement is what makes value to be returned after all execution,
    if m == 1 and n == 1:
        ans.append(p)
        return
    if m > 1:
        grid_travel_path_list(p + "U", m - 1, n, ans)
    if n > 1:
        grid_travel_path_list(p + "L", m, n - 1, ans)

    return ans


# print(grid_travel_path_list("", 2, 2, []))


def grid_travel_path_list2(p, m, n):
    # last line return statement is what makes value to be returned after all execution,
    # returning list without passing list in function calls
    if m == 1 and n == 1:
        return [p]
    result = []
    if m > 1:
        result = result + grid_travel_path_list2(p + "U", m - 1, n)
    if n > 1:
        result = result + grid_travel_path_list2(p + "L", m, n - 1)

    return result


# print(grid_travel_path_list2("", 2, 2))
