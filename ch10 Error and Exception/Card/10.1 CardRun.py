__author__ = 'JimberXin'
"""
	Description: debt account system, calculate the transfer records.
	Output: @carddata.txt: input file system, records the card data
			@cardlog.txt:  output of the log, records the process
"""


def safe_float(obj):
	"""save version of float()"""
	try:
		ret = float(obj)
	except (ValueError, TypeError), diag:
		ret = str(diag)
	return ret


def file_input():
	fobj = open('cardData.txt', 'w')
	str = """previous balance
25
debits
21.64
541.24
25
credits
-25
-541.24
finance charge/late fees
7.30
5
"""
	fobj.write(str)


def main():
	"""handles oll the data processing"""
	file_input()   # generate data in the carddata.txt
	log = open('cardlog.txt', 'w')
	try:
		ccfile = open('carddata.txt', 'r')
	except IOError, e:
		log.write('no data exchange this month\n')
		log.close()
		return
	text = ccfile.readlines()   # read all the lines in the carddata.txt
	ccfile.close()
	total = 0.00
	log.write('account log:\n')

	for each_line in text:
		result = safe_float(each_line)
		if isinstance(result, float):
			total += result
			log.write('data...processed successfully \n')
		else:
			log.write('ignored: %s' % result)

	print '%.2f (new balance)' % total
	log.close()


if __name__ == '__main__':
	main()