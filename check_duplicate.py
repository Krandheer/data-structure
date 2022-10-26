def contains_duplicate(nums):
    # nums is array of integer
    # leet code question
    return len(nums) != len(set(nums))


def contains_duplication2(nums):
    # we can also use dictionary and track how many times a number appears

    hash_map = {}
    for i in nums:
        if i in hash_map:
            return True
        else:
            hash_map[i] = i
    return False
