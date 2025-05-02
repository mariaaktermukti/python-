marks = int(input("Enter the marks: "))

if marks >= 90 and marks <= 100:
    print("You got A.")
elif marks >= 80 and marks < 90:
    print("You got A-.")
elif marks >= 70 and marks < 80:
    print("You got B.")
elif marks >= 60 and marks < 70:
    print("You got B-.")
else:
    print("You got C.")

print("Marks are updated.")
