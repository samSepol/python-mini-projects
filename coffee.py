from ingredient import MENU, resources
# print(MENU)


# TODO 2: Get resources

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
coffee_profit = 0

'''
    # TODO 2: use for loop over resources
    for resource in resources:
    print(f"{resource}:{resources[resource]}")
       Output : 
            water:300
            milk:200
            coffee:100
'''


def get_resources():
    # TODO: 1 print report of ingredient
    """Get the report of resources in machine """
    print(f'Milk  : {milk} ml')
    print(f"Water : {water} ml ")
    print(f"Coffee : {coffee} ml")
    print(f"Coffee-Profit : {coffee_profit} $ ")


def check_resources(milk, water, coffee, coffee_Request):
    """ Returns the resources needed for requested coffee"""
    if milk_needed > milk:
        print("Sorry, there is not enough milk . ")
        return False
    elif water_needed > water:
        print("Sorry, there is not enough water. ")
        return False
    elif coffee_needed > coffee:
        print("Sorry, there is not enough coffee. ")
        return False
    else:
        return True


def insert_coins():
    """ Insert the coins and return total of inserted coins"""
    print("Please insert the coins.")
    # Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    quarters = int(input("How many quarters. "))
    dimes = int(input("How many dimes. "))
    nickles = int(input("How many nickles. "))
    pennies = int(input("How many pennies. "))
    total = (quarters*0.25)+(dimes*0.10) + (nickles*0.05)+(pennies*0.01)
    return round(total, 2)


# is_machine_Off = True
while True:
    coffee_Request = input(
        'What would you like? (espresso/latte/cappuccino): ')

    #  only for maintenance guys

    if coffee_Request == 'off':
        print("Machine is under Maintenance :( ")
        break
        # is_machine_Off = False

    elif coffee_Request == 'report':
        get_resources()
    elif coffee_Request == 'refill':
        water += 100
        milk += 100
        coffee += 50
        print("Ingredients are refilled !")
        get_resources()
    else:
        # resources needed
        if coffee_Request != 'espresso':
            milk_needed = MENU[coffee_Request]['ingredients']['milk']
            water_needed = MENU[coffee_Request]['ingredients']['water']
            coffee_needed = MENU[coffee_Request]['ingredients']['coffee']
        needed_resources = check_resources(
            milk, water, coffee, coffee_Request)
        print(needed_resources)
        if needed_resources:
            inserted_Money = insert_coins()
            # get coffee price from ingredients.py
            coffee_Price = MENU[coffee_Request]['cost']
            if inserted_Money >= coffee_Price:
                if inserted_Money > coffee_Price:
                    change = inserted_Money-coffee_Price
                    coffee_profit += coffee_Price
                    print(f"Here your change {round(change,2)} $")
                print(f"Here is your {coffee_Request} ! Enjoy it ..")
                milk -= milk_needed
                water -= water_needed
                coffee -= coffee_needed
                print(f"coffee_profit : {coffee_profit}")
                print("Remaining ingredients")

                get_resources()
            else:
                print("Sorry that's not enough money. Money refunded. ")
