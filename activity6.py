#Choosing the upto where the even numbers
b = int(input("Enter the ending number: "))

for even in range (2,b,2):
    print(even, end= " ")
print ("\n")

#for multiplication
#i is number from 1-3 whose multiplications would be shown
for i in range (1,4):
    print(f'multiplication table of {i}')
    for j in range (1,11):
        print(f'{i} x {j} = {i*j}')
print("\n")

#for reversed verion
string = input("Enter the word that you want to reverse: ")
rev = " "
print ("Reversed verion:", end=" ")
for ch in string:
   rev= ch + rev 
print(rev, end=" ")