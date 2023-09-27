# Jimmy's Jambalaya Joint
# File:        jimmys_jambalaya_joint_main_cli.py
# Author:      Gus Allred
# Created:     09/27/23
# Version:     2
# Description: POS program

import jimmys_jambalaya_joint_class as jimmys_jambalaya

def display_menu():
    print("Menu:")
    menu_items = jambalaya.get_menu_items()
    menu_prices = jambalaya.get_menu_prices()
    for item, price in zip(menu_items, menu_prices):
        print(f"{item}: ${price:.2f}")

def display(bowls, rice, drinks):
    # TODO: Display transaction for customer
    total_sale = jambalaya.get_total_sale()
    print(f" bowls of jambalaya ordered: {bowls}")
    print(f"bowls of cajun rice ordered: {rice}")
    print(f"             drinks ordered: {drinks}")
    print(f"Your order total is: ${total_sale:,.2f}")


# Create JimmysJambalaya object
jambalaya = jimmys_jambalaya.JimmysJambalaya()
display_menu()

# Get number of bowls from user
jambalaya.get_qty_bowls()
bowls = jambalaya._num_of_bowls

# Get number of rice from user
jambalaya.get_qty_rice()
rice = jambalaya._num_of_rice

# Get number of drinks from user
jambalaya.get_qty_drinks()
drinks = jambalaya._num_of_drinks

# Calculate cost of bowls
jambalaya.calculate_bowls(bowls)
jambalaya.calculate_rice(rice)
jambalaya.calculate_drinks(drinks)
jambalaya.calculate_total()

# Display results of transaction
display(bowls, rice, drinks)