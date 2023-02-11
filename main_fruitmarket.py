print('Welcome to the GC Fruit market!')

#Setting fruit count variables
apple_count = 0
grape_count = 0
orange_count = 0

shopping = True

name = input('What is your name? \n')
while(shopping == True):

    selection = (input(f'Welcome {name}. Which Fruit would you like to buy? \n'
           f'1. Apple $2 \n'
           f'2. Grape $1 \n'
           f'3. Orange $3 \n'))

    if (selection == '1'):
        apple_count += 1
        apple_cost = apple_count * 2
        print("You bought 1 apple at $2")
        shop_continue = input("Would you like to buy an other piece of fruit? y/n \n")
        if (shop_continue == 'n'):
            shopping = False
    elif (selection == '2'):
        grape_count += 1
        grape_cost = grape_count * 1
        print("You bought 1 grape at $1")
        shop_continue = input("Would you like to buy an other piece of fruit? y/n \n")
        if (shop_continue == 'n'):
            shopping = False

    elif (selection == '3'):
        orange_count += 1
        orange_cost = orange_count * 3
        print('You bought 1 orange at $3')
        shop_continue = input("Would you like to buy an other piece of fruit? y/n \n")
        if (shop_continue == 'n'):
            shopping = False
    else:
        print("Please make a selection from the list given.")

subtotal = apple_cost + grape_cost + orange_cost
tax = float(.05 * subtotal)
total = float(subtotal + tax)

print(f"Order for {name} \n"
      f"{apple_count} apple(s) at $2 apiece \n"
      f"{grape_count} grape(s) at $1 apiece \n"
      f"{orange_count} orange(s) at $3 apiece \n"
      f"Sub Total: ${subtotal} \n"
      f"5% Tax: ${round(tax, 2)} \n"
      f"Total: ${round(total, 2)}")
