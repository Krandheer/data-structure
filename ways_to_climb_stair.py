def ways_to_climb_stairs(p, target, ans):
    if target == 0:
        ans.append(p)
        return
    ways_to_climb_stairs(p + str(1), target - 1, ans)
    if target >= 2:
        ways_to_climb_stairs(p + str(2), target - 2, ans)
    if target >= 3:
        ways_to_climb_stairs(p + str(3), target - 3, ans)
    return len(ans)


print(ways_to_climb_stairs("", 4, []))

