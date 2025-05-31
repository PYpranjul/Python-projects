a=input("Enter the Message: ")
b=input("Enter the key:")
anew=a.split(" ")
if b=="code":
    code=[]
    for i in anew:
        if len(i)>=3:
            new=i[1:] + i[0]
            code.append(new)
        else:
            new=i[::-1]
            code.append(new)
    print(" ".join(code))
elif b=="decode":
    decode=[]
    for i in anew:
        if len(i)>=3:
            new=i[-1] + i[:-1]
            decode.append(new)
        else:
            new=i[::-1]
            decode.append(new)
    print(" ".join(decode))