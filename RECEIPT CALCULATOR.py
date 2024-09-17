import math
print("Looking to split the cost of a group purchase?\nWelcome to our Receipt Calculator!\nWe will ask you a few questions about your purchase(s) to calculate the total cost per person.")

price_all=eval(input("Step 1: Please input the cost of each meal/product.\n(Note: Eliminate the '$' sign instead seperate with a '+'.)\n"))
tax_p=float(input("Step 2:What is the sales tax in your area?\n(Note: Eliminate the '%' sign.)\n"))
tip_p=float(input("Step 3: What percentage would you like to give as a tip?\n(Note: Eliminate the '%' sign.)\n"))
split=float(input("Step 4: How many people are you splitting the bill with?\n(Note:If you are not splitting the bill with anyone, just type'1'.)\n"))
total_p= (price_all+(price_all*(tax_p/100.0))+(price_all*(tip_p/100.0)))/split
final_p= round(total_p,2)
print("The total cost per person is: $",final_p,".")