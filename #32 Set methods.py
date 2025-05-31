s1={1,2,3,4,66,99,77,0}
s2={1,3,88,96,99,77}
s3={1,3,6,8,9}
s9={1,3}
##print(s1.union(s2))               # All values    
##print(s1.intersection(s2))        # Only common values
##s1.update(s3)                     # update the value of s3 in s1
##print(s1)
##print(s2)
##s2.intersection_update(s1)        # update the common values in s2 
##print(s2)
##print(s1,s2,s3)
##s4=s2.symmetric_difference(s3)    # removes common value
##print(s4)
##print(s1.difference(s3))             #S1-S3
##s1.difference_update(s3)            
##print(s1)
##print(s1.isdisjoint(s2))            # Any thing common or not
##print(s1.issuperset(s3))
##print(s3.issuperset(s9))
##print(s9.issubset(s3))
##s9.add(9)                           # add is used for adding single item and update we can use for more than one
##print(s9)
##s9.remove(3)                        # for removing use discard/remove
##print(s9)                           # Discard don't dont give error if item is not present in the set but Remove will give the errror
##s9.discard(9)
##print(s9)
a=s2.pop()
print(s2)
print(a)                              #randomly poping a value from the set
##del s2                                # delete the set
##print(s2)
##s1.clear()
##print(s1)
if 3 in s1:
    print("yes")
else:
    print("why")
