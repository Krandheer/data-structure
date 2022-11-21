"""cat sat on the mat
    dog sat on the mat
"""


def listtype(list1):
    dict1 = {}
    for elem in list1:
        if type(elem) in dict1:
            dict1[type(elem)] += 1
        else:
            dict1[type(elem)] = 1

    dict1 = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    if len(dict1) > 1:
        return f"list is hetrogenous, with larget element of datatype {dict1[0]}"


list1 = [1, 2, 'rande', 'su', 'na']
print(listtype(list1))

"""def jacardiandistance(str1, str2):
    dict1 = {}
    dict2 = {}

    str1 = str1.split(" ")
    str2 = str2.split(" ")

    for word in str1:
        if word is not dict1:
            dict1[word] = 1

        dict1[word] += 1

    for word in str2:
        if word is not dict2:
            dict2[word] = 1

        dict2[word] += 1

    listofkey = []
    for key in dict1.keys():
        if key in dict2.keys():
            listofkey.append(key)

    denominator = len(listofkey)

    if len(str1) > len(str2):
        numerator = len(str1)
    else:
        numerator = len(str2)

    return numerator / denominator"""

# str1 = "cat sat on the mat"
# str2 = "dog sat on the mat"
# print(jacardiandistance(str1, str2))
