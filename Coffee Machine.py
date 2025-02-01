

print("""
   ,o888888o.        ,o888888o.     8 8888888888   8 8888888888   8 8888888888   8 8888888888              ,8.       ,8.                   .8.           ,o888888o.    8 8888        8  8 8888 b.             8 8 8888888888   
   8888     `88.   . 8888     `88.   8 8888         8 8888         8 8888         8 8888                  ,888.     ,888.                 .888.         8888     `88.  8 8888        8  8 8888 888o.          8 8 8888         
,8 8888       `8. ,8 8888       `8b  8 8888         8 8888         8 8888         8 8888                 .`8888.   .`8888.               :88888.     ,8 8888       `8. 8 8888        8  8 8888 Y88888o.       8 8 8888         
88 8888           88 8888        `8b 8 8888         8 8888         8 8888         8 8888                ,8.`8888. ,8.`8888.             . `88888.    88 8888           8 8888        8  8 8888 .`Y888888o.    8 8 8888         
88 8888           88 8888         88 8 888888888888 8 888888888888 8 888888888888 8 888888888888       ,8'8.`8888,8^8.`8888.           .8. `88888.   88 8888           8 8888        8  8 8888 8o. `Y888888o. 8 8 888888888888 
88 8888           88 8888         88 8 8888         8 8888         8 8888         8 8888              ,8' `8.`8888' `8.`8888.         .8`8. `88888.  88 8888           8 8888        8  8 8888 8`Y8o. `Y88888o8 8 8888         
88 8888           88 8888        ,8P 8 8888         8 8888         8 8888         8 8888             ,8'   `8.`88'   `8.`8888.       .8' `8. `88888. 88 8888           8 8888888888888  8 8888 8   `Y8o. `Y8888 8 8888         
`8 8888       .8' `8 8888       ,8P  8 8888         8 8888         8 8888         8 8888            ,8'     `8.`'     `8.`8888.     .8'   `8. `88888.`8 8888       .8' 8 8888        8  8 8888 8      `Y8o. `Y8 8 8888         
   8888     ,88'   ` 8888     ,88'   8 8888         8 8888         8 8888         8 8888           ,8'       `8        `8.`8888.   .888888888. `88888.  8888     ,88'  8 8888        8  8 8888 8         `Y8o.` 8 8888         
    `8888888P'        `8888888P'     8 8888         8 8888         8 888888888888 8 888888888888  ,8'         `         `8.`8888. .8'       `8. `88888.  `8888888P'    8 8888        8  8 8888 8            `Yo 8 888888888888 

""")

water = 300
milk = 300
coffee = 100
money = 0


def report_list():
    print(f"""Water: {water}ml
Milk: {milk}ml
Coffee: {coffee}g
Money: {money}$""")


def coins():
    print("Enter Coins")
    quarters = float(input("Quarters : ? ")) * 0.25
    dimes = float(input("Dimes : ? ")) * 0.10
    nickles = float(input("Nickles : ? ")) * 0.05
    pennies = float(input("Pennies : ? ")) * 0.01
    return (quarters + dimes + nickles + pennies)


def make_drink(drink, water_needed, coffee_needed, milk_needed, price):
    global water, milk, coffee, money
    if water >= water_needed and coffee >= coffee_needed and milk >= milk_needed:
        cash = coins()
        if cash >= price:
            water -= water_needed
            coffee -= coffee_needed
            milk -= milk_needed
            money += price
            change = cash - price
            if change > 0:
                print(f"Here is your {drink} ☕. Your change is {change:.2f} $.")
            else:
                print(f"Here is your {drink} ☕. No change due.")
        else:
            print(f"Sorry, that's not enough money. Please insert more coins.")
    else:
        print(f"Sorry, not enough resources to make a {drink}.")


while True:
    start_q = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if start_q == "off":
        print("Turn Off Coffee Machine ✅")
        break
    elif start_q == "report":
        report_list()
    elif start_q == "espresso":
        make_drink("espresso", 50, 18, 0, 1.5)
    elif start_q == "latte":
        make_drink("latte", 200, 24, 150, 2.5)
    elif start_q == "cappuccino":
        make_drink("cappuccino", 250, 24, 100, 3.0)
    else:
        print("Please Enter espresso/latte/cappuccino only !!!")
