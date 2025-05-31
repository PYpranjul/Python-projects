countries_1 =("Singapur","Philippines","china","Bharat","Australia","England","America")
countries_2 =("Sri lanka","Bhutan","Nepal")
World = countries_1+ countries_2   #addition of tuple
print(World)
temp_1=list(countries_1)   #converting from tuple to list
temp_1.append("India")     #add in the end of the list
temp_1.pop(2)              #remove on index value
temp_1[1]="PHIL"           #replace on index place
countries_1=temp_1
print(countries_1)
b=countries_1.count("Australia")
print(b)
c=countries_1.index("Bharat")
print(c)
d=countries_1.index("Bharat",1,7)
print(d)
print(countries_1[2:6])
