# python3

class Object:

	__maximum = None
	__minimum = None
	__average = None

	def __init__(self):
		self.data = []
		
	def add(self, x):
		self.data.append(x)

	def getData(self):
		return self.data
	
	def getMaxMinAvg(self):
		if not len(self.data):return {'Empty list':'no data'}
		self.__minimum = self.data[0]
		self.__maximum = self.data[0]
		self.__average = 0
		for item in self.data:
			self.__average += item
			if item < self.__minimum: self.__minimum = item
			if item > self.__maximum: self.__maximum = item
		self.__average = self.__average / len(self.data)
		return {'max':self.__maximum, 'min':self.__minimum, 'avg':self.__average}


arr = Object()

while True:
	numb = input('Input number (to break type \'exit\'): ')
	if numb == 'exit': break
	if numb.isalpha() or not len(numb): continue
	arr.add(float(numb))

arr.getMaxMinAvg()
print()
print('You have inputed:',arr.getData())
result = arr.getMaxMinAvg()
for item in result.keys():
	print(item,'=',result[item])

		