from re import X


empdata={
         "p1":["amit",2000,35], "p2":["smit",3000,25]   
}
#print(empdata["p1"])
for x in empdata:
    if x == "p1":
        y = empdata.get("p1")
        print(y[0])
    elif x=="p2":
        y=empdata.get("p2")
        print(y[0])

        