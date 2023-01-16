#working with __init__ method
class Library:
	def __init__(self, name, book):
		self.name = name
		self.book = book
	def borrowme (self):
		print (self.name)
		print(self.book)

	def greeting(self):
		if self.name:
			print('Hello, you are in', self.name, 'library')
		else:
			print ('forgot to provide the library name')

p = Library('Fairview','The Old Man and The Sea')
p.borrowme()
p.greeting()
print()
z=Library('Mississauga','The Mask')
z.greeting()
z.borrowme()



