# task 2 
# 1
amount=int(input("Enter the total amount:"))
member=input("Are you a member?(yes/no)")
if amount>=2000 and member=="yes":
  print("Eligible for 20% discount")
else:
  print("Not eligible for discount")

# 2
stu_attend=int(input("Enter your attendance percentage:"))
stu_marks=int(input("Enter your marks:"))
if stu_attend>=75 and stu_marks>=40:
  print("Eligible for examination")
else:
  print("Not Eligible for examination")

# ouput

Enter the total amount:4000
Are you a member?(yes/no)yes
Eligible for 20% discount

Enter your attendance percentage:56
Enter your marks:68
Not Eligible for examination
