def denom_val(denoms, amount):
    amount = amount - sum(denoms)
    dic = {}
    for elem in denoms:
        dic[elem] = 1
    done = False
    for elem in denoms:
        if amount >= elem and amount % elem == 0:
            dic[elem] += amount // elem
            amount = 0
            done = True
        if not done:
            while amount >= elem:
                amount -= elem
                dic[elem] += 1

    return dic


denom = [500, 200, 100]
amount = 1900

print(denom_val(denom, amount))
