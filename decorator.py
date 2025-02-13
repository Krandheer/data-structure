# decorators are used to extend the functionality of the function on which it is used.


def start_end_decorator(func):
    def wrapper():
        print("start of function")
        func()
        print("end of function")

    return wrapper


@start_end_decorator
def print_name():
    print("randheer")


print_name()
