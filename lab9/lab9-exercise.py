"""
Sally Han
April 24, Python Conditional Statement
Lab 9 Exercise"""

print("\n-----Lab 9 Exercise-----")
# nested conditionals will get extra points.
grade1 = float(input("Enter a number: "))
grade2 = float(input("Enter a number: "))
average = (grade1 + grade2)/2

if 0 <= average <= 100:
    if 90 <= average <= 100:
        print(f"GPA is A")
    else:
        if 70 <= average <= 89.99:
            print(f"GPA is B")
        else:
            if 60 <= average <= 69.99:
               print(f"GPA is C")
            else:
                if 50 <= average <= 59.99:
                   print(f"GPA is FAIL")
                else:
                    print("UNDEFINED")
else:
    print("Average is out of range")
print(f"For the average of {grade1} and {grade2}, your GPA is {average}")


