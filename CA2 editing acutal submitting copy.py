#Importing Libraries (copy , from rich import printprint("[bold red]This text is bold and red.[/bold]")) 
import copy 
import csv
import re

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
    print("\tClass 02\n \t1. Saravanan Jeeva (2215338)  \n  \t2. Edison Khoo Yi Sheng (2119122)\033[37m") 
    print("-"*80)
    print("\t\033[1m\033[33mCryptocurrency Portfolio Application Main Menu\033[22m\033[37m")
    print("-"*80)
    intro_text="""    1. \033[33mDisplay\033[37m Cryptocurrency
    2. \033[33mAdd\033[37m Cryptocurrency
    3. \033[33mAmend\033[37m Cryptocurrency
    4. \033[33mRemove\033[37m Cryptocurrency
    5. \033[33mCrypto Portfolio\033[37m Statement
    6. \033[33mWaterfall\033[37m Graph
    7. \033[33mPredict\033[37m Price of Cryptocurrency
    E. \033[31mExit\033[37m Main Menu"""

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
    print('\033[1m\033[33mNo - CryptoCurrency\033[22m\033[37m')
    print('-'*80)
    for i in range(len(cryptolist)):
        if i == 0:
            continue
        print(i ,"-", cryptolist[i][0])
    input_string = "Enter 1 to " + str(len(cryptolist)-1) +  " for your selection or '\033[31mE\033[37m' to exit: "
    print('-'*80)
    while True:
        x = input(input_string)
        if x.isnumeric(): #Checking if input is numeric
            if int(x) < 1 or int(x)>len(cryptolist)-1: #checking for out of range
                input_string = "Please only input 1 to " + str(len(cryptolist)-1) +  " for your selection or '\033[31mE\033[37m' to exit: "
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
                                input_string2 = "Please only input 1 to " + str(len(cryptolist2)-2) +  " for your selection or '\033[31mE\033[37m' to exit: "
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
                                input_string2 = "Please only input 1 to " + str(len(cryptolist2)-2) +  " for your selection or '\033[31mE\033[37m' to exit: "
                                continue
                    break

        elif x.isalpha():
            if x.upper() == 'E': #check for E
                break
            else: #check for other alphabetical input that is not E
                input_string = "Please only input 1 to " + str(len(cryptolist)-1) +  " for your selection or '\033[31mE\033[37m' to exit: "
                continue

#Option 4: Remove CryptoCurrency
def RemoveCrypto():
    print('\033[1m\033[33mNo - CryptoCurrency\033[22m\033[37m')
    print('-'*80)
    for i in range(len(cryptolist)):
        if i == 0:
            continue
        print(i ,"-", cryptolist[i][0])
    print('-'*80)
    input_string = "Enter 1 to " + str(len(cryptolist)-1) +  " for your selection or '\033[31mE\033[37m' to exit: "
    while True:
        x = input(input_string)
        if x.isnumeric() and (int(x) < 1 or int(x)>len(cryptolist)-1): #Checking if input is within numeric options
            input_string = "Please only input 1 to " + str(len(cryptolist)-1) +  " for your selection or '\033[31mE\033[37m' to exit: "
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
    v=["""Total        Invested          Total Current       Profit/Loss   Current
                                                                                          Invested       Portfolio Size       Value                         Portfolio size """]
    

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
    count1 = 0
    for i in range(1,len(option5cryptolist)):
        sumlist.append(option5cryptolist[i][5])
        totalcurrentvaluelist.append(option5cryptolist[i][7])
        profitlosslist.append(option5cryptolist[i][8])
    for row_index, row in enumerate(option5cryptolist):
        printedrow = ''
        for col_index, col in enumerate(row):#got error, theres a spacing here + the first section supposed to be No
            if col_index == 0:         
                if count1 ==0:
                    printedrow+= "No.".ljust(7)
                    count1+=1
                else:
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

#Option 7: Student 2
def Student2():

    #Display Table and Selection Prompt
    print('\033[1m\033[33mNo - CryptoCurrency\033[22m\033[37m')
    print('-'*80)
    for i in range(len(cryptolist)):
        if i == 0:
            continue
        print(i ,"-", cryptolist[i][0])
    print('-'*80)
    input_string = "Enter 1 to " + str(len(cryptolist)-1) +  " for your selection or '\033[31mE\033[37m' to exit: "
    while True: #Input validation
        crypto_chosen = input(input_string)
        if crypto_chosen.isnumeric() == False:
            print("Please key in a proper input")
            continue
        elif int(crypto_chosen) <= 0 or int(crypto_chosen)> (len(cryptolist)-1):
            print("Please key in a proper input")
            continue
        else:
            break
    option_chosen = cryptolist[int(crypto_chosen)][0]

#user input and input validation for date of prediction

    # Define the pattern for the date format 'yy/mm/dd'
    date_pattern = re.compile(r'^\d{2}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$')

    while True:
    # Get user input
        input_date_str = input("Please input the date in the format of yy/mm/dd: ")

        # Validate the input against the pattern and additional conditions
        if date_pattern.match(input_date_str):
            year, month, day = map(int, input_date_str.split('/'))
            
            # Check if month is between 1 and 12
            if 1 <= month <= 12:
                # Check if day is between 1 and 31
                if 1 <= day <= 31:
                    break
                    # Further processing or use the input_date_str as needed
        else:
            print("Invalid date format. Please ensure your input is in the format yy/mm/dd and that a valid date is chosen.")
            continue

    #Importing Modules. Import here so it can do the loading all at once.
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler
    from keras.models import Sequential
    from keras.layers import LSTM, Dense
    from sklearn.model_selection import train_test_split
    from datetime import timedelta
    import matplotlib.dates as mdates
    import matplotlib.pyplot as plt

    # Load the data
    cryptoDf = pd.read_csv("Data/" + option_chosen + ".csv")
    cryptoDf['Date'] = pd.to_datetime(cryptoDf['Date'])

    # Normalizing the 'Close' values
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_close = scaler.fit_transform(cryptoDf['Close'].values.reshape(-1, 1))

    # Define the time step
    time_step = 100
    X, y = [], []

    # Create sequences manually
    for i in range(time_step, len(scaled_close)):
        X.append(scaled_close[i - time_step:i, 0])
        y.append(scaled_close[i, 0])

    X, y = np.array(X), np.array(y)

    # Reshape input to be [samples, time steps, features]
    X = X.reshape(X.shape[0], X.shape[1], 1)

    # Calculate the split index
    split_idx = int(len(X) * 0.7)

    # Splitting the data into train and test sets
    X_train, X_test = X[:split_idx], X[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]

    # Create the LSTM model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(time_step, 1)))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dense(units=1))

    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=2)

    # Predictions
    train_predict = model.predict(X_train)
    test_predict = model.predict(X_test)

    # Inverse transform to get actual values
    train_predict = scaler.inverse_transform(train_predict)
    test_predict = scaler.inverse_transform(test_predict)


    def iterative_predictions(model, start_data, start_date, target_date, scaler, time_step):
        # Calculate the number of days to predict
        days_to_predict = (target_date - start_date).days

        # Prepare the initial input data
        current_input = start_data[-time_step:]

        # Iteratively predict the next price
        for _ in range(days_to_predict):
            # Reshape and predict the next point
            next_point = model.predict(current_input.reshape((1, -1, 1)))
            # Append the prediction and remove the first element
            current_input = np.append(current_input, next_point)[1:]

        # Inverse transform the last prediction to get the actual price
        predicted_price = scaler.inverse_transform(next_point)

        return predicted_price[0, 0]

    # Ensure 'Date' column is in datetime format
    cryptoDf['Date'] = pd.to_datetime(cryptoDf['Date'])

    # Input the target date for prediction
    input_date_str = '2023-01-01'  # Modify as per your requirement
    target_date = pd.to_datetime(input_date_str)

    # Ensure the target date is after the last date in your dataset
    last_date_in_data = cryptoDf['Date'].iloc[-1]
    if target_date <= last_date_in_data:
        print("Target date should be after the last date in the dataset.")
    else:
        # Get the most recent 'time_step' data points
        recent_data = scaled_close[-time_step:]

        # Predict the price for the target date
        predicted_price = iterative_predictions(model, recent_data, last_date_in_data, target_date, scaler, time_step)
        print(f"Predicted price for {input_date_str}: {predicted_price} USD")
        
    input("Press Enter to Continue")


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
            Student2()
        case "E":
            Update()
            print("The data has been updated")
            break
        case _:
            input_string = "Please select an existing option: "


        