#working with overriding methods in Python
class SchoolMember:
	'Represents any school member.'
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Initialized SchoolMember: {})'.format(self.name))
	def tell(self):
		'Tell my details.'
		print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")
class Teacher(SchoolMember):
	'Represents a teacher.'
	def __init__(self, name, age, salary):# overriding SchoolMember init method
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print('(Initialized Teacher: {})'.format(self.name))
	def tell(self): # overriding SchoolMember tell method
		#SchoolMember.tell(self)
		print('Salary: "{:d}"'.format(self.salary))
		print(self.name)
		
class Student(SchoolMember):
	'Represents a student.'
	def __init__(self, name, age, marks):# overriding SchoolMember tell method
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('(Initialized Student: {})'.format(self.name))
	def tell(self): # overriding SchoolMember tell method
		#self.tell()
		print('Marks: "{:d}"'.format(self.marks))
		print(self.name)
		
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
# prints a blank line
print()
t.tell()
s.tell()
#members = [t, s]
#for member in members:
	# Works for both Teachers and Students
	#member.tell()