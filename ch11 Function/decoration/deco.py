__author__ = 'JimberXin'
"""  Date: 2014/01/04
     Author:  Junbo Xin
     Description:  decoration of function
"""

from time import ctime, sleep


def test_fun(func):
    def wrapped_fun():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()
    return wrapped_fun


@test_fun
def foo():
    pass


foo()
sleep(4)


for i in range(2):
    sleep(1)
    foo()