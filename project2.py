#Tip-Calculator-Generator

print("Welcome to the tip calculator.")
bill=input("What was the total bill? $")

tip_percentage=input("What percentage tip would you like to give? 10, 12, or 15? ")

number_of_people=input("How many people split the bill? ")

#Converting strings to float and int
bill_as_float=float(bill)
tip_percentage_as_int=int(tip_percentage)
number_of_people_as_int=int(number_of_people)

#converting tip percentage in dollars
tip_in_dollars=(bill_as_float*tip_percentage_as_int)/100

#bill_with_tip represents the bill need to be pay by each one
bill_with_tip=(bill_as_float+tip_in_dollars)/number_of_people_as_int
bill_with_tip_upto_two_decimals="%.2f"%(bill_with_tip)

print(f"Each person should pay: ${bill_with_tip_upto_two_decimals}")
