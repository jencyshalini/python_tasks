#task 5

def student_details():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    full_name = first_name + " " + last_name
    print("Full Name: {}".format(full_name))
    print("Uppercase:", full_name.upper())
    print("Lowercase:", full_name.lower())
    print("Total characters:", len(full_name))
    print("Characters:")
    for i in full_name:
        if i == " ":
            continue
        print(i)
    letter = input("Enter a letter to check: ")
    if full_name.lower().startswith(letter.lower()):
        print("The name starts with", letter)
    else:
        print("The name does not start with", letter)
    print("First 3 characters:", full_name[:3])
    print("Last 3 characters:", full_name[-3:])
  
student_details()

# output
Enter your first name: Jency
Enter your last name: shalini
Full Name: Jency shalini
Uppercase: JENCY SHALINI
Lowercase: jency shalini
Total characters: 13
Characters:
J
e
n
c
y
s
h
a
l
i
n
i
Enter a letter to check: p
The name does not start with p
First 3 characters: Jen
Last 3 characters: ini

