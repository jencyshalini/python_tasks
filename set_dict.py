# Set

numbers = set()
for i in range(10):
  num = int(input("Enter a number: "))
  numbers.add(num)
print("Unique Numbers:", numbers)  
numbers.add(100)
print("After adding:", numbers)
numbers.discard(10)
print("After removing:", numbers)
check = int(input("Enter a number to check: "))
if check in numbers:
    print(check, "exists in the set")
else:
    print(check, "does not exist in the set")
numbers2 = {10, 20, 30, 40, 50}
print("Second Set:", numbers2)
print("Union:", numbers.union(numbers2))
print("Intersection:", numbers.intersection(numbers2))
print("Difference:", numbers.difference(numbers2))
print("Total Unique Elements:", len(numbers))

# Outpur
Enter a number: 76
Enter a number: 98
Enter a number: 45
Enter a number: 87
Enter a number: 24
Enter a number: 11
Enter a number: 22
Enter a number: 87
Enter a number: 93
Enter a number: 94
Unique Numbers: {98, 11, 76, 45, 22, 87, 24, 93, 94}
After adding: {98, 100, 11, 76, 45, 22, 87, 24, 93, 94}
After removing: {98, 100, 11, 76, 45, 22, 87, 24, 93, 94}
Enter a number to check: 22
22 exists in the set
Second Set: {50, 20, 40, 10, 30}
Union: {98, 100, 40, 10, 11, 76, 45, 50, 20, 30, 22, 87, 24, 93, 94}
Intersection: set()
Difference: {98, 100, 11, 76, 45, 22, 87, 24, 93, 94}
Total Unique Elements: 10


# dictionary

employee = {"employee_id": 101,"name": "Jency","age": 21,"department": "IT","salary": 25000}
print("Employee Details:", employee)
print("Employee Name:", employee["name"])
print("Employee Salary:", employee["salary"])
employee["experience"] = "1 Year"
print("After Adding Experience:", employee)
employee["salary"] = 30000
print("Updated Salary:", employee["salary"])
employee.pop("age")
print("After Removing Age:", employee)
print("Keys:", employee.keys())
print("Values:", employee.values())
print("Employee Information:")
for key, value in employee.items():
  print(key, ":", value)
if "department" in employee:
  print("Department key exists")
else:
  print("Department key does not exist")

# output
Employee Details: {'employee_id': 101, 'name': 'Jency', 'age': 21, 'department': 'IT', 'salary': 25000}
Employee Name: Jency
Employee Salary: 25000
After Adding Experience: {'employee_id': 101, 'name': 'Jency', 'age': 21, 'department': 'IT', 'salary': 25000, 'experience': '1 Year'}
Updated Salary: 30000
After Removing Age: {'employee_id': 101, 'name': 'Jency', 'department': 'IT', 'salary': 30000, 'experience': '1 Year'}
Keys: dict_keys(['employee_id', 'name', 'department', 'salary', 'experience'])
Values: dict_values([101, 'Jency', 'IT', 30000, '1 Year'])
Employee Information:
employee_id : 101
name : Jency
department : IT
salary : 30000
experience : 1 Year
Department key exists

