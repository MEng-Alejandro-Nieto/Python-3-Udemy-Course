# create a class that accept coordinates as a pair of tuples and return the slope and distance of the lines

class Geometry():
	def __init__(self,c1,c2):
		self.c1=c1
		self.c2=c2

	def distance(self):
		x=self.c2[0]-self.c1[0]
		y=self.c2[1]-self.c1[1]
		return (x**2+y**2)**0.5
	def slope(self):
		x=self.c2[0]-self.c1[0]
		y=self.c2[1]-self.c1[1]
		return y/x
c1=(3,2)
c2=(8,10)
b=Geometry(c1,c2)
print(b.distance())
print(b.slope())

# create a class to calculate the volume of a cylinder and the surface area of a cylinder

class Cylinder():
	def __init__(self,radius,height):
		self.radius=radius
		self.height=height
	
	def volume(self):
		return 3.14159*self.radius**2*self.height
	
	def surface(self):
		return 2*(3.14159*self.radius**2)+(2*3.14159*self.radius*self.height)

my_cylinder=Cylinder(3,2)
print(my_cylinder.volume())
print(my_cylinder.surface())










