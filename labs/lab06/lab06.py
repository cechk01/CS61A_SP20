this_file = 'lab06.py'
def make_adder_inc(n):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2) 
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    # def inc(g):
    #     while 1:
    #         yield g
    #         g= g + 1
    # i = inc(n)
    # x = 
    def make_adder(y):
        nonlocal n
        n += 1
        return  y + n -1
    return make_adder
def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    "*** YOUR CODE HERE ***"
    prev1 = 0
    prev2 = 0
    x= 0
    def fibber():
        nonlocal prev1
        nonlocal prev2
        nonlocal x
        if x == 0:
            x += 1
            return 0
        if x == 1:
            x = 2
            prev1 = 1
            return 1
        print("DEBUG: prev1", prev1)
        print("DEBUG: prev2", prev2)
        result = prev1 + prev2
        prev2 = prev1
        prev1 = result
        if prev1 == 0 & prev2 ==0:
            prev1 = 1
        
        # if x == 0:
        # x =
        return result
    return fibber

# Generators
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    for i in it:
        yield i * multiplier

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    yield n
    while n >1:   
        if n%2 ==0:
            n = int(n/2)
        else:
            n = n*3 +1
        yield n


