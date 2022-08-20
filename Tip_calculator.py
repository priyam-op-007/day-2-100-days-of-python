print('Welcome to tip calculator.')
total_bill = input("What was the total bill? $")
percentage_of_tip = input("What percentage tip would you like to give? 10, 12 or 15?\n")
bill_of_tip = (int(percentage_of_tip)/100)*(float(total_bill))
final_bill = bill_of_tip + float(total_bill)
peoples = input("How many people to split the bill?\n")
pay = round(final_bill/(float(peoples)), 2)
print(f"Each person must pay: ${pay}")
                
                
Output - 
Welcome to tip calculator.
What was the total bill? $124.56
What percentage tip would you like to give? 10, 12 or 15?
12
How many people to split the bill?
7
Each person must pay: $19.93
