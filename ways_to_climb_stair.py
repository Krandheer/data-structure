def ways_to_climb_stairs(p, target, ans):
    if target == 0:
        ans.append(list(p))
        return
    ways_to_climb_stairs(p + str(1), target - 1, ans)
    if target >= 2:
        ways_to_climb_stairs(p + str(2), target - 2, ans)
    if target >= 3:
        ways_to_climb_stairs(p + str(3), target - 3, ans)
    # return len(ans)
    return ans


def way_dp(target, dp):
    if target == 1 or target == 2:
        return target
    elif target == 0:
        return 1
    elif dp[target] != -1:
        return dp[target]
    else:
        dp[target] = (
            way_dp(target - 1, dp) + way_dp(target - 2, dp) + way_dp(target - 3, dp)
        )
        return dp[target]


# print(ways_to_climb_stairs("", 10, []))
# print(way_dp(10, [-1] * 11))
