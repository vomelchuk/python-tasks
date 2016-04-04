# This module using Python 3 intepreter

from get_max_min_avg import getMaxMinAvg

arr = [] # create empty list

# this section fills list
while True:
	numb = input('Input number (to break type \'exit\'): ')
	if numb == 'exit': break # end of filling list
	if numb.isalpha() or not len(numb): continue # ignoring non-numerical data
	arr.append(float(numb))

print () # separator between incoming datas and result
print ('You have inputed:',arr)
result = getMaxMinAvg(arr)
for item in result.keys():
	print(item,'=',result[item])


		