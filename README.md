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
