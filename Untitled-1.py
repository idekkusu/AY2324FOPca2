#filePath = r"C:\Users\jeeva\OneDrive\Documents\CA2 elective list.csv"
filePath = "C:\\Users\\USER\\Downloads\\CA2 elective list.csv"




file = open(filePath,encoding='utf-8-sig')
data = file.readlines()


cryptolist = []
cryptolistheader = data[0]
cryptolistheader = cryptolistheader.split(",")
for i in range(len(cryptolistheader)):
    cryptolistheader[i] = cryptolistheader[i].strip('\n')

print(cryptolistheader)


CryptoList = []
for i in range(len(data)-1):
    line = data[i+1]
    line = line.split(",")

    count = 0
    AppendDict = {}
    for r in line:
        AppendDict[cryptolistheader[count]] = r.strip('\n')
        count+=1
    CryptoList.append(AppendDict)

print(CryptoList)


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
