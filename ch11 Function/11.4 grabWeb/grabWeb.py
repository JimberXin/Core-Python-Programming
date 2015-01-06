__author__ = 'JimberXin'

"""
   Author:  Junbo Xin
   Date:   2015/01/06
   Description:  use urllib to grab web, download() function to deal with different urls
     finally grab a web of Baidu ,and print the first and last not bland line of the html file
"""


from urllib import urlretrieve


def first_not_blank(lines):
    for each_line in lines:
        if not each_line.strip():
            continue
        else:
            return each_line


def first_last(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print first_not_blank(lines)
    lines.reverse()
    print first_not_blank(lines)


def download(url='http://www.baidu.com',  process=first_last):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:
        process(retval)


if __name__ == '__main__':
    download()