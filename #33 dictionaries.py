dict={"p32218": "Pranjul","p24891": "Pooja mam","A24123":"Anjesh sir"}
print(dict["A24123"])
##print(dict["Anjesh sir"])
##print(dict.get("p32218"))
##print(dict.get("P32218"))           #this will not give error if it is not there
##print(dict.keys())
for key in dict.keys():
    print(key)
    print(dict[key])
    print(dict.values())
##    print(dict.values())
##    print(dict.keys())
##    print(dict[key])
    print(f"The employee code of {dict[key]} is {key}")
print(dict.items())
