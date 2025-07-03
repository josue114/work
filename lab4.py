#checking = 'yes' 
#while checking = 'yes'
#print("what is your age:17")
#user_input = input()
#if int(user_input) >= 18:
#print('yes you can vote')
#else:
#print('you cant vote')
#print('would you like to check another age?')
#user_input2=input()
#checking = user_input2








#task 2
number = [15, -7, 0, 23, -42, 8]
for number in number:
    if number >0:
        print( f"{number} is positive")
    elif number < 0:
        print( f"{number} is negative")
    else:
        print( f"{number} is zero")


        #task3
        inventory="coal", "dirt", "gold", "enchanted sword"
        for block in inventory:
            print( f"{block} is in the inventory")
            if block == "enchanted sword":
                print("jackpot! you found a enchanted sword!")
