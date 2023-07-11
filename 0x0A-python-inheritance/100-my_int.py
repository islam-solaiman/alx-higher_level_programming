#!/usr/bin/python3
"""
    100-my_int: class inherits from int
    MyInt is a rebel. MyInt has == and != operators inverted
"""


class MyInt(int):
    """
        MyInt implements int. (inherits from)
    """
    def __init__(self, number):
        self.inumber = number

    def __eq__(self, value):
        return (self.number != value)
    
    def __ne__(self, value):
        return (self.number == value)
    
    def __str__(self):
        return (str(self.number))
