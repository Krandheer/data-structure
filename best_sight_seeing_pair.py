def maxScoreSightseeingPair(values) -> int:
    """
    given a list find best sight seeing pair
    leetcode solution day7
    """
    # a[i] + i + a[j] - j

    ans = 0
    best_max = 0
    for index, nums in enumerate(values):
        ans = max(ans, best_max + nums - index)
        best_max = max(best_max, index + nums)
    return ans

    # max_score = 0
    # for index, num in enumerate(values):
    #     for j in range(1, len(values)):
    #         if index < j and num + values[j]+index-j > max_score:
    #             max_score = num + values[j]+index-j

    # return max_score


print(maxScoreSightseeingPair([8, 1, 5, 2, 6]))
