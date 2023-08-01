name =input("Hello welcome to our coffee shop!\nCan i get your name?\n\n")


#if the name is ben patrick or patricia and they are evil they will get kicked out.
if name in ["Ben", "Patrick", "Patricia"]:
  evil =input("Are you evil?\n")
  if evil == "Yes":
    print ("GET OUT OF HERE YOUR NOT WELCOME")
    exit()
  else:
    
    print("Oh so your one of those good " +name)

print("\nHello " + name + " what would you like to order?\n")

menu =("Latte\nBlack coffee\nGreen coffee\nPizza\nTea\nSushi")

print(menu)

response =input()

if response == "Latte":
  cream = input("Would you like whipped cream?\n")
  
  if cream in ["Yes", "yes", "y"]:
    print("Your total is 15 $")
  else:
    print("Your total is 9 $")
    

elif response == "Black coffee":
  print("Your total is 5 $")

elif response == "Green coffee":
  print("Your total is 8 $")

elif response == "Tea":
  print("Your total is 4 $")

if response == "Sushi":
  def calculate_total_cost(num_pieces):
    cost_per_set = 5  # $5 for every set of 4 pieces
    sets_needed = (num_pieces + 3) // 4  # Round up to the nearest set of 4 pieces
    total_cost = sets_needed * cost_per_set
    return total_cost

def main():
    try:
        num_pieces = int(input("How many pieces of sushi would you like? "))
        if num_pieces < 0:
            print("Can you please try a different amounut.")
        else:
            total_cost = calculate_total_cost(num_pieces)
            print(f"Total cost: ${total_cost}")
    except ValueError:
        print("Can you please try a different amounut.")

if __name__ == "__main__":
    main()
  
if response == "Pizza":
   pizzatype = ("")


#END
else:
  print("Sorry we dont have that here.")
  exit()