#Min is the minimum wage 
min = 18 

pay= float(input("Enter your wage per hour: "))

#creating boolean variable
Min_is_more_than_pay= True
Min_is_less_than_pay= False

print ("logical Operations:")
print ("pay>=min AND pay<=min:", pay >= min and pay <= min )
print ("pay>=min OR pay<=min:", pay >= min or pay <= min)
print ("NOT pay>=min:", not pay >= min)

if pay>=min:
    print("\nIt is greater than minimum wage. You are aware about labor act.")
else:
    print("\nIt is less than minimun wage. You are being expolited. ")