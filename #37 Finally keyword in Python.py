def fun():
    try:
        A=[9,0,8,4,77]
        i=int(input("Enter the index: "))
        print(A[i])
    except ValueError:
        print("Num is not Valid")
    except IndexError:
        print("Out of Range")
    finally:
        print(i)
p=fun()