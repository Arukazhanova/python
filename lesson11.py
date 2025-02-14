# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def print_person(self):
#         print(f"Name:{self.name}")
#         print(f"Age:{self.age}")
        
# tom=Person("Tom",23)
# tom.print_person()

# class Person:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def print_person(self):
#         print(f"Name:{self.__name}")
#         print(f"Age:{self.__age}")
        
# tom=Person("Tom",23)
# tom.__name="Spider man"
# tom.__age=-129
# tom.print_person()



# class Person:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def print_person(self):
#         print(f"Name:{self.__name}")
#         print(f"Age:{self.__age}")
        
# tom=Person("Tom",23)
# tom._Person__name="Spider man"
# tom._Person__age=-129
# tom.print_person()

# class Person:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
        
#     def set_age(self,age):
#         if 0<age<110:
#             self.__age=age
#         else:
#             print("Incorrect age")
#     def get_age(self):
#         return self.__age
    
#     def get_name(self):
#         return self.__name
    
#     def print_person(self):
#         print(f"Name:{self.__name}")
#         print(f"Age:{self.__age}")

# tom=Person("Tom",23)
# tom.print_person()
# tom.set_age(-56789)
# tom.set_age(25)
# tom.print_person()

# class Person():
#     def __init__(self,name):
#         self.__name=name
        
#     @property
#     def name(self):
#         return self.__name
    
#     def display_info(self):
#         print(f"Name:{self.name}")   
# class Employee(Person):
#     def work(self):
#         print(f"{self.name} is working")
    
# tom=Employee("Tom")
# print(tom.name)
# tom.display_info()
# tom.work()








        