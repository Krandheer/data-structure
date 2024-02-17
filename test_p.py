"""
a variable defined outside the scope of function can be accessed 
inside the function but can't be modified without declaring it as 
global inside the function, if you try to modify without declaring it as global as actually python
creates new variable with same name inside the function instead of actually modifying the variable..
"""

# import requests
import math


def is_valid(s):
    """checking if ip is valid or not"""
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
            if not 0 <= int(i) <= 255:
                return 0
    return 1


# URL = "https://wsguat.writercorporation.com/AtmCassetteMapping/api/GetAtmCasseteMapping"
# API_KEY = "123456"
# API_VALUE = "ACM@123"
#
# headers = {"Authorization": f"{API_KEY} {API_VALUE}"}
#
#
# response = requests.get(URL, headers=headers)
#
# print(response)
# # Check if the request was successful (HTTP status code 200-299 typically indicates success)
# if response.status_code >= 200 and response.status_code < 300:
#     print("Request successful!")
#     print(response.json())  # If the API returns JSON data
# else:
#     print(f"Request failed with status code: {response.status_code}")
#     print(response.text)  # Print the response content for debugging purposes


def fun(a):
    """
    just checking variables
    """
    print(f"first a from fun {a}")
    a = a - 10
    print(f"a from fun {a}")


def main():
    """
    so this concludes that the variable from main is being copied to fun and
    the variable in main remains same, as python everything is call by value
    which basically implies copy.
    """
    a = 20
    print(f"a from main first time {a}")
    fun(a)
    print(f"a second time from main {a}")


# main()


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def dump(self) -> None:
        """method"""
        print(f"Object point@{id(self)}, x = {self.x}, y = {self.y}")

    def origin(self) -> float:
        """method"""
        return math.sqrt(self.x * self.x + self.y * self.y)


pt = Point(3, 4)
pt.dump()
print(pt.origin())
