#working with class variables
class Student:
	'Common base class for all students'
	stuCounter = 0

	def __init__(self, name, mark):
		self.name = name
		self.mark = mark
		Student.stuCounter += 1
	
	
	def dispStudent(self, age):
		self.age=age
		print ("Student : ", self.name,  ", Mark: ", self.mark, ", Age: ", self.age)


#creating a first object of Student class
student1 = Student("John", 91)
#creating a second object of Student class
student2 = Student("Diana", 94)

student1.dispStudent(45)
student2.dispStudent(41)
print("student name",student1.name)
print("student name",student2.name)

print ("Total number of students %d" % Student.stuCounter)
print (student1.stuCounter)
print (student2.stuCounter)# it prints 2 because stuCounter is a class var
print ("test ",Student.stuCounter)
#print (stuCounter)# error name is not defined
print (student1.name)# it only prints student1 name because name is an instnce var of student1, the current instance
print (student1.mark)
print (student1.age)
print (student2.name)
print (student1.__dict__)
print (student2.__dict__)