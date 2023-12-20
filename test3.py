def good_pairs(num):
    counter = 0
    for i in range(len(num)):
        for j in range(i, len(num)):
            if num[i] == num[j] and i < j:
                counter += 1
    return counter


temp1 = [1, 2, 3, 1, 1, 3]
print(good_pairs(temp1))
