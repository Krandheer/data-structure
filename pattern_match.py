def get_match_index(string, pat):
    result = []
    # i think take or not take will work here
    # and i feel i need to do dsa question or watch DSA related vidoes everyday
    # for a hour atleast to stay warmed up all time
    len_str = len(string)
    len_pat = len(pat)
    for i in range(len_str - len_pat + 1):
        if string[i : i + len_pat] == pat:
            result.append(i)
    return result


STRING = "abababad"
PATTERN = "aba"

print(get_match_index(STRING, PATTERN))
