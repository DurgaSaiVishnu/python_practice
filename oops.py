# class Vehicle:
#     pass

# print(Vehicle)


# class Vehicle:
#     def __init__(self,max_speed,mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

# car = Vehicle(250,18)
# print(car.mileage)
# print(car.max_speed)


# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length*self.width
#     def Perimeter(self):
#         return 2*(self.length+self.width)

    

# rect  = Rectangle(10,4)
# print(rect.Perimeter())


# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def average(self):
#         sum = 0
#         for mark in self.marks:
#             sum+=mark
#         return sum/len(self.marks)

# s1 = Student("Alice",[85, 90, 78, 92, 88])
# print(f"{s1.name}'s average grade: {s1.average()}")


# class Product:
#     def __init__(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def total_value(self):
#         return f"Total stock value of {self.name}: ${self.price*self.quantity}"

# p1 = Product("Laptop", 899.99, 5)
# print(p1.total_value())


# class BankAccount:
#     def __init__(self,balance):
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance += amount
#         return self.balance
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance -= amount
#             return self.balance
#         else:
#             return "insufficient founds current balance: ",self.balance

        

# person1 = BankAccount(1000)
# deposit = person1.deposit(500)
# print("After deposit",deposit)
# withdraw = person1.withdraw(200)
# print("After withdraw",withdraw)
# trywithdraw = person1.withdraw(2000)
# print(trywithdraw)



# class Light:
#     def turn_on(self):
#         self.is_on = True
#         print("Light is ON")
#     def turn_off(self):
#         self.is_on = False
#         print("Light is OFF")
#     def status(self):
#         print("Status: ON") if self.is_on else print("status: OFF")
  
# light = Light()
# light.turn_off()
# light.status()


# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password
#     def check_passcode(self,passcode):
#         return self.password == passcode 

# u1 =     User("alice", "secure123")

# print(u1.check_passcode("secure123"))
# print(u1.check_passcode("seure123"))


# class Temparature:
#     def __init__(self,celsius):
#         self.celsius = celsius
#     def to_fahrenheit(self):
#         return (self.celsius*9/5)+32
#     def to_kelvin(self):
#         return self.celsius +273.15

# t = Temparature(100)
# print("celsius: ",t.celsius)
# print("fahrenheit",t.to_fahrenheit())
# print("kelvin: ",t.to_kelvin())


# class Notebook:
#     def __init__(self):
#         self.notes = []
#     def add_note(self,note):
#         self.notes.append(note)
#     def show_notes(self):
#         return self.notes

    
# nb = Notebook()
# nb.add_note("Buy groceries")
# nb.add_note("Read a book")
# nb.add_note("Call the doctor")
# print(nb.show_notes())

# class CoffeMachine:
#     def __init__(self,water,coffe,milk):
#         self.water = water
#         self.coffe = coffe
#         self.milk = milk
#     def make_latte(self):
#         if self.water>=200 and self.coffe>=20 and self.milk>=150:
#             print(f"latte made! {self.water-200}ml of water left , {self.coffe-20}g of coffe and {self.milk-150}ml of milk left")
#         else:
#             print("not enough resources to make latte")
    
# machine = CoffeMachine(300,100,200)
# print(machine.make_latte())
    


# class Vehicle:
#     def __init__(self,name,max_speed):
#         self.name = name
#         self.max_speed = max_speed
#     def display(self):
#         return f"Name: {self.name} and Max Speed: {self.max_speed}"

# class Bus(Vehicle):
#     pass

# bus1 = Bus("school bus",120)
# print(bus1.name)
# print(bus1.max_speed)



# class Vehicle:
#     def __init__(self,name):
#         self.name = name
#     def seating_capacity(self,capacity):
#         print(capacity)
    
# class Bus(Vehicle):
#     def seating_capacity(self):
#         super().seating_capacity(50)



# bus = Bus("School Bus")
# bus.seating_capacity()


# class Vehicle:
#     def __init__(self,fare):
#         self.fare = fare
    
# class Taxi(Vehicle):
#     def MaintenanceFee(self):
#         totalfare = self.fare+self.fare*0.10
#         return totalfare

# car = Taxi(500)
# print(car.MaintenanceFee())

# class Animal:
#     def speak(self):
#         return "animal sound"

# class Dog(Animal):
#     def speak(self):
#         return "woof"
# class Cat(Animal):
#     def speak(self):
#         return "meow"

# # dog = Dog()
# # print(dog.speak())


# class employee:
#     def __init__(self,name):
#         self.name = name
#     def calculate_pay(self):
#         return 0

# class FullTimeEmployee(employee):
#     def __init__(self,name,annual_pay):
#         super().__init__(name)
#         self.pay = annual_pay
#     def calculate_pay(self):
#         return self.pay/12

# class PartTimeEmployee(employee):
#     def __init__(self,name,hourly_rate,hours_worked):
#         super().__init__(name)
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked
#     def calculate_pay(self):
#         return self.hours_worked*self.hourly_rate


    
# ft = FullTimeEmployee("Alice", 60000)
# pt = PartTimeEmployee("Bob", 500, 20)

# print(ft.calculate_pay())
# print(pt.calculate_pay())



# class Shape:
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return f"{3.14159*self.radius**2:.2f}"

# class Square(Shape):
#     def __init__(self,side):
#         self.side = side
#     def area(self):
#         return self.side**2

# circle = Circle(7)
# print(circle.area())

# square = Square(4)
# print(square.area())


# class Media:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def describe(self):
#         return f"name: {self.name} and rupees {self.price}"

# class Book(Media):
#     def __init__(self,name,price,author):
#         super().__init__(name,price)
#         self.author = author
    
#     def describe(self):
#         return f"book: {self.name} by {self.author} and rupees - {self.price}"

# class Magazine(Media):
#     def __init__(self,name,price,frequency):
#         super().__init__(name,price)
#         self.frequency = frequency
#     def describe(self):
#         return f"magazine: {self.name} ({self.frequency}) - Rs.{self.price}"

# class DVD(Media):
#     def __init__(self,name,price,time):
#         super().__init__(name,price)
#         self.time = time
#     def describe(self):
#         return f"DVD: {self.name},{self.time} - {self.price}"

# book =  Book("Clean Code", 499, "Robert C. Martin")
# print(book.describe())

# class Order:
#     def __init__(self,OrderNo,price):
#         self.OrderNo = OrderNo
#         self.price = price
#     def TotalAmount(self):
#         return f"{self.OrderNo}-{self.price}"

# class DiscountedOrder(Order):
#     def __init__(self,OrderNo,price):
#         super().__init__(OrderNo,price)
#     def TotalAmount(self):
#         return f"{self.price - self.price*0.10}"

# order = DiscountedOrder("ORD001", 1200)
# print("origanl ID: ",order.OrderNo)
# print("origanl price: ",order.price)
# print("after  price: ",order.TotalAmount())


# class Vehicle:
#     def __init__(self,name,max_speed):
#         self.name = name
#         self.max_speed = max_speed
#     def describe(self):
#         pass

# class Bike(Vehicle):
#     def __init__(self,name,max_speed):
#         super().__init__(name,120)
#     def describe(self):
#         return f"Bike max speed : {self.max_speed}km/h"


# class Truck(Vehicle):
#     def __init__(self,name,max_speed):
#         super().__init__(name,90)
#     def describe(self):
#         return f"Truck max speed : {self.max_speed}km/h"

# truck = Bike("bob",50)
# print(truck.describe())



# class Dog:
#     pass

# d =  Dog()
# print(type(d).__name__)


# class Vector:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __add__(self,other):
#         return self.x + other.x,self.y + other.y

# vector1 = Vector(2,3)
# vector2 = Vector(4,1)
# print(vector1+vector2)









