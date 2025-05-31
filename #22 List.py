HDFC=[2,5,2,2,5,5,1,4151,33,65]
print(HDFC[0:8])
print(len(HDFC))
print(type(HDFC))
print(HDFC[0:11])
print(HDFC[0:11:3])
for i in HDFC:
    print(HDFC)
##lst=[i+i for i in range(8) if i==5]
##print(lst)
l= HDFC
l[4]=0
print(l)
m=[900,75]
l.extend(m)
print(l)
print(l+m)
