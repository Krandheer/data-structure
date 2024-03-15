# nums1 = [-5, 4]
# nums2 = [1, 7, 8, 9]


# def find_median(nums1, nums2):
#     temp = []
#     i = 0
#     j = 0
#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] < nums2[j]:
#             temp.append(nums1[i])
#             i += 1
#         else:
#             temp.append(nums2[j])
#             j += 1

#     if j < len(nums2):
#         temp = temp + nums2[j:]
#     elif i < len(nums1):
#         temp = temp + nums1[1:]
#     return temp


# print(find_median(nums1, nums2)


class Order:
    def __init__(self) -> None:
        self.order_item = {}
        self.quantities = 0

    def add_itmes(self, item, quantity, price):
        self.quantities += quantity
        self.order_item[item] = (quantity, price)

    def total_price(self):
        tot_pr = 0
        for _, v in self.order_item.items():
            tot_pr += v[1]
        return tot_pr


order = Order()
order.add_itmes("keyboard", 21, 50)
order.add_itmes("mouse", 20, 40)
print(order.order_item)
print(order.quantities)
print(order.total_price())
