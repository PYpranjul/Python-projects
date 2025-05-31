A = float(input("Enter the Num: "))
match A:
    case 0:
        print(A,"Arayabhatt Zindabad")
    case _  if (A>=1):
        print(A,"Num is +")
    case _ if(A<=0):
        print(A,"Num is -")
    case _:
        print("Invalid")
