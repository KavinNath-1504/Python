import time
class taskManager():
    def __init__(self):
        self.tasks = []

    def stuffToPrint(self):
        if self.tasks:
            print("Your list:")
            for index, item in enumerate(self.tasks, start= 1):
                time.sleep(0.75)
                print(f"{index}. {item}", flush=True)
        else:
            print("There is nothing to print. The list is empty 😅")    
    def viewTask(self):
        self.stuffToPrint()   
    def addTask(self):
        task = str(input("Enter your task:\n"))
        self.tasks.append(task)
        print("Task successfully added.")
        self.stuffToPrint()
    def removeTasks(self):
        if self.tasks:
            try:
                self.stuffToPrint()
                indice = int(input("Enter the index of the item you want to remove: ")) 
                if 1 <= indice <= (len(self.tasks)):
                    self.tasks.pop(indice-1)
                    self.stuffToPrint()
                else:
                    print("Value is not within the range of the list.")
            except ValueError:
                print("Please enter a integer within the range.")    
    def clearTasks(self):
        if self.tasks:
            self.tasks.clear()
        else:
            print("The list is already empty.")    
def main():
    taskmanager = taskManager()
    while True:    
        print("What do you want to do?\n 1. View list\n 2. Add to list\n 3. Remove list items\n 4. Clear list\n 5. Quit")
        choice = str(input("Enter your input: ").strip())
        if choice == "1":
            taskmanager.viewTask()
        elif choice == "2":
            taskmanager.addTask()
        elif choice == "3":
            taskmanager.removeTasks()
        elif choice == "4":
            taskmanager.clearTasks()
        elif choice == "5":
            print("Exiting the program", end="", flush=True)
            for dot in "...":
                time.sleep(0.5)
                print(dot, end="", flush=True)
            time.sleep(0.5)
            print(" Done.")
            break
        else:
            print("Enter a valid choice.")
if __name__ == "__main__":
    main()