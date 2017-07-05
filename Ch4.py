4.4 b and c are both true.

4.5 ABC Zap ABC

4.6
def computepay(Hours, Rate):
	try:
		Hours = float(Hours)
		Rate = float(Rate)

		if Hours > 40:
			Pay = 40 * 10 + (Hours - 40) * 1.5 * Rate
		else:
			Pay = Hours * Rate
		return 'Pay:', Pay
	except:
		return 'Error, please enter numeric input'

Hours = raw_input('Enter Hours:')
Rate = raw_input('Enter Rate:')

print computepay(Hours, Rate)

4.7
def computepay(Hours, Rate):
	try:
		Hours = float(Hours)
		Rate = float(Rate)

		if Hours > 40:
			Pay = 40 * 10 + (Hours - 40) * 1.5 * Rate
		else:
			Pay = Hours * Rate
		return 'Pay:', Pay
	except:
		return 'Error, please enter numeric input'

Hours = raw_input('Enter Hours:')
Rate = raw_input('Enter Rate:')

print computepay(Hours, Rate)
