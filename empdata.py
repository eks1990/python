emp_db=[
    {"emp_id":"1", "emp_name":"Sumit", "emp_salary":"20000"},
    {"emp_id":"2", "emp_name":"Aumit", "emp_salary":"30000"},
    {"emp_id":"3", "emp_name":"Rumit", "emp_salary":"40000"},
   
]

for x in emp_db:
   if x.get("emp_id")=="1":
     print(x.get("emp_name"))
     x.update({"emp_email":"a@gmail.com"})
     print(x.get("emp_email"))