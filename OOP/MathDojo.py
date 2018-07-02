#Part I
class MathDojo(object):
    def __init__(self):
        self.val = 0
    def add(self, *args):
        for arg in args:
            self.val += arg
        return self
    def subtract (self, *args):
        for arg in args:
            self.val -=  arg
        return self
    def result(self):
        print self.val

md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()

#Part II
def add_modified(self, *args):
    for arg in args:
        # self.val += arg
        if isinstance(arg, (list, tuple)):
            for i in range (0, len(arg)):
                self.val += arg[i]
        else:
            self.val += arg        
    return self

MathDojo.add = add_modified

def subtract_modified(self, *args):
    for arg in args:
        if isinstance(arg, (list, tuple)):
            for i in range (0, len(arg)):
                self.val -= arg[i]
        else:
            self.val -= arg        
    return self

MathDojo.subtract = subtract_modified
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract((1,2,7),6,9).result()


