# Welcome message and input for the customer's name
name = input("Hello, welcome to our coffee shop!\nCan I get your name?\n\n")

# Check if the name is in a predefined list
if name in ["Ben", "Patrick", "Patricia"]:
    evil = input("Are you evil?\n")
    
    # Check if the customer is evil
    if evil.lower() == "yes":
        print("GET OUT OF HERE YOU'RE NOT WELCOME")
        exit()
    else:
        print("Oh, so you're one of those good " + name)
elif name.lower() == "gloria":
    print("\nOh, I know someone named Gloria. What would you like to order?\n")
else:
    print("\nHello " + name + ", what would you like to order?\n")

while True:
    # Display the menu
    menu = "Latte\nBlack coffee\nGreen coffee\nIce Cream\n"
    print(menu)

    # Get the customer's order
    response = input().lower()

    # Process the order
    if response == "latte":
        cream = input("Would you like whipped cream?\n")
        
        if cream.lower() in ["yes", "y"]:
            print("Your total is $15")
        else:
            print("Your total is $9")
    elif response == "black coffee":
        print("Your total is $5")
    elif response == "green coffee":
        print("Your total is $8")
    elif response == "ice cream":
        flavour = input(
            "\nWhat flavor would you like?\n\n"
            "Strawberry flavor $14\n"
            "Banana flavor $13\n"
            "Vanilla flavor $12\n"
            "Simple $10\n"
            "Mango flavor $17\n\n"
        ).lower()
        
        if flavour == "strawberry":
            print("That's gonna be $14")
        elif flavour == "banana":
            print("That's gonna be $13")
        elif flavour == "vanilla":
            print("That's gonna be $12")
        elif flavour == "simple":
            print("That's gonna be $10")
        elif flavour == "mango":
            print("That's gonna be $17")
        else:
            print("Sorry, we don't have that flavor on the menu.")

    # Ask if the customer wants to order again
    order_again = input("Would you like to order again? (yes/no)\n").lower()
    if order_again != "yes":
        break

# Farewell message
print("Thank you for visiting our coffee shop, " + name + "! Goodbye!")