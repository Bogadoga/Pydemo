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

menu =("Latte\nBlack coffee\nGreen coffee\n")

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

#END
else:
  print("Sorry we dont have that here.")
  exit()