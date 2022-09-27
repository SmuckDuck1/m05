
def monthly_sales():

    stateTax = .05
    countyTax = .025
    total_sales = float(input("Enter total sales tax: "))

    State_tax = stateTax * total_sales
    print("state tax is", format(State_tax, '.2f'))

    county_tax = countyTax * total_sales
    print("county tax is", format(county_tax, '.2f'))

    total_sales_tax = State_tax + county_tax
    print("total sales tax is", format(total_sales_tax, '.2f'))

monthly_sales()



