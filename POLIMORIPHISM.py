class Animal:
      def __init__(self,name):
          self.a=name
class Cat(Animal):
      def talk(self):
          return "meow"
        
class Dog(Animal):
      def talk(self):
          return "woof"


list1=[Cat("sonia"),Dog("abhishek"),Cat("riya"),Dog("himanshu")]
for x in list1:
    print(x.a,"-",x.talk())
