# Initial value of sum
sum = 0

while sum <= 100: #only continuing the loop if the sum is less than 100
    n = input("Enter the number for sum (or space and enter to quit): ")

    #breaking the loop when the user enters space
    if n == " ":
        break

    #converting the user input into float for the calculation
    n1 = float(n)
    sum += n1
    print(f'The total sum is {sum:.2f}')

#printing the total sum before exiting
print(f'The total sum of the numbers is {sum:.2f}. BYE')