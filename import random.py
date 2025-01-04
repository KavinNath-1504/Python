collection = [684, 787, 446, 6874, 654645564]
smallest = collection[0]
largest = collection[len(collection)-1]

def smallestNumber():
    global smallest
    for number in collection:
        if smallest < number:
            smallest = number
        else:
            pass
    print(smallest)

def largestNumber():
    global largest
    for number in collection:
        if largest > number:
            largest = number
        else:
            pass
    print(largest)

smallestNumber()
largestNumber()