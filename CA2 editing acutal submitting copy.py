
#CA2 doc 
#copied from google doc 
"""Class 02
Kim
Chee
Cryptocurrency Portfolio Application Main Menu

Display Cryptocurrency
Add Cryptocurrency
Amend Cryptocurrency
Remove Cryptocurrency
Crypto Portfolio Statement
<Student 1 to propose a new function>
<Student 2 to propose a new function>
E. Exit Main Menu
Select an option:"""


print("Class 02\n Jeeva \n Edison \nCryptocurrency Portfolio Application Main Menu\n")
intro_text="""1. Display Cryptocurrency
2. Add Cryptocurrency
3. Amend Cryptocurrency
4. Remove Cryptocurrency
5. Crypto Portfolio Statement
6. <Student 1 to propose a new function>
7. <Student 2 to propose a new function>
E. Exit Main Menu"""
list=[["No","Name", "Capitalization", "QtyBought", "Bought Price", "Current Price"],
[1, "Bitcoin", "High", 15, 38000, 62000],
[2, "Ethereum", "High", 90, 4200, 3500],
[3, "Solana", "Mid", 60, 260, 110],
[4, "Decentraland", "Mid", 30000, 1.5, 5],
[5, "The Sandbox", "Mid", 25000, 2, 4],
[6, "Dogecoin", "Low", 55000, 0.4, 0.15]]
print(intro_text)
#option=input("Select option to choose ")
print(len(list))
option=input("Select an option:")
#if option.lower() =="e":
    #print("Exit Main Menu")
spaceneed=10
#print(len(list[3][1]))
#must make function that can print number of spaces 
def space(x):
    return (" "*x)
#rmb can do string multiplication , dont use for loop as the x doest change properly 
if option.lower()=='e':
    print("Exited ")
elif int(option)== 1:
    #thinkig process: u need a set number of spaces , so number of space- length of word 
    for row in list:
        print(str(list[list.index(row)][0])+str(space(5-len(str(list[list.index(row)][0])))),str(list[list.index(row)][1])+str(space(15-len(str(list[list.index(row)][1])))), str(list[list.index(row)][2])+str(space(15-len(str(list[list.index(row)][2])))), str(list[list.index(row)][3])+str(space(15-len(str(list[list.index(row)][3])))), str(list[list.index(row)][4])+str(space(15-len(str(list[list.index(row)][4])))), str(list[list.index(row)][5])+str(space(9-len(str(list[list.index(row)][0])))))

        #print(str(list[list.index(row)][0])+"    ",list[list.index(row)][1],list[list.index(row)][2],list[list.index(row)][3],list[list.index(row)][4],list[list.index(row)][5])   
elif int(option) == 2:
    while True:
        a = input("Enter Cryptocurrency Name :")
        for i in range(len(list)):
            if a.title() == list[i][1]:
                print(list[i][1], "already exists, please enter a new cryptocurrency")
                break
        else:
            break
    while True:
        b = input("Enter Market Cap of Crypto: High, Mid, Low :")
        caselist=("high","low","mid")#using this ignores the bracket nonscne
        if b.lower() in caselist:
            break
        else:
            print("Please enter the correct word ")
    while True:
        try:
            c = int(input("Enter Quantity of Crypto Bought = "))
            d = float(input("Enter Buy In Price of Crypto = "))
            e = float(input("Enter Market Price of Crypto = "))
        except ValueError :
            print("Please enter again ")
        else:
            break
    empty = [a, b, c, d, e]
    list.append(empty)




#Qns 2 
"""When the Add Cryptocurrency function is chosen, the user is prompted to enter the Name, Market 
Cap, Quantity of Crypto Bought, the Buy In Price of Crypto and the Market Price of the Crypto. 
• Perform input validation of Market Cap of Crypto, Quantity of Crypto Bought, the Buy In Price of the 
Crypto and the Market Price of the Crypto.
• You may want to check that the Cryptocurrency Name entered does not already exist in your database."""

