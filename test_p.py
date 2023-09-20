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
import requests

url = "https://wsguat.writercorporation.com/AtmCassetteMapping/api/GetAtmCasseteMapping"
api_key = "123456"
api_value = "ACM@123"

headers = {
    "Authorization": f"{api_key} {api_value}"
}


response = requests.get(url, headers=headers)

print(response)
# # Check if the request was successful (HTTP status code 200-299 typically indicates success)
# if response.status_code >= 200 and response.status_code < 300:
#     print("Request successful!")
#     print(response.json())  # If the API returns JSON data
# else:
#     print(f"Request failed with status code: {response.status_code}")
#     print(response.text)  # Print the response content for debugging purposes


