# task 3
def Even():
  for i in range(1,51):
    if i%2==0:
      print(i)

def mul_of_3():
  for i in range(1,30):
    if i%3==0:
      continue
    else:
      print(i)

def stop():
  num=int(input("Enter a number:"))
  i=1
  while i<=num:
    print(i)
    i+=1
    if i==num:
      break

def pos_neg_num():
  for i in range(10):
    nums=int(input("Enter the number:"))
    if nums>0:
      print("Positive")
    elif nums<0:
      print("Negative")
    else:
      print("Zero")
      break

Even()
stop()
mul_of_3()
pos_neg_num()

# output
# even numbers
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
# stop at 15
Enter a number:15
1
2
3
4
5
6
7
8
9
10
11
12
13
14
# mul of 3
1
2
4
5
7
8
10
11
13
14
16
17
19
20
22
23
25
26
28
29
# break at 0
Enter the number:6
Positive
Enter the number:-9
Negative
Enter the number:0
Zero

    

