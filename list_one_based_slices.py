# list_one_based_slices.py

# One-based list including support for slices

'''
Have you wondered whether it is possible to have one-based lists in Python 
(lists whose indices start at one instead onf the usual zero)?

It is unlikely that anyone would seriously need this, so consider this an 
intellectual exercise exploring the feasibility of such a thing.

This class produces a list with support for one-based indices.  These work as 
individual indices and as part of slices.  Zero is considered an invalid index.  
Negative indices work from the end (right hand side) of the list in the 
conventional manner.
'''


class OneList(list):
	'List with one-based indexing'
	
	@staticmethod
	def _fixi(ix):
		'Adust index if positive'
		if ix == 0:
			raise IndexError('Index 0 is invalid')
		return ix - 1 if ix > 0 else ix
	
	def _fixs(self, slc):
		'Adjust slice limits if supplied or insert defaults'
		start = 0 if slc.start is None else self._fixi(slc.start)
		stop = len(self) if slc.stop is None else self._fixi(slc.stop)
		return slice(start, stop, slc.step)
	
	def __setitem__(self, ix, val):
		if type(ix) is int:
			super().__setitem__(self._fixi(ix), val)
		else:
			super().__setitem__(self._fixs(ix), val)
	
	def __getitem__(self, ix):
		if type(ix) is int:
			return super().__getitem__(self._fixi(ix))
		else:
			return super().__getitem__(self._fixs(ix))
	
	def __delitem__(self, ix):
		if type(ix) is int:
			super().__delitem__(self._fixi(ix))
		else:
			super().__delitem__(self._fixs(ix))
	
	def insert(self, ix, val):
		super().insert(self._fixi(ix), val)
	
	def pop(self, ix=-1):
		return super().pop(self._fixi(ix))
	
	def index(self, item, *args):
		return 1 + super().index(item, *args)

