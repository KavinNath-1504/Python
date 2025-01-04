#Duplicates in a list
mainList = [1, 22 ,198, 867, 578, 879, 45011]

oddList = []
evenList = []

def main():
    localMain = mainList.copy()
    for number in mainList:
        if number%2 == 0:
            evenList.append(number)
        else:
            oddList.append(number)


    print("Even List: ", evenList)
    print("Odd List: ", oddList)

print("Main List: ", mainList)

main()