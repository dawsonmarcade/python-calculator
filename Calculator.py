'''

Initializing the math Class of Python

'''

class Calculator:
    def __init__(self,x):
        self.x = x
        
    
    def __add__(self, *args):
        self.values = list(args)
        if isinstance(self.values, Calculator):
            addition = [self.x + self.values for i in self.values]

        return addition


