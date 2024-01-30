Marks = [['Benny',89,45,55],["Robin",56,86,23],["Sally",88,81,73],["Aaron",35,75,29],["Simon",65,62,77]]
print(Marks[2][0] , Marks[2][1])

for i in Marks:
    print(i[0] , i[1])

for r in Marks:
    print(r[0],end=" ")
    total = 0
    for f in i:
        try:
            f = int(f)
            total+=f
        except:
            continue
    print(total/3)
