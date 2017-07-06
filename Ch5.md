5.1
```
def mystat():
	sum = 0
	count = 0
	
	while True:
		number = raw_input('Enter Your Number:')

		if number == 'done':
			print 'Sum:', sum, 'Count:', count,'Average:', ave
			break
		else: 
			try:
			    number = float(number)
			    sum = sum+number
			    count = count +1
			    ave = sum/count
			except:
			    print 'Error, please enter numeric input'
			    continue

mystat()
```

5.2
```
def max_min ():
	nums = []
	
	while True:
		get_num = raw_input("Please enter your numbers:")

		if get_num == 'done':
			print 'Done!'
			break
		else:
			try:
				nums.append(float(get_num))
				print max(nums), min(nums)
			except:
				print 'Error, please enter numeric input'
				continue

max_min()
```
