# is_valid_date.py

'''
Have you ever wanted to simply validate a date string?  Strangely, the datetime 
module does not export such a function.  Here is a function that you could use.  
If need be, change the default format string to what is likely to occur most 
often.

Of course, the datetime module does need to validate dates to be able to do its 
work, but the function it uses cannot be imported from the module.  Also, 
it does it using the three integer arguments after they have separated from the 
date string.  That function also relies on other functions and constants in the 
module.
'''


from datetime import datetime


def is_valid_date(date_text, format='%Y-%m-%d'):
	try:
		datetime.strptime(date_text, format)
		return True
	except ValueError:
		return False


#testing
print(is_valid_date('2003-12-23'))  # True
print(is_valid_date('2003-12-32'))  # False
print(is_valid_date('2003/12/23', format='%Y/%m/%d'))  # True

