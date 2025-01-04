cnt = int(input("Enter the size of arrays: "))
arrays = []


for i in range(cnt):
    length = int(input("Enter the length of the array you want: "))
    array = [input(f"Enter the elements of array {j+1}" for j in range(length))]
    arrays.append(array)

print(arrays)