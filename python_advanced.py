class MathDojo(object):
    def __init__(self,total=0):
        self.total = total
    def add (self,*args):
        for arg in args:
            if type(arg) == tuple or type(arg) == list:
                for item in arg:
                    self.total += item
            else:
                self.total += arg
        return self
    def subtract(self,*args):
        for arg in args:
            if type(arg) == tuple or type(arg) == list:
                for item in arg:
                    self.total -= item
            else:
                self.total -= arg
        return self

class Underscore(object):
    def map(self,x,y):
        for index, item in enumerate(x):
            x[index] = y(item)
        return x

    def reduce(self,x,y):
        total = 0
        for item, val in enumerate(x):
            total += y(val)
        return total

    def find(self,x,y):
        for index,val in enumerate(x):
            if val == y:
                return index
        return -1

    def filter(self,x,y):
        for index,val in enumerate(x):
            if not y(val):
                del x[index]
        return x

    def reject(self,x,y):
        for item in x:
            if type(item) != y:
                return True
        return False
