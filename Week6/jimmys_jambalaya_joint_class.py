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

    def get_number_of_bowls(self):
        # Validation
        if self._num_of_bowls > 0:
            return self._num_of_bowls
        else:
            return 0

    def get_total_sale(self):
        return self._total_sale

    def calculate(self, num_of_bowls):
        # TODO: Calculate cost of bowls puchased
        self._num_of_bowls = num_of_bowls
        self._total_sale = num_of_bowls * BOWL_COST