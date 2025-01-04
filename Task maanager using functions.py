import time
def stuffToPrint():
    if tasks:
        print("Your list:")
        for index, item in enumerate(tasks, start= 1):
            time.sleep(0.75)
            print(f"{index}. {item}", flush=True)
    else:
        print("There is nothing to print. The list is empty 😅")
def taskManager():
    print("What do you want to do?\n 1. View list\n 2. Add to list\n 3. Remove list items\n 4. Clear list\n 5. Quit")
    choice = str(input("Enter your choice: "))
    if choice == "1":
        stuffToPrint()
    elif choice == "2":
        task = str(input("Enter your task:\n"))
        tasks.append(task)
        print("Task successfully added.")
        stuffToPrint()
    elif choice == "3":
        if tasks:
            stuffToPrint()
            indice = int(input("Enter the index of the item you want to remove: ")) 
            if 1 <= indice <= (len(tasks)):
                tasks.pop(indice-1)
                stuffToPrint()
            else:
                print("Value is not within the range of the list.")
    elif choice == "4":
        if tasks:
            tasks.clear()
            print("The list has been cleared.")
        else:
            print("There is nothing to clear. The list is already empty. 😅")
    else:
        print("Please select one of the five options.")
tasks = []
while True:
    taskManager()
    while True:
        print("Do you want to perform another operation?")
        cont = input("Yes/No: ").strip().lower()
        if cont == "no":
            print("Exiting the program", end="", flush=True)
            for dot in "...":
                time.sleep(0.5)
                print(dot, end="", flush=True)
            time.sleep(0.5)
            print(" Done.")
            break
        elif cont == "yes":
            break
        else:
            print("Please enter either Yes/No.")
    if cont == "no":
        break