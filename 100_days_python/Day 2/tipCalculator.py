print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, 15(please do not write % in it just write number: " ))
people = int (input("How many people to split the bill? "))

bill_with_tip = (tip/100 * bill) + bill
print(bill_with_tip)

bill_per_person = bill_with_tip/people

print(f"Each person should pay: ${bill_per_person}")