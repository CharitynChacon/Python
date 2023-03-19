#Project 
#Income tax calculator

grossIncome= float(input("Enter the gross income: "))
taxpayer=grossIncome
flatrate= 0.2
standarddeduction= 10000
deduction= 3000
dependents= int(input("Enter the number of dependents: "))

calculation= (taxpayer-standarddeduction-(dependents*deduction))*flatrate
print("The income tax is $",calculation)