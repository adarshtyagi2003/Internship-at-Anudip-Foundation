class student:
    name="xyz"
    age=0
    def study(self):
        print("study 3 hour",self.name)
        self.sleep() 
                             #self is used to call methods and members of the own class 

    def sleep(self):
        print("sleep 1 hour")


obj=student()
obj.study()



#inheritance 

class a:
    def show(self):
        print("this is show method")


class b(a):
    def demo(self):
        print("demo method")

class c(a):
    pass

class d(b,c):
    pass

obj=c() 
obj.show()
#obj.demo()    #error because c does not have demo




#method overloading does not support in python 

def sum(a,b,c=0):
    print(a+b+c)

sum(10,20,30)
sum(10,20)


'''Polymorphism lets us define methods in the child class that have the same name as the methods
in the parent class. In inheritance, the child class inherits the methods from the parent class. However,
it is possible to modify a method in a child class that it has inherited from the parent class. 
This is particularly useful in cases where the method. Inherited from the parent class doesn't quite fit the child class.
In such cases, we re-implement the method in the child class. 
This process of re-implementing a method in the child class is known as Method Overriding'''


class bird:
    def intro(self):
        print("there are many types of birds")

    def flight(self):
        print("most of the birds can fly but some cannot.")

class sparrow(bird):
    def flight(self):
        print("i can fly")

class ostrich(bird):
    def flight(self):
        print("i cannot fly")

class papakipari(bird):
    def flight(self):
        print("always fly")


obj=bird()
obj.intro()
obj1=papakipari()
obj1.flight()



class a:
    __name="xyz"  #__="private"    #_="protected"
class b(a):
     def show(self):
        print("this is show method",self.name)

obj=b()
obj.show()

