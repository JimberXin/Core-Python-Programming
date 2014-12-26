"""Judge whether num is a prime or not:
	if it's not a prime,  print its max divisor,
	if it's a prime, print 'P'
	In the main function, print (2,100)'s max divisor"""
__author__ = 'JimberXin'


def show_max_factor(num):
	count = num / 2
	while count > 1:
		if num % count == 0:
			print '%d: %d  ' % (num, count),
			break
		count -= 1
	else:  # only if while is ended count == 1
		print num, ': P   ',


if __name__ == '__main__':
	for each in range(2, 100):
		show_max_factor(each)
		if each % 10 == 0:   # print 10 nums each line
			print ''

