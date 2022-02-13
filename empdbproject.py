emp_db=[
    {"emp_id":"1", "emp_name":"Priyanka", "emp_salary":"41000"},
    {"emp_id":"2", "emp_name":"Harshada", "emp_salary":"42000"},
    {"emp_id":"3", "emp_name":"Pawan", "emp_salary":"43000"},
]

print("Select operation")
print("0.View All Employee Data:")
print("1.View Employee Data:")
print("2.Add New Employee Data:")
print("3.Update Existent Employee Data:")
print("4.Remove Employee data:")


while True:
   selected_val =input("Enter the choice:")
   if selected_val=="0":
       for x in emp_db:
           print(x)
  
   elif selected_val=="1":
        emp_ids=input("enter employee id:")
        for x in emp_db:
            if x.get("emp_id")==emp_ids:
                print(x)

   elif selected_val=="2":
       #db_len=(len(emp_db))
       print("enter new employee record")
       emp_ids=input("emp_id:")
       emp_names=input("emp_name:")
       emp_salaries=input("emp_salary:")
       recods={"emp_id:":emp_ids,"emp_name:":emp_names,"emp_salary:":emp_salaries}
       emp_db.append(recods)
       print(emp_db)

   elif selected_val=="3":
       emp_ids=input("enter emp_id:")
       keys_val=input("enter key:")
       update_val=input("update value:")
       for x in emp_db:
            if x.get("emp_id")==emp_ids:
               x.update({keys_val:update_val})
               print(x)

   elif selected_val=="4":
       emp_ids=input("enter employee id:")
       key_val=input("Remove info key value:")
       for x in emp_db:
           if x.get("emp_id")==emp_ids:
              x.pop(key_val)
              print(x)
   else:
       print("input is invalid")
   next_operation = input("Let's do next operation? (y/n): ")
   if next_operation == "n":
    break
    

