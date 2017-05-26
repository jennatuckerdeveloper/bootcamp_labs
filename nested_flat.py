lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#this is nested

for x in lst:
    print(x)

for x in lst:
    for i in x:
        print(i)

#we're avoiding:
#if x:
    #if z:
        #if c:
