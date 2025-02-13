def get_match_index(string, pat):
    result = []
    len_str = len(string)
    len_pat = len(pat)
    for i in range(len_str - len_pat + 1):
        if string[i : i + len_pat] == pat:
            result.append(i)
    return result


STRING = "abababad"
PATTERN = "aba"

print(get_match_index(STRING, PATTERN))
