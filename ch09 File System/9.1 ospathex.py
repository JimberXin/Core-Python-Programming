__author__ = 'JimberXin'

import os

# judge whether Unix(Linux or Mac OS) or Windows
for tmpdir in ('/tmp', r'c: \temp'):
	if os.path.isdir(tmpdir):
		break

else:
	print 'no such temp directory exist'
	tmpdir = ''

if tmpdir:
	# change current directory, get it and print it
	os.chdir(tmpdir)
	cwd = os.getcwd()
	print '=' * 40
	print 'current temporary directory'
	print cwd

	# create new directory, get it and print it
	print '=' * 40
	print 'creating example directory'
	os.mkdir('example')
	os.chdir('example')
	cwd = os.getcwd()
	print cwd

	# before adding new file, list the empty dir
	print '=' * 40
	print 'original directory listing'
	print os.listdir(cwd)

	# after adding new file, list the file in the dir
	print '=' * 40
	print 'creating test file...'
	fobj = open('test', 'w')
	fobj.write('this\n')
	fobj.write('is just\n')
	fobj.write('a test\n')
	fobj.close()
	print '=' * 40
	print 'update directory listing:'
	print os.listdir(cwd)

	# list the file after renaming.
	print '=' * 40
	print "renaming 'test' to 'filetest.txt' "
	os.rename('test', 'filetest.txt')
	print '=' * 40
	print 'update directory listing after renaming'
	print os.listdir(cwd)

	# print different tpye of filename
	path = os.path.join(cwd, os.listdir(cwd)[0])
	print '=' * 40
	print 'full file pathname'
	print path
	print '=' * 40
	print '(pathname, basename) == '
	print os.path.split(path)
	print '=' * 40
	print '(filename, extension)== '
	print os.path.splitext(os.path.basename(path))

	# print file content
	print '=' * 40
	print 'displaying file contents: '
	fobj = open(path)
	for each_line in fobj:
		print each_line,
	fobj.close()

	# print file and directory
	print '=' * 40
	print 'deleting test file'
	os.remove(path)
	print '=' * 40
	print 'update directory listing '
	print os.listdir(cwd)
	os.chdir(os.pardir)
	print '=' * 40
	print 'deleting test directory'
	os.rmdir('example')
	print '=' * 40
	print 'Done.'

