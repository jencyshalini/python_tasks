# task 1
marks=[]
for i in range(1,6):
  mark=int(input("Enter the mark:"))
  marks.append(mark)
print("Marks:",marks)
marks.append(95)
print("After append:",marks)
marks.insert(1,85)
print("After insert:",marks)
marks.remove(90)
print("After remove:",marks)
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))
total = sum(marks)
average = total / len(marks)
print("Total Marks:", total)
print("Average Marks:", average)
marks.sort()
print("Ascending Order:", marks)

# output
Enter the mark:78
Enter the mark:99
Enter the mark:90
Enter the mark:85
Enter the mark:95
Marks: [78, 99, 90, 85, 95]
After append: [78, 99, 90, 85, 95, 95]
After insert: [78, 85, 99, 90, 85, 95, 95]
After remove: [78, 85, 99, 85, 95, 95]
Highest Mark: 99
Lowest Mark: 78
Total Marks: 537
Average Marks: 89.5
Ascending Order: [78, 85, 85, 95, 95, 99]

# task 2
products=("pen","pencil","eraser","sharpener","ruler")
print(products)
print("First Product",products[0])
print("Last Products",products[-1])
print("First 3 products",products[:3])
product=input("Enter the product:")
if product in products:
  print(product,"is available")
else:
  print(product,"is not available")
print("No of pens",products.count("pen"))
print("Position of pencil:",products.index("pencil"))
new_products=("paper","pin")
products+=new_products
print(products)
print(products*2)
for i in products:
  print(i)

# output
('pen', 'pencil', 'eraser', 'sharpener', 'ruler')
First Product pen
Last Products ruler
First 3 products ('pen', 'pencil', 'eraser')
Enter the product:scale
scale is not available
No of pens 1
Position of pencil: 1
('pen', 'pencil', 'eraser', 'sharpener', 'ruler', 'paper', 'pin')
('pen', 'pencil', 'eraser', 'sharpener', 'ruler', 'paper', 'pin', 'pen', 'pencil', 'eraser', 'sharpener', 'ruler', 'paper', 'pin')
pen
pencil
eraser
sharpener
ruler
paper
pin
