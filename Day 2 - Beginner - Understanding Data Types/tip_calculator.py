
# Ask some basic questions about the bill using inputs
bill_price = input("What is the price of the bill? ")
tip = input("How much tip do you want to give? ")
split = input("How many people are going to split the bill? ")

# Calculate the cost of the tip, total bill with tip, and how much each person is going to pay
total_tip = (float(tip) / 100) * float(bill_price)
total_price_with_tip = total_tip + float(bill_price)
price_per_person = total_price_with_tip / int(split)

# Print the final result
print(f"The total price per person is {price_per_person:.2f}")
