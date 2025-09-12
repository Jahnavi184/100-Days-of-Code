print("Welcome to the tip calculator!")
bill=input("What was the total bill?")
tip=input("how much tip would you like to give, 10, 12 or 15?") 
people=input("How many people would like to spilt the bill?")
total_bill=bill+(100/tip)
bill_per_person=total_bill/people
print("Each person should pay", bill_per_person)
