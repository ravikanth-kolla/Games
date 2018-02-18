import random

comp_list = []
while len(comp_list) < 4:
    number = random.randint(1, 9)
    if not number in comp_list:
        comp_list.append(random.randint(1, 9))

user_list = []
bullsCounter = 0
cowsCounter = 0
scoreboard = []
scoreboard.append("     |Bulls|Cows")
scoreboard.append("___________|____")
while bullsCounter < 4:
    bullsCounter = 0
    cowsCounter = 0
    user_str = str(input("Think of 4 numbers: "))
    user_list = user_str
    print(user_list)
    for x in user_list:
        if int(x) in comp_list:
            cowsCounter = cowsCounter +1
        if int(x) == comp_list[user_list.index(x)]:
            bullsCounter = bullsCounter +1
    print("You have " + str(bullsCounter) + " bulls and " +str(cowsCounter) +" cows")
    scoreboard.append(" "+user_str + "|  "+str(bullsCounter)+ "  "+ "|"+" "+str(cowsCounter)+"  ")
    for line in scoreboard:
        print(line)
    if bullsCounter < 4 :
        keepGoing = input("Do you want to continue? (y)es or (n)o? ")
        if keepGoing == "n":
            break

print("Computer thought of "+str(comp_list))