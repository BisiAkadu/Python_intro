listofitems=['mango', 'orange', 'cocoa', 'banana', 'watermelon']
basket=[]
for i in listofitems:
    #print(i)
    basket.append(i)
    print(basket)
    
    #writing a python code that can loop through number list and collate them
    listofnumbers=[1,2,3,4,5,6,7,8,9,11]
    sum=0
    for k in listofnumbers:
        sum=sum+k
        print(sum)
        
    #write python code that will loop thru numberlist, add them and put a threshold
    listofno=[1,2,3,4,5,6,7,8,9,11]
    sumr=0
    for k in listofno:
        sumr=sumr+k
        print(sumr)
        if sumr==21:
            print("it works")
            break
