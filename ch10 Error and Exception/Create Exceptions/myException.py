__author__ = 'JimberXin'
"""
    Date: 2014/12/28
    Author:  Junbo Xin
    Description: Define two Error: FileError, NetworkError
"""

import os
import socket
import errno
import types
import tempfile


class NetWorkError(IOError):
    pass


class FileError(IOError):
    pass


# update the new exception arguments, and return
def update_args(args, newarg=None):
    if isinstance(args, IOError):
        myargs = []
        myargs.extend([arg for arg in args])
    else:
        myargs = list(args)

    if newarg:
        myargs.append(newarg)

    return tuple(myargs)


def file_args(file, mode, args):
    """ find the "permission denied" error: EACCES"""
    if args[0] == errno.EACCES and 'access' in dir(os):
        perms = ''
        permd = {'r': os.R_OK, 'w': os.W_OK, 'x': os.X_OK}
        pkeys = permd.keys()
        pkeys.sort()
        pkeys.reverse()

        for each_perm in 'rwx':
            if os.access(file, permd[each_perm]):  #
                perms += each_perm
            else:
                perms += '-'

        if isinstance(args, IOError):
            myargs = []
            myargs.extend([arg for arg in args])
        else:
            myargs = list(args)

        myargs[1] = "'%s' %s (perms: '%s')" % (mode, myargs[1], perms)

        myargs.append(args.filename)

    else:
        myargs = args

    return tuple(myargs)


def myconnect(sock, host, port):
    try:
        sock.connect((host, port))
    except socket.error, args:   # only capture IOError
        myargs = update_args(args)
        if len(myargs) == 1:    # no #s on some errs
            myargs = (errno.ENXIO, myargs[0])

        raise NetWorkError, update_args(myargs, host + ': ' + str(port))


def myopen(file, mode='r'):
    try:
        fo = open(file, mode)
    except IOError, args:
        raise FileError, file_args(file, mode, args)

    return fo


def test_file():
    file = tempfile.mktemp()  # create a temporary file
    f = open(file, 'w')
    f.close()

    # define 4 types permission: 1)0: no per; 2)0100:excute, 3)0400:read 4)0500: read & excute
    for each in ((0, 'r'), (0100, 'r'), (0400, 'w'), (0500, 'w')):
        try:
            os.chmod(file, each[0])
            f = myopen(file, each[1])

        except FileError, args:
            print "%s: %s" % (args.__class__.__name__, args)

    else:
        print file, "open ok...perm ignored."
        f.close()

    os.chmod(file, 0777)  # enable all permissions
    os.unlink(file)


def test_net():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for each in ('deli', 'www'):
        try:
            myconnect(s, 'deli', 8080)
        except NetWorkError, args:
            print "%s: %s" % (args.__class__.__name__, args)


if __name__ == '__main__':
    test_file()
    test_net()







