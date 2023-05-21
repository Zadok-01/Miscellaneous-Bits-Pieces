# range_float.py

'''
Have you ever needed a "range" function that handled floats.  Well, here's one.  
The arguments work the same as for the built-in range function.  You may get 
some strange looking output from time to time, but that will only be the 
dreaded floating point rounding.  Do not be tempted to save one line of code 
by successively adding the step value at each cycle of the loop; if you do any 
rounding errors will accumulate.
'''


def range_float(start, stop=None, step=1):
	if stop is None:
		start, stop = 0, start
	cond = 'val < stop' if step > 0 else 'val > stop'
	k, val = 0, start
	while eval(cond):
		yield val
		k += 1
		val = start + k * step


# testing
print(list(range_float(3, 5, .3)))
print(list(range_float(8, 6, -.2)))
print(list(range_float(1/3, 5/8, 1/10)))
print(list(range_float(7/8, 1/4, -1/10)))

