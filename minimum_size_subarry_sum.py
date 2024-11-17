from typing import List


def min_sub_array_len(target: int, nums: List[int]) -> int:
    i, j = 0, 0
    temp=0
    minimal_len = len(nums)+1
    while j < len(nums):
        temp+=nums[j]
        while temp>=target:
            minimal_len = min(minimal_len, j-i+1)
            temp-=nums[i]
            i+=1
        # increment is happening in last j-i+1 works otherwise j-i+1 would have not worked
        j+=1
    return minimal_len if minimal_len<=len(nums) else 0

print(min_sub_array_len(15, [1,2,3,4,5]))
