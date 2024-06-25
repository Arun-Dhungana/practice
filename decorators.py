# here output will be hello .why???
# because as init wraps square and init returns wrapper function so when square function is invoked actually wrapper function is activated ignoring the square function,so if we want to execute square function we must call it inside the wrapper function using func arg which takes square ass args ...also we can take func and return func in python
# def init(func):
#     def wrapper(*args):
#         result = "hello"
#         return result

#     return wrapper

import time


# here the function is called inside wrapper
def init(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Completed in {(end-start)*1000} mili seconds.")
        return result

    return wrapper


@init
def square(numbers):
    arrary = []
    for number in numbers:
        arrary.append(number * -1)
    return arrary


num = range(1, 6)
result = square(num)
print(result)
