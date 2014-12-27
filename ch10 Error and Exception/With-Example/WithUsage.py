__author__ = 'JimberXin'

"""
    Date: 2014/12/28
    Author: Junbo Xin
    ==============================Function===============================
    1): with_usage(): show how to use 'with' to operate file object
    2): try_finally_usage(): show how to use 'try' to operate file object
    3): with_to_try(): show how the 'with' module works inside.
    ================================Class================================
    DummyResource:  self-define of a context manage, and main function
    calls this class to show how to use it.
    Tips:
    **need to redefine
    1) __enter__() for allocation resource
    2) __exit__() for release resource
"""


def with_usage():
    with open(r'seomeFileName') as some_file:
        for line in somefile:
        print line
        # ...more code here


def try_finally_usage():
    some_file = open(r'someFileName')
    try:
        for line in some_file:
            print line
            # ... more code here
    finally:
        some_file.close()


def with_to_try(context_expression, target, with_body):
    context_manager = context_expression   # return a manager
    exit = type(context_manager).__exit__
    value = type(context_manager).__enter__(context__manager)
    exc = True
    try:
        try:
            target = value   # if used 'as' module
            # with_body
        except:
            # if exception happens
            exc = False
            # if __exit__ return True, ignore the except, otherwise raise exception
            # outer code deal with the exception
            if not exit(context_manager, *sys.exc_info()):
                raise
        finally:
            # exit normally, or break/exit/return, or ignore exception, do nothing
    if exc:
        exit(context_manager, None, None, None)
        # default return None, in the manager context regard as False


class DummyResource:
    def __init__(self, tag):
        self.tag = tag
        print 'Recource [%s]' % tag
        
    def __enter__(self):
        print '[Enter %s]: Allocate resource.' % self.tag
        return self    # return its ref

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print '[Exit %s]: Free resource.' % self.tag
        if exc_traceback is None:
            print '[Exit %s]: Exited without exception.' % self.tag
        else:
            print '[Exit %s]: Exited wih exception raised.' % self.tag
            return False


def main():
    print '=' * 60
    with DummyResource("Jimber's_Normal"):
        print '[with-body] Run without exceptions.'

    print '=' * 60
    with DummyResource("Jimber's_Exception"):
        print '[with-body] Run with exception.'
        raise Exception
print '[with-body] Run with exception.'

if __name__ == '__main__':
    main()
