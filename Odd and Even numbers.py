def main():
    numbers = [5, 6, 54, 6857.687, 70.000,  456, 3748]
    even = []
    odd = []
    for number in numbers:
        quotient = number/2
        if quotient == int(quotient):
            even.append(number)
        else:
            odd.append(number)
    print(f'The list of odd numbes in the given list are {odd}.')
    print(f'The list of even number in the given list are {even}.')
    
main()