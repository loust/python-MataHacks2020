import sys

def newfunction()

class Project_name:
    def __init__(
        self
    ):
        self.global_var_only_for_this_class = 1


    def newfunction(
        self,
        param1=None,
        param2=1
    ):
        return True



newfunction() <--- Line 3


from Project_name import Project_name as pn


pn.newfunction() <-- Line 12

