class Employee:
  def __init__(self,id,name):
    self.id=id
    self.name=name
class Salary(Employee):
  def __init__(self,id,name,basic_salary,bonus):
    super().__init__(id,name)
    self.basic_salary=basic_salary
    self.bonus=bonus
  def total_salary(self):
    total=self.basic_salary+self.bonus
    return total
  def display(self):
    print("ID:",self.id)
    print("Name:",self.name)
    print("Basic Salary:",self.basic_salary)
    print("Bonus:",self.bonus)
    print("Total Salary:",self.total_salary())
sal=Salary(101,"Jency",25000,5000)
sal.display()

# output
ID: 101
Name: Jency
Basic Salary: 25000
Bonus: 5000
Total Salary: 30000


class Vehicle:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
class Car(Vehicle):
  def __init__(self,brand,model,fuel_type,seat):
    super().__init__(brand,model)
    self.fuel_type=fuel_type
    self.seat=seat
  def display(self):
    print("Brand:",self.brand)
    print("Model:",self.model)
    print("Fuel Type:",self.fuel_type)
    print("Seat:",self.seat)
car=Car("Toyota","Camry","Petrol",5)
car.display()

# output
Brand: Toyota
Model: Camry
Fuel Type: Petrol
Seat: 5
