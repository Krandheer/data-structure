def safest_home_from_wind_from_left_right(home_list):
    """
    param home_list:
    return: safe from left, safe from right, house to choose from
    """
    safe_from_left = []
    safe_from_right = []
    max_left = home_list[0]
    for index, value in enumerate(home_list):
        if index == 0:
            continue
        else:
            if value <= max_left:
                safe_from_left.append(index)
            else:
                max_left = value
    max_right = home_list[-1]
    for i in range(len(home_list) - 2, -1, -1):
        if home_list[i] <= max_right:
            safe_from_right.append(i)
        else:
            max_right = home_list[i]
    temp = []
    for i in safe_from_right:
        if i in safe_from_left:
            temp.append(i)
    result = [len(safe_from_left), len(safe_from_right), len(temp)]

    return result


home = [2, 3, 3, 1, 5]

print(safest_home_from_wind_from_left_right(home))