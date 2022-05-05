# [Types of Variables in a Class in Python](https://dotnettutorials.net/lesson/class-variables-in-python/)
# TODO: incomplete
# TODO: separate out instance, static, local variables

#    Instance variables (object level variables)
#    Static variables (class level variables)
#    Local variables


# Instance Variables in Python
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def TODO():
        print("TODO:")


s1 = Student("Nitya", 1)
s2 = Student("Anushka", 2)
print("Studen1 info:")
print("Name: ", s1.name)
print("Id : ", s1.id)
print("Studen2 info:")
print("Name: ", s2.name)
print("Id : ", s2.id)


# Where instance variables can be declared?
# By using a constructor.
# By using instance methods.
# By using object name

# CONSTRUCTOR
class Employee:
    def __init__(self):
        self.eno = 1
        self.ename = "Nithya"
        self.esal = 100


e = Employee()
print("Employee number: ", e.eno)
print("Employee name: ", e.ename)
print("Employee salary: ", e.esal)
print(e.__dict__)


# INSTANCE METHOD
class Student2:
    def m1(self):
        self.a = 11
        self.b = 21
        self.c = 34
        print(self.a)
        print(self.b)
        print(self.c)


s = Student2()
s.m1()
print(s.__dict__)


# USE OBJECT NAME
class Test:
    def __init__(self):
        print("This is constructor")

    def m1(self):
        print("This is instance method")


t = Test()
t.m1()
t.a = 10
t.b = 20
t.c = 55
print(t.a)
print(t.b)
print(t.c)
print(t.__dict__)

# Accessing instance variables in Python

#    By using self variable
#    By using object name


# Accessing with self


class Student3:
    def __init__(self):
        self.a = 10
        self.b = 20

    def display(self):
        print(self.a)
        print(self.b)


s3 = Student3()
s3.display()


# Access by object name


class Student4:
    def __init__(self):
        self.a = 10
        self.b = 20


t = Student4()
print(t.a)
print(t.b)


# Static Variables in Python
class Student_Static:
    college_name = "GITAM"

    def __init__(self, name, id):
        self.name = name
        self.id = id


s1 = Student_Static("Nithya", 1)
s2 = Student_Static("Anushka", 2)
print("Studen1 info:")
print("Name: ", s1.name)
print("Id : ", s1.id)
print("College name n : ", Student_Static.college_name)
# or 
print("College name n : ", s1.college_name)
print("\n")
print("Studen2 info:")
print("Name: ", s2.name)
print("Id : ", s2.id)
print("College name : ", Student_Static.college_name)
# or
print("College name n : ", s1.college_name)






# Declaring static variables in Python - Changes scope of variable
# Inisde Class 
class Demo:
   a=20
   def m(self):
       print("this is method")
print(Demo.__dict__)


# Inside CONSTRUCTOR
class Demo:
  
   def __init__(self):
       Demo.b=20
d = Demo()
print(Demo.__dict__)


# Inside Instance METHOD
class Demo:
  
   def m1(self):
       Demo.b=20
obj=Demo()
obj.m1()
print(Demo.__dict__)

# INSIDE CLASSMETHOD
class Demo:
   @classmethod
   def m2(cls):
       Demo.b=30
obj=Demo()
obj.m2()
print(Demo.__dict__)

# static variable inside class method with class parameter
class Demo:
   @classmethod
   def m2(cls):
       cls.b=30
obj=Demo()
obj.m2()
print(Demo.__dict__)

# STATIC METHOD - STATIC VARIABLE
class Demo:
   @staticmethod
   def m3():
       Demo.z=10
Demo.m3()
print(Demo.__dict__)



# Accessing a static variable in Python
# Local Variables in Python
