def reverse_characters(temp_str):
    temp = list(temp_str)
    i = 0
    j = len(temp_str) - 1
    while i < j:
        if ord(temp[i]) in range(96, 123) and ord(temp[j]) in range(96, 123):
            temp[i], temp[j] = temp[j], temp[i]
            i+=1
            j-=1
        elif ord(temp[i]) not in range(96, 123) and ord(temp[j]) not in range(96, 123):
            i += 1
            j -= 1
        elif ord(temp[i]) not in range(96, 123):
            i += 1
        elif ord(temp[j]) not in range(96, 123):
            j -= 1
    return "".join(temp)


print(reverse_characters("ab-cd"))
