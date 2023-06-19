space = float(input("enter the square feet of wall space to be painted: "))
unit_price = float(input("enter price of the paint per gallon: "))
unit_space = (space/115)
price_paint = unit_space * unit_price
price_labor = unit_space * 8 * 20
labor_hrs = unit_space * 8
total_cost = price_labor + price_paint

print()
print("The number of gallons of paint required: %.2f" %unit_space)
print("The hours of labor required: %.2f" %labor_hrs)
print("The cost of the paint: %.2f" %price_paint)
print("The labor charges: %.2f" %price_labor)
print("The total cost of the paint %.2f" %total_cost)