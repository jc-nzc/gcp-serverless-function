#class Person:
#  def __init__(self, name, age):
#    self.name = name
#    self.age = age

#  def myFunc(self):
#    print("My age is {}".format(self.age))

#p1 = Person("Jorge", 34)
#p1.myFunc()	

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("and my age is {}".format(self.age))

p1 = Person("John", 36)
p1.myfunc()
