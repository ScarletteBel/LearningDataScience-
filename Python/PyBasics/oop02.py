#working with built in class attributes
class Vehicle:
	pass
class Car(Vehicle):
	' this subclass has a superclass'
	pass
#accessing buit-in class attributes
print ("Car.__doc__:", Car.__doc__)
print ("Car.__name__:", Car.__name__)
print ("Car.__module__:", Car.__module__)
print ("Car.__bases__:", Car.__bases__)
print ("Car.__dict__:",Car.__dict__)