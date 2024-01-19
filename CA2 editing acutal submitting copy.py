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


#Cryptocurrency cryptolist
cryptolist=[["No","Name", "Capitalization", "QtyBought", "Bought Price", "Current Price"],
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
    for row in cryptolist:
        printedrow = ''
        #print(str(cryptolist[cryptolist.index(row)][0])+str(space(5-len(str(cryptolist[cryptolist.index(row)][0])))),str(cryptolist[cryptolist.index(row)][1])+str(space(15-len(str(cryptolist[cryptolist.index(row)][1])))), str(cryptolist[cryptolist.index(row)][2])+str(space(15-len(str(cryptolist[cryptolist.index(row)][2])))), str(cryptolist[cryptolist.index(row)][3])+str(space(15-len(str(cryptolist[cryptolist.index(row)][3])))), str(cryptolist[cryptolist.index(row)][4])+str(space(15-len(str(cryptolist[cryptolist.index(row)][4])))), str(cryptolist[cryptolist.index(row)][5])+str(space(9-len(str(cryptolist[cryptolist.index(row)][0])))))
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
        for i in range(len(cryptolist)):
            if a.title() == cryptolist[i][1]:
                print(cryptolist[i][1], "already exists, please enter a new cryptocurrency")
                break
        else:
            break
    while True:
        b = input("Enter Market Cap of Crypto: High, Mid, Low :")
        casecryptolist=("high","low","mid")#using this ignores the bracket nonscne
        if b.lower() in casecryptolist:
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
    cryptolist.append(empty)

#OPTION 3
elif int(option) == 3:
Total Invested = Quantity x Buy In Price
• Invested Portfolio Size = Percentage of Total Invested/ Sum of Total Invested 
• Total Current Value = Quantity x Market Price
• Profit/ Loss = Total Current Value – Total Invested 
• Current Portfolio Size = Percentage of Total Current Value / Sum of Total Current Valu
'''
#random libraries we require , copy , rich for bolded text
import copy 

#Initialising Variables
option = ""

exit = False

input_string = "Select an option: "
a=r"C:\Users\jeeva\OneDrive\Documents\CA2 elective list.csv"
filePath=a
file = open(filePath,encoding='utf-8-sig')
data = file.readlines()
cryptolist = []
# start from 1 to ignore 1st line which is the header
for i in range(len(data)):
  line = data[i]
  cols = line.split(",")
  Number=cols[0]
  name = cols[1]
  Capitalization = cols[2].strip()
  QtyBought=cols[3].strip()
  Bought_Price=cols[4].strip()
  Current_Price=cols[5].strip()
  x=[name,Capitalization,QtyBought,Bought_Price,Current_Price]
  cryptolist.append(x)
print(cryptolist)
cryptolist2 = ["Index","Name","Market Cap","Quantity Bought","Buy In Price","Market Price","E. Edit Complete. Exit"]
#from rich import printprint("[bold red]This text is bold and red.[/bold]")"""

#Main Menu Display
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
    option1cryptolist=cryptolist.copy()
    for row in option1cryptolist:
        printedrow = ''
        for col in row:
            if True:
                printedrow += str(col).ljust(17)
        print(printedrow)
    print("-"*100)
    input("Press Enter to Continue")


#Option 2: Add CryptoCurrency
def AddCrypto():
    f = len(cryptolist)
    while True:
        a = input("Enter Cryptocurrency Name :")
        for i in range(len(cryptolist)):
            if a.title() == cryptolist[i][1]:
                print(cryptolist[i][1], "already exists, please enter a new cryptocurrency")
                break
        else:
            break
    while True:
        b = input("Enter Market Cap of Crypto: High, Mid, Low :")
        casecryptolist=("high","low","mid")#using this ignores the bracket nonscne
        if b.lower() in casecryptolist:
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
    cryptolist.append(empty)
    print("-"*80)
    input("Addition Successful! Press Enter to Continue")
    print(cryptolist)


#Option 3: Amend CryptoCurrency
def AmendCrypto():
    print('No - CryptoCurrency')
    print('-'*80)
    for i in range(len(cryptolist)):
        if i == 0:
            continue
        print(i ,"-", cryptolist[i][0])
    input_string = "Enter 1 to " + str(len(cryptolist)-1) +  " for your selection or 'E' to exit: "
    print('-'*80)
    while True:
        x = input(input_string)
        if x.isnumeric(): #Checking if input is numeric
            if int(x) < 1 or int(x)>len(cryptolist)-1: #checking for out of range
                input_string = "Please only input 1 to " + str(len(cryptolist)-1) +  " for your selection or 'E' to exit: "
                continue
            else: #If input is valid
                    i = 0
                    while i <= len(cryptolist[int(x)]):
                        if i != 0:
                            print(str(i) +'.',cryptolist2[i].ljust(25)+':',cryptolist[int(x)][i-1])
                        else:
                            print()
                            print(cryptolist2[i].ljust(25)+'   :',int(x))
                        i+=1
                    print(cryptolist2[6])
                    
                    input_string2 = "What do you want to edit?: "
                    while True:
                        y = input(input_string2)

                        if y.isnumeric(): #Checking if input is numeric
                            if int(y) < 1 or int(y)>len(cryptolist2)-2: #checking for out of range
                                input_string2 = "Please only input 1 to " + str(len(cryptolist2)-2) +  " for your selection or 'E' to exit: "
                                continue
                            else: #if y is a valid input and is not "E"
                                match y:
                                    case "1":
                                        input_string3 = "(1) Enter new Name of Crypto: "
                                        while True:
                                            z = input(input_string3)
                                            for i in range(len(cryptolist)):
                                                if z.title() == cryptolist[i][1]:
                                                    print(cryptolist[i][1], "already exists, please enter a new cryptocurrency")
                                                    input_string3 = str(cryptolist[i][1]) + " already exists, please enter a new cryptocurrency"
                                                    continue
                                            cryptolist[int(x)][int(y)] = z
                                            input("Amendment Successful! Press Enter to Continue")
                                            break
                                    case "2":
                                        input_string3 = "(2) Enter new Market Cap of Crypto: "
                                        while True:
                                            z = input(input_string3)
                                            casecryptolist=("high","low","mid")#using this ignores the bracket nonsense1
                                            if z.lower() not in casecryptolist:
                                                input_string2 = "Please key in a valid edit (High, Low, Mid)"
                                                continue
                                            z = z.capitalize()
                                            break
                                        cryptolist[int(x)][int(y)] = z
                                        input("Amendment Successful! Press Enter to Continue")
                                        break
                                        
                                    case "3":
                                        input_string3 = "(3) Enter new Quantity of Crypto Bought = "
                                        while True:
                                            z = input(input_string3)
                                            try:
                                                z = int(z)
                                            except ValueError :
                                                input_string3 = "Please key in a valid input: "
                                                continue
                                            else:
                                                cryptolist[int(x)][int(y)] = z
                                                input("Amendment Successful! Press Enter to Continue")
                                                break

                                    case "4":
                                        input_string3 = "(4) Enter new Buy In Price of Crypto = "
                                        while True:
                                            z = input(input_string3)
                                            try:
                                                z = float(z)
                                            except ValueError :
                                                input_string3 = "Please key in a valid input: "
                                                continue
                                            else:
                                                cryptolist[int(x)][int(y)] = z
                                                input("Amendment Successful! Press Enter to Continue")
                                                break
                                    case "5": 
                                        input_string3 = "(5) Enter new Market Price of Crypto = "
                                        while True:
                                            z = input(input_string3)
                                            try:
                                                z = float(z)
                                            except ValueError :
                                                input_string3 = "Please key in a valid input: "
                                                continue
                                            else:
                                                cryptolist[int(x)][int(y)] = z
                                                input("Amendment Successful! Press Enter to Continue")
                                                break
                                                
                                    case _:
                                        input_string2 = "Please input a valid option: "
                                        continue
                                break

                        elif y.isalpha():
                            if y.upper() == 'E': #check for E
                                break
                            else: #check for other alphabetical input that is not E
                                input_string2 = "Please only input 1 to " + str(len(cryptolist2)-2) +  " for your selection or 'E' to exit: "
                                continue
                    break

        elif x.isalpha():
            if x.upper() == 'E': #check for E
                break
            else: #check for other alphabetical input that is not E
                input_string = "Please only input 1 to " + str(len(cryptolist)-1) +  " for your selection or 'E' to exit: "
                continue
#Option 4: Remove CryptoCurrency
def RemoveCrypto():
    print('No - CryptoCurrency')
    print('-'*80)
    for i in range(len(cryptolist)):
        if i == 0:
            continue
        print(i ,"-", cryptolist[i][0])
    print('-'*80)
    input_string = "Enter 1 to " + str(len(cryptolist)-1) +  " for your selection or 'E' to exit: "
    while True:
        x = input(input_string)
        if x.isnumeric() and (int(x) < 1 or int(x)>len(cryptolist)-1): #Checking if input is within numeric options
            input_string = "Please only input 1 to " + str(len(cryptolist)-1) +  " for your selection or 'E' to exit: "
            continue
        elif x.isalpha() and x.upper()!= "E": # checking for other inputs
            input_string = "Please key in a valid input: "
            continue
        elif x.upper() == "E": # checking for E
            break
        else: #valid option
            cryptolist.pop(int(x))
            input("Your Choice has been Successfully Removed! Press Enter to Continue")
            break
        

#Option 5: Crypto Portfolio Statement

option5cryptolist=copy.deepcopy(cryptolist)#making a cryptolist that wouldnt change 
currentadditioncryptolist=[]
totalvalue=[]
for i in range(1,7):#starting at 1 since we dont take the headings in caluclation
    totalinvested = float(cryptolist[i][2]) * float(cryptolist[i][3])
    Sumcurrentvalue = float(cryptolist[i][2]) * float(cryptolist[i][4])
    currentadditioncryptolist.append(Sumcurrentvalue)
    totalvalue.append(totalinvested)
v=["total invested","invested ","Portfolio Size","Total Current","Value Profit/ Loss Current","Portfolio Size"]
option5cryptolist[0].extend(v)

for i in range(1,7):#starting at 1 since we dont take the headings in caluclation
    totalinvested = float(cryptolist[i][2]) * float(cryptolist[i][3])
    Sumcurrentvalue = float(cryptolist[i][2]) * float(cryptolist[i][4])
    profitloss=Sumcurrentvalue-totalinvested
    currentportfoilosize=Sumcurrentvalue/sum(currentadditioncryptolist)*100
    totalportfoilosize=totalinvested/sum(totalvalue)*100
    extrafunction=[totalinvested,str(round(totalportfoilosize,2))+"%",Sumcurrentvalue,profitloss,str(round(currentportfoilosize,2))+"%"]
    if len(option5cryptolist)==len(cryptolist):#here making sure the option5cryptolist doesnt add to itself ,only the first time it will extend. got a few issues tho 
        option5cryptolist[i].extend(extrafunction)
def CryptoPortfolioStatement():
    for row_index, row in enumerate(option5cryptolist):
        printedrow = ''
        for col_index, col in enumerate(row):#got error, theres a spacing here + the first section supposed to be No
            if col_index == 0:         
                printedrow += str(row_index).ljust(7)
                printedrow += str(col).ljust(17)
            else:
                printedrow += str(col).ljust(17)
        print(printedrow)


#Option 6: Student 1
def Student1():
    print('why')
    option7cryptolist=[]
    for i in range(1,len(option5cryptolist)):
        option7cryptolist.append(option5cryptolist[i][0])
        option7cryptolist.append(option5cryptolist[i][8])
    print(option7cryptolist)
    import plotly.graph_objects as go

    # Your cryptolist
    data_cryptolist = option7cryptolist
    # Convert the cryptolist to a dictionary
    data_dict = {data_cryptolist[i]: data_cryptolist[i + 1] for i in range(0, len(data_cryptolist), 2)}
    # Create cryptolists for x and y values
    x_values = list(data_dict.keys())
    y_values = list(data_dict.values())
    labels = ['{0}: {1}'.format(x, y) for x, y in zip(x_values, y_values)]
    # Create a waterfall chart
    fig = go.Figure(go.Waterfall(
        x = x_values,
        y = y_values,
        text = labels,
        measure = ["relative"] * len(x_values),
        base = 0,
        decreasing = {"marker":{"color":"Red"}},
        increasing = {"marker":{"color":"Green"}},
        totals = {"marker":{"color":"Blue"}}
    ))

    # Show the figure
    fig.show()

#Option 7: Student 2
def Student2():
    print('why')



#MAIN PROGRAMME
    
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
            RemoveCrypto()
        case "5":
            CryptoPortfolioStatement()
        case "6":
            Student1()
            break
        case "7":
            break
        case "E":
            break
        case _:
            input_string = "Please select an existing option: "
            
        