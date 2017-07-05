3.1
```
Hours = raw_input('Enter Hours:')
Rate = raw_input('Enter Rate:')

Hours = float(Hours)
Rate = float(Rate)
Pay = Hours * Rate

if Hours > 40:
    Pay = 40 * 10 + (Hours - 40) * 1.5 * Rate

print 'Pay:', Pay
```
3.2
```
Hours = raw_input('Enter Hours:')
Rate = raw_input('Enter Rate:')

try:
    Hours = float(Hours)
    Rate = float(Rate)
    Pay = Hours * Rate

    if Hours > 40:
        Pay = 40 * 10 + (Hours - 40) * 1.5 * Rate

    print 'Pay:', Pay

except:
    print 'Error, please enter numeric input'
```
3.3
```
Score = raw_input('Enter Score (should be between 0.0 and 1.0):')

try:
    Score = float(Score)
    
    if Score > 1.0 or Score < 0.0 :
        Grade = 'Bad score'
    elif Score >= 0.9:
	Grade = 'A'
    elif Score >= 0.8:
	Grade = 'B'
    elif Score >= 0.7:
	Grade = 'C'
    elif Score >= 0.6:
	Grade = 'D'
    elif Score < 0.6:
	Grade = 'F'

    print Grade

except:
    print 'Bad score'
```
