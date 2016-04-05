def getMaxMinAvg(data):
	"""
	This function calculates minimum, maximum and average
	values of the passing list in this function and returns 
	as result dictionary.
	If passing list is empty each value of the element of 
	the dictionary would receive the value `None`.
	"""

	maximum = minimum = average = None

	if not len(data): # if list is empty function returns results data with value `None` 
		return {'max':maximum, 'min':minimum, 'avg':average}
	# initialization `minimum` and `maximum` with the first value of the list
	maximum = minimum = data[0]
	average = 0 # initialization starts value of the `average`
	# calculate result if list is not empty
	for item in data:
		average += item
		if item < minimum: minimum = item
		if item > maximum: maximum = item
	average = average / len(data)

	return {'max':maximum, 'min':minimum, 'avg':average}

def isPalindrom(data):
	"""This function returns `true` if passing string is palindrom, 
	otherwise returns `false`"""
	excep = (' ', ',', '.', '!', '?', ':', ';') # exceptions signs
	for symb in excep: # this cycle excepts some signs 
		data = data.replace(symb,'')
	return data.lower() == data[::-1].lower()

def reverseString(data):
	"""This function reverses passing string"""
	return data[::-1]