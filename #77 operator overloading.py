class Vector:
    def __init__(self):
        self.i=int(input("Enter the Value of i: "))
        self.j=int(input("Enter the Value of j: "))
        self.k=int(input("Enter the value of k: "))

    def __add__(self,x):
        result=Vector.__new__(Vector)
        result.i=self.i+x.i
        result.j=self.j+x.j
        result.k=self.k+x.k
        return result
    # def __add__(self,x):
    #     return f"{self.i+x.i}+{self.j+x.j}+{self.k+x.k}"
    # def __add__(self,x):
    #     return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
p=Vector()
print(p)
s=Vector()
print(s)
print(p+s)
