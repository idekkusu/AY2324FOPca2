'''
#Menu Display
print("-"*80)
print("\tClass 02\n \t1. Jeeva \n \t2. Edison") 
print("-"*80)
print("\tCryptocurrency Portfolio Application Main Menu")
print("-"*80)
intro_text="""1. Display Cryptocurrency
2. Add Cryptocurrency
3. Amend Cryptocurrency
4. Remove Cryptocurrency
5. Crypto Portfolio Statement
6. <Student 1 to propose a new function>
7. <Student 2 to propose a new function>
E. Exit Main Menu"""


print(intro_text)
print("-"*80)
option=input("Select an option: ")


#Cryptocurrency List
list=[["No","Name", "Capitalization", "QtyBought", "Bought Price", "Current Price"],
[1, "Bitcoin", "High", 15, 38000, 62000],
[2, "Ethereum", "High", 90, 4200, 3500],
[3, "Solana", "Mid", 60, 260, 110],
[4, "Decentraland", "Mid", 30000, 1.5, 5],
[5, "The Sandbox", "Mid", 25000, 2, 4],
[6, "Dogecoin", "Low", 55000, 0.4, 0.15]]

#OPTION 1
spaceneed=10
#must make function that can print number of spaces 
def space(x):
    return (" "*x)
#rmb can do string multiplication , dont use for loop as the x doest change properly 
while True:
    if option.lower()=='e':
        break
    elif option.isnumeric():
        if int(option) <=7 and int(option) >=1:
            break
    option=input("Please select one of the available options: ")


if option.lower()=='e':
    print("Exited ")
elif int(option)== 1:
    #thinking process: u need a set number of spaces , so number of space- length of word 
    for row in list:
        printedrow = ''
        #print(str(list[list.index(row)][0])+str(space(5-len(str(list[list.index(row)][0])))),str(list[list.index(row)][1])+str(space(15-len(str(list[list.index(row)][1])))), str(list[list.index(row)][2])+str(space(15-len(str(list[list.index(row)][2])))), str(list[list.index(row)][3])+str(space(15-len(str(list[list.index(row)][3])))), str(list[list.index(row)][4])+str(space(15-len(str(list[list.index(row)][4])))), str(list[list.index(row)][5])+str(space(9-len(str(list[list.index(row)][0])))))
        for col in row:
            if row.index(col)== 0:
                printedrow += str(col).ljust(7)
            else:
                printedrow += str(col).ljust(17)
        print(printedrow)

#OPTION 2
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

#OPTION 3
elif int(option) == 3:
'''

#Importing Modules



#Initialising Variables
option = ""

exit = False

input_string = "Select an option: "

list=[["No","Name", "Capitalization", "QtyBought", "Bought Price", "Current Price"],
[1, "Bitcoin", "High", 15, 38000, 62000],
[2, "Ethereum", "High", 90, 4200, 3500],
[3, "Solana", "Mid", 60, 260, 110],
[4, "Decentraland", "Mid", 30000, 1.5, 5],
[5, "The Sandbox", "Mid", 25000, 2, 4],
[6, "Dogecoin", "Low", 55000, 0.4, 0.15]]

list2 = ["Index","Name","Market Cap","Quantity Bought","Buy In Price","Market Price","E. Edit Complete. Exit"]

#Menu Display
def Menu():
    print("-"*80)
    print("\tClass 02\n \t1. Jeeva \n \t2. Edison") 
    print("-"*80)
    print("\tCryptocurrency Portfolio Application Main Menu")
    print("-"*80)
    intro_text="""    1. Display Cryptocurrency
    2. Add Cryptocurrency
    3. Amend Cryptocurrency
    4. Remove Cryptocurrency
    5. Crypto Portfolio Statement
    6. <Student 1 to propose a new function>
    7. <Student 2 to propose a new function>
    E. Exit Main Menu"""

    print(intro_text)
    print("-"*80)

#Option 1: Display Cryptocurrency 
def DisplayCrypto():
    for row in list:
        printedrow = ''
        #print(str(list[list.index(row)][0])+str(space(5-len(str(list[list.index(row)][0])))),str(list[list.index(row)][1])+str(space(15-len(str(list[list.index(row)][1])))), str(list[list.index(row)][2])+str(space(15-len(str(list[list.index(row)][2])))), str(list[list.index(row)][3])+str(space(15-len(str(list[list.index(row)][3])))), str(list[list.index(row)][4])+str(space(15-len(str(list[list.index(row)][4])))), str(list[list.index(row)][5])+str(space(9-len(str(list[list.index(row)][0])))))
        for col in row:
            if row.index(col)== 0:
                printedrow += str(col).ljust(7)
            else:
                printedrow += str(col).ljust(17)
        print(printedrow)
    print("-"*80)
    input("Press Enter to Continue")

#Option 2: Add CryptoCurrency
def AddCrypto():
    f = len(list)
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
    empty = [f, a, b.capitalize(), c, d, e]
    list.append(empty)
    print("-"*80)
    input("Addition Successful! Press Enter to Continue")

#Option 3: Amend CryptoCurrency
def AmendCrypto():
    print('No - CryptoCurrency')
    print('-'*80)
    for i in range(len(list)):
        if i == 0:
            continue
        print(i ,"-", list[i][1])
    input_string = "Enter 1 to " + str(len(list)-1) +  " for your selection or 'E' to exit: "
    print('-'*80)
    while True:
        x = input(input_string)
        if x.isnumeric(): #Checking if input is numeric
            if int(x) < 1 or int(x)>len(list)-1: #checking for out of range
                input_string = "Please only input 1 to " + str(len(list)-1) +  " for your selection or 'E' to exit: "
                continue
            else:
                break
        elif x.isalpha():
            if x.upper() == 'E': #check for E
                break
            else: #check for other alphabetical input that is not E
                input_string = "Please only input 1 to " + str(len(list)-1) +  " for your selection or 'E' to exit: "
                continue
      
            
    for i in range(len(list[int(x)])):
        print(str(i) +'.',list2[i].ljust(25)+':',list[int(x)][i])
    print(list2[6])
    
    input_string2 = "What do you want to edit?: "
    while True:
        y = input(input_string2)
        if y.isnumeric(): #Checking if input is numeric
            if int(y) < 1 or int(y)>len(list2)-2: #checking for out of range
                input_string2 = "Please only input 1 to " + str(len(list2)-2) +  " for your selection or 'E' to exit: "
                continue
            else:
                break
        elif y.isalpha():
            if y.upper() == 'E': #check for E
                break
            else: #check for other alphabetical input that is not E
                input_string2 = "Please only input 1 to " + str(len(list2)-2) +  " for your selection or 'E' to exit: "
                continue
    input_string3 = '('+y+') '+'Enter new '+ list2[int(y)]+ ' of Crypto:'
    list[int(x)][int(y)] = input(input_string3)
    input("Amendment Successful! Press Enter to Continue")


#Option 4: Remove CryptoCurrency
def RemoveCrypto():
    print('why')

#Option 5: Crypto Portfolio Statement
def CryptoPortfolioStatement():
    print('why')

#Option 6: Student 1
def Student1():
    print('why')

#Option 7: Student 2
def Student2():
    print('why')


while True:
    Menu()
    option = input(input_string)
    input_string = "Select an option: "
    match option:
        case "1":
            DisplayCrypto()

        case "2":
            AddCrypto()
            
        case "3":
            AmendCrypto()

        case "4":
            break
        case "5":
            break
        case "6":
            break
        case "7":
            break
        case "E":
            break
        case _:
            input_string = "Please select an existing option: "
            
        