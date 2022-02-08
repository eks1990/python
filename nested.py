persons={"p1":{"name":"A", "age":"35", "height":"6 feet", "education":"BE", "hobbies":"sports"}, 
"p2":{"name":"B", "age":"33", "height":"5 feet", "education":"BE", "hobbies":"xy"}, 
"p3":{"name":"C", "age":"37", "height":"5.5 feet", "education":"BE", "hobbies":"xyz"}}

#print(persons) # printining all contet of dictionary
print(persons.get("p1").get("name"), persons.get("p1").get("age") )

x =int( persons.get("p1").get("age"))
print(x)

if x > 20:
    print("old age")
else:
    print("teenage")