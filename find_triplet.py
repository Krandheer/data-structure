arr = [1, 2, 3, 4, 5]
target = 9


def triplete():
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            temp = target - (arr[i] + arr[j])
            if temp in arr:
                if arr.index(temp) > i and arr.index(temp) > j:
                    return arr[i], arr[j], temp


def find_triplet(arr, target, triplet=[], index=0):
    if len(triplet) == 3 and sum(triplet) == target:
        return triplet
    if len(triplet) == 3 or index == len(arr):
        return None

    # take case
    triplet.append(arr[index])
    include_triplet = find_triplet(arr, target, triplet, index + 1)

    # not take case
    if include_triplet is None:
        triplet.pop()
        exclude_triplet = find_triplet(arr, target, triplet, index + 1)
    if include_triplet:
        return include_triplet
    elif exclude_triplet:
        return exclude_triplet
    else:
        return None


# Example usage
arr = [1, 2, 3, 4, 5]
target = 9
# result = find_triplet(arr, target)

# if result:
# print("Triplet found:", result)
# else:
# print("No triplet found")


def find_triplet_memo(arr, target, triplet=[], index=0, memo={}):
    if len(triplet) == 3 and sum(triplet) == target:
        return triplet
    if len(triplet) == 3 or index == len(arr):
        return None

    # Convert triplet to a tuple to use it as a key in the memoization dictionary
    triplet_key = tuple(triplet)

    if triplet_key in memo:
        return memo[triplet_key]

    # Take case
    triplet.append(arr[index])
    include_triplet = find_triplet_memo(arr, target, triplet, index + 1, memo)

    # Not take case
    if include_triplet is None:
        triplet.pop()
        exclude_triplet = find_triplet_memo(arr, target, triplet, index + 1, memo)

    if include_triplet:
        memo[triplet_key] = include_triplet
        return memo[triplet_key]
    elif exclude_triplet:
        memo[triplet_key] = exclude_triplet
        return memo[triplet_key]
    else:
        memo[triplet_key] = None
        return None


# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
target = 10
result = find_triplet_memo(arr, target)

if result:
    print("Triplet found:", result)
else:
    print("No triplet found")
