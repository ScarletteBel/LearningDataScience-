#accessing attributes
class Car:
	' this subclass has a superclass'
	pass
x=Car()
x.make="Toyota"
x.color="white"
x.year="2001"
print (x.color)
print (x.__dict__)
Car.model="Sienna"
print (x.model) # will print Sienna
x.model="Camry"
print (Car.model) #will print Sienna
print (getattr(x, 'model')) #another way to access attributes
setattr(x, 'fuel','diesel') #creating a new attribute associated with a new value
print (getattr(x, 'fuel'))
print (x.__dict__)
delattr (x,'fuel')
print (x.__dict__)
print (hasattr(x, 'fuel'))
setattr(x, 'fuel', 'benzene')
print (x.__dict__)
y=Car()
print ("the color of y is: "+getattr(y, 'color'))
print ("the model of y is: "+getattr(y, 'model'))
print (y.__dict__)
