# Jimmy's Jambalaya Joint
# File:        jimmys_jambalaya_joint_main_cli.py
# Author:      Gus Allred
# Created:     09/13/23
# Version:     2
# Description: POS program

import jimmys_jambalaya_joint_class as jambalaya

def get_input():
    # TODO: Get int input from user how many bowls sold
    num_of_bowls = int(input("Enter number of bowls of Jambalaya: "))
    return num_of_bowls

def display():
    # TODO: Display transaction for customer
    num_of_bowls = jimmys_jambalaya.get_number_of_bowls()
    total_sale = jimmys_jambalaya.get_total_sale()
    print(f"Number of bowls ordered: {num_of_bowls}")
    print(f"Your order total is: ${total_sale:,.2f}")


num_of_bowls = get_input()

jimmys_jambalaya = jambalaya.JimmysJambalaya()

jimmys_jambalaya.calculate(num_of_bowls)

display()