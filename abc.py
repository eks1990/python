persons={"name":"A", "age":"35", "height":"6 feet", "education":"BE", "hobbies":"sports"}
print(persons["name"])
print(persons.get("age"))
#print(type(persons))
#print(persons)\
persons["email"]="a@gmail.com"
persons["age"]="30"
persons.update({"age":"25"})
persons.pop("height")
persons.popitem()
persons.popitem()
print(persons)
