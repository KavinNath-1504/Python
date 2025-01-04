#Ascending and Descending order
mainList = [687, 68, 65874, 251, 367221]
descendingOrder = []
ascendingOrder = []

def ascending():

    localCopyMain = mainList.copy()
    localCopyAsc = ascendingOrder.copy()

    while localCopyMain:
        smallest = localCopyMain[0]
        for number in localCopyMain:
            if number < smallest:
                smallest = number
        localCopyAsc.append(smallest)
        localCopyMain.remove(smallest)
    

    print("The smallest number in the list is: ", localCopyAsc[0])
    print("ascending order = ", localCopyAsc)
    
def descending():
    localCopyMain = mainList.copy()
    localCopyDes = descendingOrder.copy()

    while localCopyMain:
        largest = localCopyMain[0]
        for number in localCopyMain:
            if number > largest:
                largest = number
        localCopyDes.append(largest)
        localCopyMain.remove(largest)
    

    print("The largest number in the list is: ", localCopyDes[0])
    print("Descending order = ", localCopyDes)

ascending()
descending()
print("Main list = ", mainList)