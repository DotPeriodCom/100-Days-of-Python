#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")

# bill_with_tip = tip / 100 * bill + bill
# bill_with_tip = bill * (1 + tip / 100)

#My Code
# print("Welcome to the tip calculator")
# bill = input("What was the total bill? ")
# tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
# people = input("How many people to split the bill? ")

# bill_as_int = float(bill)
# tip_as_int = int(tip)
# people_as_int = int(people)

# total = bill_as_int / people_as_int
# total_with_tip = total * ((tip_as_int / 100) + 1)
# split_bill = round(total_with_tip, 2)

# print(f"Each person should pay: ${split_bill}")