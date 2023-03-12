# def outer(msg="hii"):
#     def inner():
#         print(msg)
#     return inner
# hi=outer("temp")
# # hi()
#
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print(f"wrapper execute this before {original_function.__name__}")
#         return original_function(*args, **kwargs)
#
#     return wrapper_function
#
#
# #
# #
# # class decorator_class(object):
# #     def __init__(self, original_function):
# #         self.original_function = original_function
# #
# #     def __call__(self, *args, **kwargs):
# #         print(f"wrapper execute this before {self.original_function.__name__}")
# #         return self.original_function(*args,**kwargs)
#
#
# @decorator_function
# def display():
#     print("Display")
#
#
# @decorator_function
# def display_info(name, age):
#     print("display_info {} {}".format(name, age))
#
#
# # display = decorator_function(display)
# display_info("john", 25)
# display()




def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__, '\n')
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator('LOG:')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))
