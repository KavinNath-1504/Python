#Second largest number in a list
mainList = [65, 6587, 65876, 32]


def secondLargest():
    descending = []
    localMain = mainList.copy()

    while localMain:
        largest = localMain[0]
        for number in localMain:
            if number > largest:
                largest = number
        descending.append(largest)
        localMain.remove(largest)

    print("The second largest number in the list is:", descending[1])

secondLargest()