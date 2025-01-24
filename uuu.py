#Min is the minimum wage 
Min = 18 
pay= float(input("Enter your wage per hour: "))

#creating boolean variable
Min_is_more_than_pay= Min>=pay = True
Min_is_less_than_pay= Min<=pay = False

print ("logical Operations:")
print ("Min_is_more_than_pay AND Min_is_less_than_pay:", Min_is_more_than_pay and Min_is_less_than_pay )
print ("Min_is_more_than_pay OR Min_is_less_than_pay:", Min_is_more_than_pay or Min_is_less_than_pay)
print ("NOT Min_is_more_than_pay", not Min_is_more_than_pay)

if Min_is_more_than_pay:
    print("\nIt is less than minimun wage. You are being expolited. ")
    
else:
   print("\nIt is greater than minimum wage. You are aware about labor act.")
