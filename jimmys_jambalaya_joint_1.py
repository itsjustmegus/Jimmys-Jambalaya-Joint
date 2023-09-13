# Jimmy's Jambalaya Joint
# File:        jimmys_jambalaya_joint_1.py
# Author:      Gus Allred
# Created:     08/31/23
# Version:     1
# Description: POS program

# TODO: Create constant variable for cost of a bowl
BOWL_COST = 10.29

# TODO: Get int input from user how many bowls sold
num_of_bowls = int(input("Enter number of bowls of Jambalaya: "))

# TODO: Calculate cost of bowls puchased
total_receipt = num_of_bowls * BOWL_COST

# TODO: Display transaction for customer
print(f"Your order total is: ${total_receipt:,.2f}")