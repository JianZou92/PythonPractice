7.1
```
def read():
	fname = raw_input('Enter the file name:')
	try:
		fhand = open(fname)
	except:
		print 'File cannot be opened:', fname
		exit()

	for line in fhand.readlines()[:5]:
		line_upper = line.upper()
		print line_upper

read()
```

7.2
```

def find_spam():
	fname = raw_input('Enter the file name:')

	try:
		fhand = open(fname)
		num_sum = 0
		num_count = 0
	except:
		print 'File cannot be opened:', fname
		exit()

	for line in fhand:
		if line.find('X-DSPAM-Confidence') == -1:
			pass
		else:   
			index = line.find(':')
			num = float(line[index+2:])
			num_sum = num_sum + num
			num_count = num_count + 1

	print 'Average spam confidence:', num_sum/num_count

find_spam()
```

7.3
```
def egg():
	fname = raw_input('Enter the file name:')

	if fname == 'na na boo boo':
		print 'NA NA BOO BOO TO YOU - You have been punl`d!'

	else:
		try:
			fhand = open(fname)
			count = 0

			for line in fhand:
				if line.find('Subject:') == -1:
					pass
				else:   
					count = count + 1
			print 'There were', count, 'subject lines in', fname
	
		except:
			print 'File cannot be opened:', fname
			exit()

egg()
```
