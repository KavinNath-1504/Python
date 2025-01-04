#Program to reverse a list
mainList = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]

def main():
    localMain = mainList.copy()
    reverseList = []

    for number in mainList:
        reverseList.append(localMain[-1])
        localMain.remove(localMain[-1])

    print(reverseList)

main()