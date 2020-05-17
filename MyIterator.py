'''
Iterator is a more general concept: any object whose class has a next method (__next__ in Python 3) and an __iter__ method that does return self.

Refence Link : https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators

'''

class squares(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self): return self
    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        current = self.start * self.start
        self.start += 1
        return current

iterator = squares(1,5)

for i in iterator:
    print(i)
