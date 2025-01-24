#ask for the numeric grade input 
nGrade= float(input("Enter your numeric grade:"))

#converting numeric grade into corresponding letter grade
if nGrade >= 90: 
    lGrade= "A+"
    print (f'Your grade is', lGrade)
elif nGrade >= 80:
    lGrade= "A"
    print (f'Your grade is', lGrade)
elif nGrade >= 70:
    lGrade= "B"
    print (f'Your grade is', lGrade)
elif nGrade >= 60:
    lGrade= "C"
    print (f'Your grade is', lGrade)
elif nGrade >= 50:
    lGrade= "D"
    print (f'Your grade is', lGrade)
elif nGrade <50:     
    lGrade="F"
    print (f'Your grade is', lGrade)