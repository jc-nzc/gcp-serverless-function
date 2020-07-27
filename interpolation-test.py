class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myFunc(self):
    print("My age is {}".format(self.age))

p1 = Person("Jorge", 34)
p1.myFunc()	
