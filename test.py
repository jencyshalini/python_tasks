# list
cart=["pencil","pen","Box","notebook"]
cart.extend(["eraser","ruler"]);
remove_item=input("Enter the item to be removed:")
if remove_item in cart:
  cart.remove(remove_item)
  print(cart)
else:
  print("Item not found")
search=input("Enter the item to be searched:")
if search in cart:
  print("Item found")
else:
  print("Item not found")
print(len(cart))
# output
Enter the item to be removed:pen
['pencil', 'Box', 'notebook', 'eraser', 'ruler']
Enter the item to be searched:pencil
Item found
5

# set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print("All unique numbers:", set1.union(set2))
print("Common numbers:", set1.intersection(set2))
print("Only in first set:", set1.difference(set2))
set1.add(80)
print("After adding:", set1)
set1.remove(10)
print("After removing:", set1)
# output
All unique numbers: {70, 40, 10, 50, 20, 60, 30}
Common numbers: {40, 50, 30}
Only in first set: {10, 20}
After adding: {80, 50, 20, 40, 10, 30}
After removing: {80, 50, 20, 40, 30}

# tuple
salary = (25000, 30000, 35000, 30000, 40000)
print("First salary:", salary[0])
print("Last salary:", salary[-1])
print("Maximum salary:", max(salary))
print("Minimum salary:", min(salary))
print("Count of 30000:", salary.count(30000))
salary_list = list(salary)
salary_list.append(45000)
print("Updated salary list:", salary_list)
# output
First salary: 25000
Last salary: 40000
Maximum salary: 40000
Minimum salary: 25000
Count of 30000: 2
Updated salary list: [25000, 30000, 35000, 30000, 40000, 45000]


# dict stud
student = {"id": 101,"name": "Jency","age": 21,"course": "B.Tech IT"}
print("Keys:", student.keys())
print("Values:", student.values())
student["email"] = "jency@gmail.com"
print("After adding email:", student)
student["age"] = 22
print("After updating age:", student)
student.pop("course")
print("After removing course:", student)
print("Name exists:", "name" in student)
# output
Keys: dict_keys(['id', 'name', 'age', 'course'])
Values: dict_values([101, 'Jency', 21, 'B.Tech IT'])
After adding email: {'id': 101, 'name': 'Jency', 'age': 21, 'course': 'B.Tech IT', 'email': 'jency@gmail.com'}
After updating age: {'id': 101, 'name': 'Jency', 'age': 22, 'course': 'B.Tech IT', 'email': 'jency@gmail.com'}
After removing course: {'id': 101, 'name': 'Jency', 'age': 22, 'email': 'jency@gmail.com'}
Name exists: True

# dict mobile
mobile = {"Samsung": 20000,"Redmi": 15000,"Vivo": 18000,"Oppo": 17000,"iPhone": 60000}
for name, price in mobile.items():
    print(name, ":", price)
mobile["Realme"] = 16000
print("After adding:", mobile)
mobile["Samsung"] = 25000
print("After updating:", mobile)
# output
Samsung : 20000
Redmi : 15000
Vivo : 18000
Oppo : 17000
iPhone : 60000
After adding: {'Samsung': 20000, 'Redmi': 15000, 'Vivo': 18000, 'Oppo': 17000, 'iPhone': 60000, 'Realme': 16000}
After updating: {'Samsung': 25000, 'Redmi': 15000, 'Vivo': 18000, 'Oppo': 17000, 'iPhone': 60000, 'Realme': 16000
