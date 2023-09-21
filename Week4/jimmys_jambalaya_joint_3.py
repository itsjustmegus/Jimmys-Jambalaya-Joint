# Jimmy's Jambalaya Joint
# File:        jimmys_jambalaya_joint_3.py
# Author:      Gus Allred
# Created:     08/31/23
# Version:     3
# Description: POS program

# TODO: Create constant variable for cost of a bowl
BOWL_COST = 10.29

class JimmysJambalaya:
    def __init__(self):
        pass

    def get_input(self):
        # TODO: Get int input from user how many bowls sold
        self.num_of_bowls = int(input("Enter number of bowls of Jambalaya: "))

    def calculate(self):
        # TODO: Calculate cost of bowls puchased
        self.total_sale = self.num_of_bowls * BOWL_COST

    def display(self):
        # TODO: Display transaction for customer
        print(f"Your order total is: ${self.total_sale:,.2f}")

jimmys_jambalaya = JimmysJambalaya()

while True:
    jimmys_jambalaya.get_input()
    jimmys_jambalaya.calculate()
    jimmys_jambalaya.display()