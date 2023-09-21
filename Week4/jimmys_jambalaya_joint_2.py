# Jimmy's Jambalaya Joint
# File:        jimmys_jambalaya_joint_2.py
# Author:      Gus Allred
# Created:     08/31/23
# Version:     2
# Description: POS program

# TODO: Create constant variable for cost of a bowl
BOWL_COST = 10.29

def main():
    number_of_bowls = get_input()
    total_sale = calculate(number_of_bowls)
    display(total_sale)

def get_input():
    # TODO: Get int input from user how many bowls sold
    num_of_bowls = int(input("Enter number of bowls of Jambalaya: "))
    return num_of_bowls

def calculate(num_of_bowls):
    # TODO: Calculate cost of bowls puchased
    total_receipt = num_of_bowls * BOWL_COST
    return total_receipt

def display(total_sale):
    # TODO: Display transaction for customer
    print(f"Your order total is: ${total_sale:,.2f}")


# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()