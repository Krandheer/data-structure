def lis(arr, n):
    # this function basically gives the longest increasing subsequence, and then we will subtract this length
    # from overall length to get number of elements to be deleted
    result = 0
    lst = [1] * n
    for i in range(1, n):
        for j in range(i):
            if (arr[i] > arr[j] and
                    lst[i] < lst[j] + 1):
                lst[i] = lst[j] + 1

    for i in range(n):
        if result < lst[i]:
            result = lst[i]

    return result


# Function to calculate minimum number of deletions
def minimum_number_of_deletions(arr, n):
    return n - lis(arr, n)


arr = [30, 40, 2, 5, 1, 7, 45, 50, 8]
n = len(arr)
print("Minimum number of deletions = ",
      minimum_number_of_deletions(arr, n))
