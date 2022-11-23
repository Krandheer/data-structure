def powerset(temp_p, temp_up):
    if len(temp_up) == 0:
        print(temp_p)
        return
    elem = temp_up[0]
    powerset(temp_p+elem, temp_up[1:])
    powerset(temp_p, temp_up[1:])
#
#
# powerset("", 'abc')


def powerset2(temp_p, temp_up, ans):
    if len(temp_up) == 0:
        ans.append(temp_p)
        return
    elem = temp_up[0]
    powerset2(temp_p, temp_up[1:], ans)
    powerset2(temp_p + elem, temp_up[1:], ans)

    return sorted(sorted(ans), key=lambda x: len(x))


temp_ans = []
print(powerset2("", 'abc', temp_ans))

