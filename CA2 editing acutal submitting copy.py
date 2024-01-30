#Importing Libraries (copy , from rich import printprint("[bold red]This text is bold and red.[/bold]")) 
import copy 
import csv

#Initialising Variables
option = ""

exit = False

input_string = "Select an option: "

cryptolist2 = ["Index","Name","Market Cap","Quantity Bought","Buy In Price","Market Price","E. Edit Complete. Exit"]

#Importing Data from CSV into a 2D List

#filePath = r"C:\Users\jeeva\OneDrive\Documents\CA2 elective list.csv"
filePath = "C:\\Users\\USER\\Downloads\\CA2 elective list.csv"
#filePath = "C:\\Users\\Edison\\Downloads\\CA2 elective list.csv"

file = open(filePath,encoding='utf-8-sig')
data = file.readlines()
cryptolist = []
for i in range(len(data)):
  line = data[i]
  cols = line.split(",")
  name = cols[0] #start from 1 to ignore 1st line which is the header
  Capitalization = cols[1].strip()
  QtyBought=cols[2].strip()
  Bought_Price=cols[3].strip()
  Current_Price=cols[4].strip()
  x=[name,Capitalization,QtyBought,Bought_Price,Current_Price]
  cryptolist.append(x)
print(cryptolist)

#Update External Data Storage
def Update():
    #filePath = r"C:\Users\jeeva\OneDrive\Documents\CA2 elective list.csv"
    filePath = "C:\\Users\\USER\\Downloads\\CA2 elective list.csv"
    file = open(filePath, 'w',encoding='UTF8', newline='')
    writer = csv.writer(file)
    for i in cryptolist:
        writer.writerow(i)
    file.close()


#Main Menu Display
def Menu():
    print("-"*80)
    print("\tClass 02\n \t1. Saravanan Jeeva 2215338  \n  \t2. Edison Khoo Yi Sheng 2119122") 
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
    count = 0
    for row in option1cryptolist:
        printedrow = ''
        if count == 0:
            printedrow += "No.".ljust(5)
        else: 
            printedrow += str(count) + ".".ljust(5)
        for col in row:
            printedrow += str(col).ljust(17)
        count +=1
        print(printedrow)
    print("-"*80)
    input("Press Enter to Continue")


#Option 2: Add CryptoCurrency
def AddCrypto():
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
    empty = [a.capitalize(), b.capitalize(), c, d, e]
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
                                            restart = 0
                                            z = input(input_string3)
                                            for i in cryptolist:
                                                if z.title() in i:
                                                    input_string3 = z.title() + " already exists, please enter a new cryptocurrency: "
                                                    restart = 1
                                            if z == "":
                                                input_string3 = "Please key in a valid Name: "
                                                restart = 1
                                            if restart == 1:
                                                continue
                                            cryptolist[int(x)][int(y)-1] = z.capitalize()
                                            input("Amendment Successful! Press Enter to Continue")
                                            break

                                    case "2":
                                        input_string3 = "(2) Enter new Market Cap of Crypto: "
                                        while True:
                                            z = input(input_string3)
                                            casecryptolist=("high","low","mid")#using this ignores the bracket nonsense1
                                            if z.lower() not in casecryptolist:
                                                input_string3 = "Please key in a valid edit (High, Low, Mid): "
                                                continue
                                            z = z.capitalize()
                                            break
                                        cryptolist[int(x)][int(y)-1] = z
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
                                                cryptolist[int(x)][int(y)-1] = z
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
                                                cryptolist[int(x)][int(y)-1] = z
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
                                                cryptolist[int(x)][int(y)-1] = z
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
        #remind edison to look at this
def CryptoPortfolioStatement():
    #making a cryptolist that wouldnt change 
    option5cryptolist=copy.deepcopy(cryptolist)
    currentadditioncryptolist=[]
    totalvalue=[]
    for i in range(1,len(cryptolist)):#starting at 1 since we dont take the headings in caluclation
        totalinvested = float(cryptolist[i][2]) * float(cryptolist[i][3])
        Sumcurrentvalue = float(cryptolist[i][2]) * float(cryptolist[i][4])
        currentadditioncryptolist.append(Sumcurrentvalue)
        totalvalue.append(totalinvested)
    v=["total invested  invested Portfolio  Total Current  Value Profit Loss current  Portfolio"]
    # [['total invested'], ['invested'], ['Portfolio'], ['Total'], 'Current'], ['Value'], ['Profit]', ['Loss' 'current'], ['Portfolio']]
    option5cryptolist[0].extend(v)
    for i in range(1,len(cryptolist)):#starting at 1 since we dont take the headings in caluclation5
        totalinvested = float(cryptolist[i][2]) * float(cryptolist[i][3])
        Sumcurrentvalue = float(cryptolist[i][2]) * float(cryptolist[i][4])
        profitloss=Sumcurrentvalue-totalinvested
        currentportfoilosize=Sumcurrentvalue/sum(currentadditioncryptolist)*100
        totalportfoilosize=totalinvested/sum(totalvalue)*100
        extrafunction=[totalinvested,str(round(totalportfoilosize,2))+"%",Sumcurrentvalue,profitloss,str(round(currentportfoilosize,2))+"%"]
        if len(option5cryptolist)==len(cryptolist):#here making sure the option5cryptolist doesnt add to itself ,only the first time it will extend. got a few issues tho 
            option5cryptolist[i].extend(extrafunction)
    sumlist=[]
    totalcurrentvaluelist=[]
    profitlosslist=[]
    for i in range(1,len(option5cryptolist)):
        sumlist.append(option5cryptolist[i][5])
        totalcurrentvaluelist.append(option5cryptolist[i][7])
        profitlosslist.append(option5cryptolist[i][8])
    for row_index, row in enumerate(option5cryptolist):
        printedrow = ''
        for col_index, col in enumerate(row):#got error, theres a spacing here + the first section supposed to be No
            if col_index == 0:         
                printedrow += str(row_index).ljust(7)
                printedrow += str(col).ljust(17)
            else:
                printedrow += str(col).ljust(17)
        print(printedrow)  # Right-align with 2 decimal places
    print("{:<75} {:<15} {:<33} {:<18}{:<8}".format("", "SUM", sum(sumlist), sum(totalcurrentvaluelist),sum(profitlosslist)))#so the brackets indicate how many spaces to put beteween the things , the commas added to make it eaiser 
    print("-"*80)
    input("Press Enter to Continue")

#Option 6: Student 1
def Student1():
    option5cryptolist=copy.deepcopy(cryptolist)# makes a list that doesnt change 
    currentadditioncryptolist=[]
    totalvalue=[]
    for i in range(1,len(cryptolist)):#starting at 1 since we dont take the headings in caluclation
        totalinvested = float(cryptolist[i][2]) * float(cryptolist[i][3])
        Sumcurrentvalue = float(cryptolist[i][2]) * float(cryptolist[i][4])
        currentadditioncryptolist.append(Sumcurrentvalue)
        totalvalue.append(totalinvested)
    v=["total invested  invested Portfolio  Total Current  Value Profit Loss current  Portfolio"]
    # [['total invested'], ['invested'], ['Portfolio'], ['Total'], 'Current'], ['Value'], ['Profit]', ['Loss' 'current'], ['Portfolio']]
    option5cryptolist[0].extend(v)
    for i in range(1,len(cryptolist)):#starting at 1 since we dont take the headings in caluclation5
        totalinvested = float(cryptolist[i][2]) * float(cryptolist[i][3])
        Sumcurrentvalue = float(cryptolist[i][2]) * float(cryptolist[i][4])
        profitloss=Sumcurrentvalue-totalinvested
        currentportfoilosize=Sumcurrentvalue/sum(currentadditioncryptolist)*100
        totalportfoilosize=totalinvested/sum(totalvalue)*100
        extrafunction=[totalinvested,str(round(totalportfoilosize,2))+"%",Sumcurrentvalue,profitloss,str(round(currentportfoilosize,2))+"%"]
        if len(option5cryptolist)==len(cryptolist):#here making sure the option5cryptolist doesnt add to itself ,only the first time it will extend. got a few issues tho 
            option5cryptolist[i].extend(extrafunction)
    option7cryptolist=[]
    #since we using the option 5 code again 
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
"""
#Option 7: Student 2
def Student2():
    print('No - CryptoCurrency')
    print('-'*80)
    for i in range(len(cryptolist)):
        if i == 0:
            continue
        print(i ,"-", cryptolist[i][0])
    input_string = "Enter Name of Cryptocurrency for your selection or 'E' to exit: "
    option_chosen = input(input_string)
    print('-'*80)

    import numpy as np
    import pandas as pd
    import torch
    import torch.nn as nn
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.model_selection import train_test_split
    from torch.utils.data import DataLoader, TensorDataset

    # Load your dataset
    try:
        df = pd.read_csv("Data/" + option_chosen + ".csv") 

    except:
        print("No Historical Data")
        return

    # Select the column to predict
    price = df['Close'].values.reshape(-1, 1)
    date = df['Date'].values.reshape(-1, 1)

    # Normalize the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    price_scaled = scaler.fit_transform(price)

    # Split data into X (features) and y (target)
    def create_dataset(data, time_step=1):
        X, y = [], []
        for i in range(len(data) - time_step - 1):
            a = data[i:(i + time_step), 0]
            X.append(a)
            y.append(data[i + time_step, 0])
        return np.array(X), np.array(y)

    time_step = 100
    X, y = create_dataset(price_scaled, time_step)

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Convert to PyTorch tensors
    X_train = torch.tensor(X_train).float().unsqueeze(-1)
    y_train = torch.tensor(y_train).float()
    X_test = torch.tensor(X_test).float().unsqueeze(-1)
    y_test = torch.tensor(y_test).float()

    # Create DataLoaders
    train_data = TensorDataset(X_train, y_train)
    test_data = TensorDataset(X_test, y_test)
    train_loader = DataLoader(train_data, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_data, batch_size=32, shuffle=False)

    class LSTMModel(nn.Module):
        def __init__(self, input_size=1, hidden_layer_size=50, output_size=1):
            super().__init__()
            self.hidden_layer_size = hidden_layer_size

            self.lstm = nn.LSTM(input_size, hidden_layer_size)

            self.linear = nn.Linear(hidden_layer_size, output_size)

        def forward(self, input_seq):
            lstm_out, _ = self.lstm(input_seq.view(len(input_seq), -1, 1))
            predictions = self.linear(lstm_out.view(len(input_seq), -1))
            return predictions[-1]

    model = LSTMModel()
    loss_function = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    epochs = 100

    for i in range(epochs):
        for inputs, labels in train_loader:
            optimizer.zero_grad()
            y_pred = model(inputs)
            single_loss = loss_function(y_pred, labels)
            single_loss.backward()
            optimizer.step()

    model.eval()
    test_predictions = []

    with torch.no_grad():
        for inputs, labels in test_loader:
            y_pred = model(inputs)
            test_predictions.append(y_pred.numpy())

    # Flatten the list of predictions
    test_predictions = np.array(test_predictions).flatten()

    # Invert predictions
    test_predictions = scaler.inverse_transform(test_predictions.reshape(-1, 1))

    import matplotlib.pyplot as plt

    def evaluate_model(y_true, y_pred, title='Model Evaluation'):
        """"""
        Plots the actual vs predicted values for model evaluation.

        Args:
        y_true (array-like): The actual values.
        y_pred (array-like): The predicted values from the model.
        title (str): The title of the plot.
        """"""
        plt.figure(figsize=(12, 6))
        plt.plot(y_true, label='Actual', color='blue')
        plt.plot(y_pred, label='Predicted', color='red')
        plt.title(title)
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.legend()
        plt.show()
    
    input("Press Enter to Continue")
"""

#MAIN PROGRAMME
    
while True:
    Menu()
    option = input(input_string).upper()
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
        case "7" :
            #tjs
        #case "E":
            Update()
            print("It has updated")
            break
        case _:
            input_string = "Please select an existing option: "


        