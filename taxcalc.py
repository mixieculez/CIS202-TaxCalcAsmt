# Name: Michael Boyer
#
# Organization: CIS 202 - 302
#
# Description: This program calculates the total tax for a purchase amount
# based on the new tax law effective 1 July 2025. The tax applied to sales
# is based on the purchase amount. State tax is half of usual tax for the
# first $100. 3/4th of the tax for each additional $100 up to $500. Full
# amount after $500. Adjusted for inflation each year.
#
# Givens:
#
# Inputs:
#
# Outputs:
#
# Processes:
#
# Begin your program after this line

# Michael Boyer (04/20/2025)
# Initialize variables for validity check and user input
purchase_amount = 0.0
valid = False
# ----------

# [-] Removed by Michael Boyer (04/20/2025)
# purchase_amount = float(input("Enter purchase amount: ")
# )
# ----------

# Michael Boyer (04/20/2025)
# Replace old code for user input with validation logic
# Using the valid variable, we will only end the loop setting
# valid to True if the input does not raise a value error.
while not valid:
    try:
        purchase_amount = float(input("Enter purchase amount (i.e. 200): $"))
        valid = True
    except ValueError:
        print("Invalid input. Please enter a numerical value for purchase amount.")
# ---------

# [-] Removed by Michael Boyer (04/18/2025)
# stateTax = 0.05 * purchase_amount
# ---------

# Michael Boyer (04/18/2025)
# Replaced old code with new logic on graduated tax rates.

# If the purchase amount is less than or equal to 100, then the tax rate is half
if purchase_amount <= 100:
    stateTax = (0.05 / 2) * purchase_amount

# If the purchase amount is less than or equal to 500, then the tax rate is half
# for the initial $100 from the total purchase amount, and 3/4 the rate for the
# remaining amount
elif purchase_amount <= 500:
    stateTax = (0.05 / 2) * 100 + (0.05 * 3/4) * (purchase_amount - 100)

# And if the purchase amount is greater than 500, then the tax rate is half for the initial
# $100 from the total purchase amount, 3/4 the rate for the next $400, and full rate for
# the remaining amount
else:
    stateTax = ((0.05 / 2) * 100 + (0.05 * 3/4) * 400 + 0.05 * (purchase_amount - 500))
# ---------

countyTax = 0.025 * purchase_amount
totalTax = stateTax + countyTax
totalSale = purchase_amount + totalTax

# [-] Removed by Michael Boyer (04/17/2025)
# print("Purchase_amount" + format(purchase_amount.2f","), \
# "state tax: $" + format(stateTax.2f" ,"), county tax : $" + \
# format(countyTax.2f" ,"), Total tax: $" + format(totalTax.2f", "), \
# "Total sales: $" + format(totalSale.2f" ,") )
# ------------

# Michael Boyer (04/17/2025)
# Fixed incorrect syntax for the previous print statement and
# added new lines on each tax component for readability
print("Purchase amount: $" + format(purchase_amount, ".2f"),
    "\nState tax: $" + format(stateTax, ".2f"), "\nCounty tax: $" +
    format(countyTax, ".2f"), "\nTotal tax: $" + format(totalTax, ".2f"),
    "\nTotal sales: $" + format(totalSale, ".2f"))
# -------------
