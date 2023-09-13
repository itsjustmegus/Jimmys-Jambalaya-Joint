# Jimmy's Jambalaya Joint
# File:        jimmys_jambalaya_joint_class.py
# Author:      Gus Allred
# Created:     09/13/23
# Version:     1
# Description:

# TODO: Create constant variable for cost of a bowl
BOWL_COST = 10.29

class JimmysJambalaya:
    def __init__(self):
        pass

    def calculate(self, num_of_bowls):
        # TODO: Calculate cost of bowls puchased
        self.num_of_bowls = num_of_bowls
        self.total_sale = num_of_bowls * BOWL_COST