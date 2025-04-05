
'''
__getitem__ method

It enables access to elements in custom classes using square brackets just like lists
'''

class MyCustomClass:
    def __init__(self):
        self.data = [0,1,2,3,4,5]

    def __getitem__(self, idx):
        return self.data[idx]