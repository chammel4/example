#! usr/local/bin python
# hello.py

import functools

class Counter:

    def __init__(self, low, high):
        self.current = low
        self.high = high


    def __iter__(self):
        return self


    def next(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

def square(num):
    return num*num


if __name__=='__main__':

    x = range(1,6)
    product = lambda x, y: x * y
    square = lambda x: x * x
    isEven = lambda x: x % 2 == 0

    print(list(filter(isEven, x)))
    print(reduce(product,x))

    for c in Counter(3,8):
        print(c)

