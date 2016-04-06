def getMaxMinAvg(numbers):
	"""
	This function calculates minimum, maximum and average
	values of the passing list in this function and returns 
	as result dictionary.
	If passing list is empty each value of the element of 
	the dictionary would receive the value `None`.
	"""
	if not len(numbers): # if list is empty function returns results values `None` 
		return {'max':None, 'min':None, 'avg':None}
	# initialization `min` and `max` with the first value of the numbers and `avg` with 0
	result = {'max':numbers[0], 'min':numbers[0], 'avg':0}
	# calculate result if list is not empty
	for item in numbers:
		result['avg'] += item
		if item < result['min']: result['min'] = item
		if item > result['max']: result['max'] = item
	result['avg'] = result['avg'] / len(numbers)
	return result

def isPalindrom(phrase):
	"""This function returns `true` if passing string is palindrom, 
	otherwise returns `false`"""
	excep = (' ', ',', '.', '!', '?', ':', ';') # exceptions signs
	# this cycle excepts some useless signs from phrase
	for symb in excep: 
		phrase = phrase.replace(symb,'')
	# next cycle of code returns `false` if phrase isn`t palindrom
	for item in range(int(len(phrase) / 2) - 1):
		if phrase[item].lower() != phrase[len(phrase) - 1 - item].lower(): return False
	return True

def reverseString(phrase):
	"""This function reverses passing string"""
	result = ""
	for item in range(len(phrase)):
		result = result + phrase[len(phrase) - 1 - item]
	return result