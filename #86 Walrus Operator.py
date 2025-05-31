# Dinner =list( )
# while True:
#     food=input("Enter what you want in dinner: ")
#     if food.strip().capitalize() == "Quit":
#         print(Dinner)
#         break
#     Dinner.append(food)

#Walrus Operator
Dinner=[]
while (food := input("What food do you like in Dinner?? ")) !="quit":
    # if food.strip().lower() == "quit":
    #     print(Dinner)
    #     break

    Dinner.append(food)
print(Dinner)