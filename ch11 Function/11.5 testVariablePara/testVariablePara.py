__author__ = 'JimberXin'

"""
    Author:  Junbo Xin
    Date:   2015/01/07
    Description:  test the non-keyword and keyword parameter in function
    Notice: Use repr() function to display, not str()
"""


def test_fun(func, *non_keyword, **keyword):
    try:
        retval = func(*non_keyword, **keyword)
        result = (True, retval)
    except Exception, diag:
        result = (False, str(diag))
    return result


def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')

    for each_fun in funcs:
        print '=' * 70
        for each_val in vals:
            retval = test_fun(each_fun, each_val)
            if retval[0]:
                print '%s(%s)' % (each_fun.__name__, repr(each_val)), retval[1]
            else:
                print 'Failed: %s(%s)' % (each_fun.__name__, repr(each_val)), retval[1]


if __name__ == '__main__':
    test()