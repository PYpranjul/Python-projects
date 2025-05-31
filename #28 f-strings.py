A="Hey my name is {} and I am from {} My age is only {},my monthly salary is {}"
name="Pranjul"
place="Kannauj"
age=28
salary=50000000.9589
print(A.format(name,place,age,salary))
print(A.format(place,name,age,salary))
print(f"Hey my name is {name} and I am from {place} My age is only {age}")
print(A.format(name,place,age,salary))
print(f"Hey my name is {name} and I am from {place} My age is only {age},my monthly salary is {salary: .2f}")
print(f"Hey my name is {{name}} and I am from {{place}} My age is only {{age}},my monthly salary is {salary: .2f}")
