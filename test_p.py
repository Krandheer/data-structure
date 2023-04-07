def int_input(input):
    if input < 10:
        return input + 1
    else:
        return input // 10 + input + 1


print(int_input(29))

# class Vehicles:
#     def __init__(self, name):
#         self.name = name
#     def drive(self):
#         print(f"{self.name} is driving")
#
#
# class Car(Vehicles):
#     def __init__(self, model, color):
#         super().__init__(model)
#         self.color = color
#
# car = Car("nano", "red")
# car.drive()
