
# .1, (.97, .98, .99, 1.01, 1.02)

""" there are three scope
    - global
    - local
"""
from time import time, sleep


def rate_limited(max_calls):
    def wrapper(func):
        l = []

        def wrapped(x=0):
            cur_time = time()
            # make sure member not exceed (max_calls)
            if len(l) >= max_calls:
                if cur_time - l[0] < 1:
                    raise Exception("Error")
                else:
                    l.pop(0)
            l.append(cur_time)
            func(x)
        return wrapped
    return wrapper


def logger(func):
    def wrapped(*args, **kwargs):
        print 'logger - ', args, kwargs
        return func(*args, **kwargs)
    return wrapped


@logger
@rate_limited(max_calls=3)
def say_hi(x=0):
    print 'hi!', x


@rate_limited(max_calls=2)
def say_bye(x=0):
    print 'bye!', x

# say_hi()
# say_hi()
# say_hi(1)

# say_bye()
# say_bye()


# Create counter decorator

def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        if kwargs.get('reset', False):
            wrapper.counter = 0
        func(*args, **kwargs)
    wrapper.counter = 0
    return wrapper


@counter
def funcA(x=0, reset=False):
    print 'run funcA', x

funcA()
funcA()
funcA('x')
funcA(reset=True)
funcA()
print funcA.counter
