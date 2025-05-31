import time
##timestamp=int(input("Enter the time: "))
timestamp= time.strftime("%H:%M:%S")
print (timestamp)
timestamp = int(time.strftime("%H"))
print (timestamp)
if (timestamp >=5 and timestamp <10):
    print ("shab ji shubhprabhat")
elif (timestamp >=10 and timestamp <15):
    print ("shahb ji dupariya hai")
elif (timestamp >=15 and timestamp <20):
    print ("Sham hui gawa")
elif (timestamp>24):
    print("Shab ji dusre universe mein aa gye")
else:
    print("Goood night")
