# def plus():
#     a=[1,2,3,4,5,6,7,8]
#     sum_even=0
#     for i in a:
#         if i%2==0:
#             sum_even+=i
#     print(sum_even)
# plus()
# def min_max():
#     a=[1,2,3,4,5,6]
#     for i in a:
#         max_sum=max(a)
#         min_sum=min(a)
#     print(max_sum)
#     print(min_sum)
# min_max()
# def sum_num():
#     n=int(input("Enter number"))
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     print(sum)
# sum_num()
# def divide():
#     num=int(input("Enter number: "))
#     for i in range(1,11):
#         result=num*i
#         print(f"{num}*{i}={result}")
# divide()
# def rev():
#     text = input("Введите строку: ")
#     text_list = list(text)
#     text_list.reverse()
#     reversed_text = ''.join(text_list) 
#     print(reversed_text) 

# rev()

# def name():
#     string=input("Enter name:")
#     def res():
#         nonlocal string
#     print(f"Hello,my name is,{string}")
#     return res
# greeting = name()  
# greeting()

# def outer():
#     a=input("Reminder: ")
#     def inner():
#         nonlocal a
#         return f"Attention,{a}"
#     return inner
# res=outer()
# print(res())
   
   
   
# a=int(input("Enter number: "))
# b=int(input("Enter number: "))
# try:
#      print(a/b)
# except ZeroDivisionError:
#     print("Error")

# list=[1,2,3,4,56]
# try:
#     x=list[5]
#     print(x)
# except IndexError:
#     print("Not Found")


# try: 
#     a=int(input("Enter number: "))
#     b=int(input("Enter number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Error")
# except ValueError:
#     print("Error Value")

# class Stadium():
#     def __init__(self,name,date_open,country,city,quantity):
#         self.__name=name
#         self.__date_open=date_open
#         self.__country=country
#         self.__city=city
#         self.__quantity=quantity
        
#     def get_name(self):
#         return self.__name
#     def get_date_open(self):
#         return self.__date_open
#     def get_country(self):
#         return self.__country
#     def get_city(self):
#         return self.__city
#     def get_quantity(self):
#         return self.__quantity
    
#     def set_name(self,name):
#         self.__name=name
        
#     def set_date_open(self,date_open):
#         self.__date_open=date_open
        
#     def set_country(self,country):
#         self.__country=country
        
#     def set_city(self,city):
#         self.__city=city
#     def set_quantity(self,quantity):
#         self.__quantity=quantity
        
#     def print_info(self):
#         print(f"Name:{self.__name}")
#         print(f"Date open:{self.__date_open}")
#         print(f"Country:{self.__country}")
#         print(f"City:{self.__city}")
#         print(f"Quantity:{self.__quantity}")
# result=Stadium("Astana Arena","2010","Kazakhstan","Nur-Sultan",30000)
# result.set_name("Saryarka")
# result.set_date_open("2011")
# result.set_country("Kazakhstan")
# result.set_city("Almaty")
# result.set_quantity(20000)
# result.print_info()

# class Phone():
#     def __init__(self,name,made,ram,storage,size,price):
#         self._name = name
#         self._made = made
#         self._ram = ram  
#         self._storage = storage
#         self._size = size
#         self._price = price
#     def discount(self,percent):
#         self._price=self._price-(self._price*percent/100)
#     def print_info(self):
#         print(f"Name:{self._name}")
#         print(f"Made:{self._made}")
#         print(f"RAM:{self._ram}")
#         print(f"Storage:{self._storage}")
#         print(f"Size:{self._size}")
#         print(f"Price:{self._price}")
# result=Phone("Iphone","USA",6,128,"6.1 inch",1000)
# result.print_info()
# result.discount(10)
# result.print_info()



# class Movie():
#     def __init__(self,name,year,director,genre,minutes,rating):
#         self._name=name
#         self._year=year
#         self._director=director
#         self._genre=genre
#         self._minutes=minutes
#         self._rating=rating
        
        
#     def print_info(self):
#         print(f"Name:{self._name}")
#         print(f"Year:{self._year}")
#         print(f"Director:{self._director}")
#         print(f"Genre:{self._genre}")
#         print(f"Minutes:{self._minutes}")
#         print(f"Rating:{self._rating}")
        
#     def calculate_time(movies):
#         result=0
#         for i in movies:
#             result+=i._minutes
#         hours=result/60
#         return hours       
# movie1 = Movie("The Dark Knight", 2008, "Christopher Nolan", "Action", 152, 9.0)
# movie2 = Movie("Inception", 2010, "Christopher Nolan", "Sci-Fi", 148, 8.8)
# movie3 = Movie("Interstellar", 2014, "Christopher Nolan", "Sci-Fi", 169, 8.6)
# movies=[movie1,movie2,movie3]
# movie1.print_info()
# movie2.print_info()
# movie3.print_info()
# print(Movie.calculate_time(movies))


# class University():
#     def __init__(self,name,year,country,city,count_student,count_teacher):
#         self._name=name
#         self._year=year
#         self._country=country
#         self._city=city
#         self._count_student=count_student
#         self._count_teacher=count_teacher
#     def print_info(self):
#         print(f"Name:{self._name}")
#         print(f"Year:{self._year}")
#         print(f"Country:{self._country}")
#         print(f"City:{self._city}")
#         print(f"Count student:{self._count_student}")
#         print(f"Count teacher:{self._count_teacher}")
#     def calculate_average_students_per_teacher(universities):
#         result=0
#         for i in universities:
#             result+=i._count_student/i._count_teacher
#         return result
# university1=University("KBTU",1993,"Kazakhstan","Almaty",10000,500)
# university2=University("KazNU",1934,"Kazakhstan","Almaty",15000,800)
# university3=University("Harvard",1636,"USA","Boston",20000,1000)
# university1.print_info()
# print(University.calculate_average_students_per_teacher([university1]))
    






# def bubble(lst):
#     swap = True
#     while swap:
#         swap = False
#         for i in range(len(lst)-1):
#             if lst[i] > lst[i +1]:
#                 lst[i], lst[i+1] = lst[i+1], lst[i]
#                 swap = True
# arr = []
# for i in range(1,11):
#     a = int(input(f"Введите {i} число "))
#     arr.append(a)
    
# bubble(arr)
# print(arr)
# while True:
#     target = int(input("Enter number for search:"))
#     low, high = 0, len(arr) - 1
#     found = False
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             found = True
#             break
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     if found:
#         print(f"Number found: {target}")
#         break
#     else:
#         print(f"Number not found: {target}")

# class Device():
#     def __init__(self,name,model,price):
#         self.name=name
#         self.model=model
#         self.price=price
#     def display_info(self):
#         print(f"Name:{self.name}")
#         print(f"Model:{self.model}")
#         print(f"Price:{self.price}")
# class CoffeeMachine(Device):
#     def coffee_make(self):
#         print(f"{self.name} is making coffee")
#         print(f"{self.model} is making coffee")
#         print(f"{self.price} is making coffee")
# class Blender(Device):
#     def blender_make(self):
#         print(f"{self.name} is making juice")
#         print(f"{self.model} is making juice")
#         print(f"{self.price} is making juice")
# class MeatGrinder(Device):
#     def meat_make(self):
#         print(f"{self.name} is making meat")
#         print(f"{self.model} is making meat")
#         print(f"{self.price} is making meat")
# coffee=CoffeeMachine("Bosch","TSM6A013B",100)
# blender=Blender("Bosch","MUM4405",200)
# meat=MeatGrinder("Bosch","MFW68660",300)
# coffee.display_info()
# coffee.coffee_make()
# blender.display_info()
# blender.blender_make()
# meat.display_info()
# meat.meat_make()

# class Ship():
#     def __init__(self,name,year,country):
#         self.name=name
#         self.year=year
#         self.country=country
#     def display_info(self):
#         print(f"Name:{self.name}")
#         print(f"Year:{self.year}")
#         print(f"Country:{self.country}")
# class Frigate(Ship):
#     def frigate_make(self):
#         print(f"{self.name} is making frigate") 
#         print(f"{self.year} is making frigate")
#         print(f"{self.country} is making frigate")
# class Destroyer(Ship):
#     def destroyer_make(self):
#         print(f"{self.name} is making destroyer") 
#         print(f"{self.year} is making destroyer")
#         print(f"{self.country} is making destroyer")
# class Cruiser(Ship):
#     def cruiser_make(self):
#         print(f"{self.name} is making cruiser") 
#         print(f"{self.year} is making cruiser")
#         print(f"{self.country} is making cruiser")
# frigate=Frigate("Frigate",1990,"USA")
# destroyer=Destroyer("Destroyer",2000,"Russia")
# cruiser=Cruiser("Cruiser",2010,"China")
# frigate.display_info()
# frigate.frigate_make()
# destroyer.display_info()
# destroyer.destroyer_make()
# cruiser.display_info()
# cruiser.cruiser_make()

# lst=[1,2,3,4,5,6,7]
# result=0
# for i in lst:
#     result+=i
# print(result)

# lst=[1,2,3,4,5,6,7]
# res=0
# for i in lst:
#     res=min(lst)
# print(res)
# num=61
# if num<=0:
#     print(False)
# else:
#     while num>1:
#         num=num/2
#     if num==1:
#          print(True)
#     else:
#         print(False)

# lst1=[1,2,3,4,5,6,7]
# lst2=[6,7,1,8,9,10]
# res=0
# for i in lst1:
#     if i in lst2:
#         res+=1
# print(res)
# lst1=[1,2,2,3,4,5,5,6,7]
# res={}
# for i in lst1:
#     if i in res:
#         res[i]+=1
#     else:
#         res[i]=1
# print(res)

# Определение регистров
# PC = 0  # Program Counter
# AC = 0  # Accumulator
# IR = None  # Instruction Register
# MAR = 0  # Memory Address Register
# MBR = 0  # Memory Buffer Register

# # Память для инструкций и данных
# memory = [
#     ("0010", 3),  # Load AC from device 3
#     ("0101", 340),  # Add contents of memory 340
#     ("1000", 7)  # Store AC to device 7
# ]

# # Данные памяти
# data_memory = {340: 7}  # Значение 7 по адресу 340
# io_devices = {3: 1, 7: None}  # Устройство 3 дает значение 1

# # Процессорная функция
# def execute_instruction():
#     global PC, AC, IR, MAR, MBR
#     while PC < len(memory):
#         # Чтение инструкции из памяти
#         IR, MAR = memory[PC]
#         PC += 1
#         if IR == "0010":  # Load AC from I/O
#             MBR = io_devices[MAR]
#             AC = MBR
#         elif IR == "0101":  # Add contents of memory
#             MBR = data_memory.get(MAR, 0)
#             AC += MBR
#         elif IR == "1000":  # Store AC to I/O
#             io_devices[MAR] = AC

#         # Печать состояния регистров
#         print(f"PC: {PC}, IR: {IR}, MAR: {MAR}, MBR: {MBR}, AC: {AC}")

# execute_instruction()
# class Processor:
#     def __init__(self):
#         self.AC = 0  # Accumulator
#         self.PC = 0  # Program Counter
#         self.MAR = 0  # Memory Address Register
#         self.MBR = 0  # Memory Buffer Register
#         self.memory = [0] * 4096  # Memory
#         self.IO = [0] * 16  # I/O devices

#     def load_ac_from_io(self, device):
#         self.MAR = device
#         self.AC = self.IO[self.MAR]

#     def add_memory(self, address):
#         self.MAR = address
#         self.MBR = self.memory[self.MAR]
#         self.AC += self.MBR

#     def store_ac_to_io(self, device):
#         self.MAR = device
#         self.IO[self.MAR] = self.AC

#     def execute_program(self):
#         self.load_ac_from_io(3)
#         print(f"Step 1: AC = {self.AC}")
#         self.add_memory(340)
#         print(f"Step 2: AC = {self.AC}")

    
#         self.store_ac_to_io(7)
#         print(f"Step 3: IO[7] = {self.IO[7]}")


# processor = Processor()
# processor.IO[3] = 1 
# processor.memory[340] = 7  

# processor.execute_program()
# class User:
#     def __init__(self, name, email, number):
#         self.name = name
#         self.email = email
#         self.number = number

# class Notifier:
#     def send_notification(self, user, message):
#         return NotImplementedError("Error")

# class EmailNotifier(Notifier):
#     def send_notification(self, user, message):
#         print(f"Email for {user.email}: {message}")

# class SMSNotifier(Notifier):
#     def send_notification(self, user, message):
#         print(f"SMS for {user.number}: {message}")

# class NotificationService:
#     def __init__(self, notifier):
#         self.notifier = notifier

#     def notify(self, user, message):
#         self.notifier.send_notification(user, message)
# user1 = User("Aruzhan", "aruzhan@example.com", "+7774756")

# email_service = NotificationService(EmailNotifier())
# email_service.notify(user1, "Email send!")

# sms_service = NotificationService(SMSNotifier())
# sms_service.notify(user1, "Sms send!")


