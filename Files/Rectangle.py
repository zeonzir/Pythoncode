class Rectangle:
	def __init__(self, length, width):
		self.Length=length
		self.Width=width
	def Area(self):
		return (self.Length*self.Width)
	def Perimeter(self):
		return (2*(self.Length+self.Width))
	
R1=Rectangle(2,3)
R2=Rectangle(4,5)
R3=Rectangle(6,7)
print(R1.Area(),R1.Perimeter())
print(R2.Area(),R2.Perimeter())
print(R3.Area(),R3.Perimeter())