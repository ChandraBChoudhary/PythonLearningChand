Income = int(input("Enter your Income "))
Taxible_income = Income - 500000
if Taxible_income > 0 :
    TaxOnIncome = Taxible_income * 0.1
    print ("Your income is taxable :",TaxOnIncome)
else :
    print ("Your income is not taxable")
