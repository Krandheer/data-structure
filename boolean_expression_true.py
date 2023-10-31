def f(i, j, isTrue, exp):
    if i > j:
        return 0
    if i == j and isTrue:
        return exp[i] == "T"
    else:
        return exp[i] == "F"
