# Bill amount
bill_amount = 547.28

# Tip percentage
tip_percentage = 15

# Calculate tip
tip = (tip_percentage / 100) * bill_amount

# Calculate total amount to pay
total_amount = bill_amount + tip

# Number of friends
number_of_friends = 2

# Calculate each friend's share
each_share = total_amount / number_of_friends

# Display the results
print("Tip amount: ${:.2f}".format(tip))
print("Total amount to pay: ${:.2f}".format(total_amount))
print("Each person needs to pay: ${:.2f}".format(each_share))

