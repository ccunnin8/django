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
