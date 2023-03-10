#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("**** Tip Calculator ****")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 5, 10, 15, 20 "))
people = int(input("How many people to split the bill? "))

tip_calul = bill * tip
tip_calul /= 100

total_bill_with_tip = bill + tip_calul
bill_per_person = total_bill_with_tip / people

final_amount = round(bill_per_person, 2)
print(f"Each Person should pay: ${final_amount}")