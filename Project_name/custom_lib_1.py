import os

class custom_lib_1:
    def __init__(
        self
    ):
        self.some_var = 1


    def some_function(
        self
    ):
        print("Hello")


from Project_name.custom_lib_1 import custom_lib_1 as cl1
