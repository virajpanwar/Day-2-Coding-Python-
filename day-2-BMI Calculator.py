#BMI Calculator
height= float(input("Enter your height in meters: "))
weight= float(input("Enter your weight in kilograms: "))
bmi= weight/height**2
print("Your BMI is: " + str(int(bmi)))
