fruits=[]
print("\n\n\t\t\t Welcome to fruits Department\n\n")
#limit to add data, only can add 10 new data



limit=10
while True:
    print("\tadd fruits or remove fruits from list")
    print("\tpress 1 to add item, press 2 to remove item")
    print("\tYour maximum limit is 10")
    choose=int(input("\nchoose option 1 or 2:"))
    
    if limit<0:
        print("you have reached your limit")
        break
    if choose==1:
        new_fruit=input("enter new fruit brought:")
        fruits.append(new_fruit)
        print("Fruits list after adding new item")
        print(fruits)
        limit=limit-1
        print("You have ", limit," limits\n")
    elif choose==2:
        
        remove_fruit=input("fruits to remove:")
        fruits.remove(remove_fruit)
        print("fruits after removing" + " " + remove_fruit)
        print(fruits)
        limit=limit+1
        if limit>10:
          print("you have reached your limit")
        else:
          print("You have ", limit," limits\n")