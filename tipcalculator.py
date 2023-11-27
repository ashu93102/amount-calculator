#this can be use the split the bills in friends

# User input
bill = input("What was the total bill?\n")
tip = input("what percentage of tip would you like to give? 10, 12 or 15?\n")
total_people = input("How many people to split the bill?\n")

# converting data type
num_bill = float(bill)
num_tip = int(tip)

pay = (num_bill + ((num_bill * num_tip) / 100)) / int(total_people)

amount_to_pay = round(pay, 2)

print(f"Each person should pay: ${amount_to_pay}")