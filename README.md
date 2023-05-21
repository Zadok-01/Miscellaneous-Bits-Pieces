# Miscellaneous Bits and Pieces
A collection of small items generally produced in response to requests by others.

## Range with Floats
### (range_float.py)
Have you ever needed a "range" function that handled floats.  Well, here's one.  
The arguments work the same as for the built-in range function.  You may get 
some strange looking output from time to time, but that will only be the 
dreaded floating point rounding.  Do not be tempted to save one line of code 
by successively adding the step value at each cycle of the loop; if you do any 
rounding errors will accumulate.

## Date String Validation
### (is_valid_date.py)
Have you ever wanted to simply validate a date string?  Strangely, the datetime 
module does not export such a function.  Here is a function that you could use.  
If need be, change the default format string to what is likely to occur most 
often.

Of course, the datetime module does need to validate dates to be able to do its 
work, but the function it uses cannot be imported from the module.  Also, 
it does it using the three integer arguments after they have separated from the 
date string.  That function also relies on other functions and constants in the 
module.
