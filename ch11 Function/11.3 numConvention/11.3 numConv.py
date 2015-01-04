__author__ = 'JimberXin'
"""
    Date: 2015/01/04
    Author: Junbo Xin
    Description: in the main function, convert() function uses
      int(), long(), and float() built-in function to convert.
"""

def convert(func, seq):
    'conv. sequence of numbers to same type'
    return [func(eachNum) for eachNum in seq]

myseq = (123, 45.67, -6.2e8, 999999999999L)


def main():
    print convert(int, myseq)
    print convert(long, myseq)
    print convert(float, myseq)


if __name__ == '__main__':
    main()