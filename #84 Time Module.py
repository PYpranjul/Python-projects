import time
# def loop():
#     i=0
#     while i<20:
#         i=i+1
#         print("While")
# def forloop():
#     i=0
#     for i in range (20):
#         print(i+1)
#         i+1


# init=time.time()

# p=loop()
# print(time.time() - init)
# init=time.time()

# p=forloop()
# print(time.time() - init)

print ("wait start")
time.sleep(2)
print("it will take 10 sec to print")
print(time.localtime())
print(time.strftime("%H:%M:%S"))