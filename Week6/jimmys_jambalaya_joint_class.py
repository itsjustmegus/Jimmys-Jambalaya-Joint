# Jimmy's Jambalaya Joint
# File:        jimmys_jambalaya_joint_class.py
# Author:      Gus Allred
# Created:     09/27/23
# Version:     2
# Description: Jambalaya class file

# TODO: Create constant variable for cost of a bowl
BOWL_COST = 10.29

class JimmysJambalaya:
    def __init__(self):
        self.qty_bowls = 0
        # Initialize parallel lists for menu items and prices
        self._menu_items = ["Jambalaya Bowl", "Cajun Rice", "Soft Drink"]
        self._menu_prices = [10.29, 2.49, 2.19]
        # Initialize empty cart
        self.cart = []

    @property
    def bowls(self) -> int:
        return self._num_of_bowls
    
    @bowls.setter
    def bowls(self, num_of_bowls):
        self._num_of_bowls = num_of_bowls

    @property
    def rice(self) -> int:
        return self._num_of_rice
    
    @rice.setter
    def rice(self, num_of_rice):
        self._num_of_rice = num_of_rice

    @property
    def drinks(self) -> int:
        return self._num_of_drinks
    
    @drinks.setter
    def drinks(self, num_of_drinks):
        self._num_of_drinks = num_of_drinks

    def get_menu_items(self) -> list:
        return self._menu_items
    
    def get_menu_prices(self) -> list:
        return self._menu_prices
    
    def display_menu(self) -> str:
        """Display menu items and prices"""
        display = ""
        for x in range(len(self._menu_items)):
            display += f"{self._menu_items[x]} {self._menu_prices[x]}\n"
        return display
    
# ---------------------------- GET BOWLS, RICE, AND DRINKS FROM USER ---------------------------- #
    def get_qty_bowls(self) -> int:
        """Input validation the customer must order at least one bowl"""
        # TODO: Get int input from user how many bowls sold
        self._num_of_bowls = int(input("Enter number of bowls of Jambalaya: "))
        if self._num_of_bowls > 0:
            return self._num_of_bowls
        else:
            return "You must order at least one bowl"

    def get_qty_rice(self) -> int:
        # TODO: Get int input from user how many bowls of rice sold
        self._num_of_rice = int(input("Enter number of bowls of Cajun Rice: "))
        if self._num_of_rice > 0:
            return self._num_of_rice

    def get_qty_drinks(self) -> int:
        # TODO: Get int input from user how many bowls sold
        self._num_of_drinks = int(input("Enter number of drinks: "))
        if self._num_of_drinks > 0:
            return self._num_of_drinks

    def calculate_bowls(self, num_of_bowls: int = 1):
        # TODO: Calculate cost of bowls purchased
        """Calculate cost of the bowls purchased
        
            Parameters:
            num_of_bowls (int)
        """
        self._num_of_bowls = num_of_bowls
        self._bowl_sale = self._num_of_bowls * self._menu_prices[0]
    
    def calculate_rice(self, num_of_rice: int = 1):
        # TODO: Calculate cost of bowls purchased
        """Calculate cost of the bowls purchased
        
            Parameters:
            num_of_bowls (int)
        """
        self._num_of_rice = num_of_rice
        self._rice_sale = self._num_of_rice * self._menu_prices[1]

    def calculate_drinks(self, num_of_drinks: int = 1):
        # TODO: Calculate cost of bowls purchased
        """Calculate cost of the bowls purchased
        
            Parameters:
            num_of_bowls (int)
        """
        self._num_of_drinks = num_of_drinks
        self._drink_sale = self._num_of_drinks * self._menu_prices[2]

    def calculate_total(self) -> float:
        self._total_sale = self._bowl_sale + self._rice_sale + self._drink_sale

    def get_total_sale(self) -> float:
        """Return total sale from object
        
            Returns:
            num_of_bowls (float)
        """
        return self._total_sale
        