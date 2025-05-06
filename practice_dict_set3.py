# #WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

marks={}
x=int(input("Enter phy: "))
marks.update({"phy" : x})

x=int(input("Enter chem: "))
marks.update({"chem" : x})

x=int(input("Enter bio: "))
marks.update({"bio" : x})

print(marks)