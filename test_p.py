"""
a variable defined outside the scope of function can be accessed inside the function but can't be modified without
 declaring it as global inside the function, if you try to modify without declaring it as global as actually python
 creates new variable with same name inside the function instead of actually modifying the variable..
"""


def isValid(s):
    # code here
    ipv4 = s.split(".")
    is_ok = True
    temp = 0

    if len(ipv4) == 4:
        for i in ipv4:
            if int(i) == 0:
                temp = temp + 1
            if temp == 4:
                is_ok = False
            if not is_ok:
                return 0
            if not (0 <= int(i) <= 255):
                return 0
    return 1


# print(isValid("0.0.0.0"))

# a = {
#     "name": 'randheer'
# }
# b = {"name": "poonam"}
#
#
# def change():
#     # global a
#     a = b
#     print(a['name'])
#
#
# change()
# print(a)

with open("writer_app_log", 'a') as f:
    atm_id = '1234'
    f.write(f"{atm_id}, data from ocr",)
