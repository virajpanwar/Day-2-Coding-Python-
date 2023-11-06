#resturant tip calculator
print("Welcome to TIP Calculator")
bill=float(input("What was the total bill? $ "))
tip=int(input("What percent tip would you like to give? 10, 12 or 15? "))
people=int(input("How many people are splitting the bill? "))
tip=tip/100 *bill
total=bill+tip
print(f"Each person should pay: ${round(total/people, 2)}")
