class Rectangle:
	def __init__(self, length, width):
		self.Area=length*width
		self.Perimeter=2*(length*width)
	def getArea(self):
		return (self.Area)
	def getPerimeter(self):
		return (self.Perimeter)
	
R1=Rectangle(2,3)
R2=Rectangle(4,5)
R3=Rectangle(6,7)
print(R1.getArea(),R1.getPerimeter())
print(R2.getArea(),R2.getPerimeter())
print(R3.getArea(),R3.getPerimeter())
