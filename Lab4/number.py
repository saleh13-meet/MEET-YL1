class Integer(object):
	def __init__(self, OneVariable, TOF):
		self.OneVariable = OneVariable
		self.TOF = TOF

	def Display(self):
		if self.TOF == True:
			return self.OneVariable * -1
		else:
			return self.OneVariable

class NegativeInteger(Integer):
	def __init__(self, n):
		super(NegativeInteger, self).__init__(n, True)
	def Display(self):
		return str(Integer.Display(self)) + " This is an object of the NegativeInteger class"
		

if __name__=="__main__":
	test = Integer(10, True)
	test2 = NegativeInteger(10)
	print test.Display()
	print test2.Display()