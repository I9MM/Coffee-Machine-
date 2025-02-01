water = 300
milk = 300
coffee = 100
money = 0

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

def report_list () :
    print(f"""Water: {water}ml
Milk: {milk}ml
Coffee: {coffee}g
Money: {money}$""")
def coins () :
    print("Enter Coins")
    quarters = float(input("Quarters : ? "))*0.25
    dimes = float(input("Dimes : ? "))*0.10
    nickles = float(input("Nickles : ? "))*0.05
    pennies = float(input("Pennies : ? "))*0.01
    return (quarters + dimes + nickles + pennies)
while True :
    start_q = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if start_q == "off"  :
        print(" Turn Off Coffee Machine ✅ ")
        break
    elif start_q == "report" :
        report_list()
    elif start_q == "espresso" :
        if water >= 50 and coffee >= 18 :
            cash = coins()
            if cash == 1.5 :
                water -=50
                coffee -=18
                money += 1.5
                print("Here is your espresso ☕. No change due.")
            elif cash > 1.5 :
                water -=50
                coffee -=18
                money += 1.5
                change = cash - 1.5
                print(f"Here is your espresso ☕. Your change is {change:.2f} $ " )
            else :
                print("Sorry, that's not enough money. Please insert more coins.")
        else :
            print(f"Sorry, not enough resources to make an {start_q}.")
    elif start_q == "latte" :
        if water >= 200 and coffee >= 24 and milk >= 150 :
            cash = coins()
            if cash == 2.50 :
                water -=200
                coffee -=24
                milk -= 150
                money += 2.50
                print("Here is your espresso ☕. No change due.")
            elif cash > 2.50 :
                water -=200
                coffee -=24
                milk -= 150
                money += 2.50
                change = cash - 2.50
                print(f"Here is your espresso ☕. Your change is {change:.2f} $ " )
            else :
                print("Sorry, that's not enough money. Please insert more coins.")
        else :
            print(f"Sorry, not enough resources to make an {start_q}.")
    elif start_q == "cappuccino" :
        if water >= 250 and coffee >= 24 and milk >= 100 :
            cash = coins()
            if cash == 3.00 :
                water -=250
                coffee -=24
                milk -= 100
                money += 3.00
                print("Here is your espresso ☕. No change due.")
            elif cash > 3.00 :
                water -=250
                coffee -=24
                milk -= 100
                money += 3.00
                change = cash - 3.00
                print(f"Here is your espresso ☕. Your change is {change:.2f} $ " )
            else :
                print("Sorry, that's not enough money. Please insert more coins.")
        else :
            print(f"Sorry, not enough resources to make an {start_q}.")
    else :
        print("Please Enter espresso/latte/cappuccino only !!!")
