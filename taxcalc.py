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

# [-] --- DELETION: MICHAEL BOYER, 18 APR 2025 ---
# purchase_amount = float(input("Enter purchase amount: ")
# )

# [+] --- ADDITION: MICHAEL BOYER, 18 APR 2025 ------
# Better formatting for input prompt; new input validation logic
# Initialize purchase_amount and validity of input as inherently false
purchase_amount = 0.0
valid = False

# While the input is not valid (can't be converted to a float), prompt the
# user to enter a valid input
while not valid:
      try:
            purchase_amount = float(input("Enter purchase amount (i.e. 200): $"))
            valid = True
      except ValueError:
            print("Invalid input. Please enter a numerical value for purchase amount.")

# [-] --- DELETION: MICHAEL BOYER, 18 APR 2025 ---
# stateTax = 0.05 * purchase_amount

# [+] ------ ADDITION: MICHAEL BOYER, 18 APR 2025 ------
# Add the new tax graduation logic
# If the purchase is less than $100, half the tax rate is applied
if purchase_amount <= 100:
      stateTax = (0.05 / 2) * purchase_amount
# Otherwise, if it's less than $500, the tax rate is 3/4 of the full rate
elif purchase_amount <= 500:
      stateTax = (0.05 / 2) * 100 + (0.05 * 3/4) * (purchase_amount - 100)
# And finally, if it's more than $500, the tax rate is full rate
else:
      stateTax = ((0.05 / 2) * 100 + (0.05 * 3/4) * 400 + 0.05 * (purchase_amount - 500))

countyTax = 0.025 * purchase_amount
totalTax = stateTax + countyTax
totalSale = purchase_amount + totalTax
# [-] --- DELETION: MICHAEL BOYER, 18 APR 2025 ---
# print("Purchase_amount" + format(purchase_amount.2f","), \
# "state tax: $" + format(stateTax.2f" ,"), county tax : $" + \
# format(countyTax.2f" ,"), Total tax: $" + format(totalTax.2f", "), \
# "Total sales: $" + format(totalSale.2f" ,") )

# [+] ------ ADDITION: MICHAEL BOYER, 18 APR 2025 ------
# Corrected formatting syntax, moved values to new lines,
# corrected "Purchase_amount" to "Purchase amount"
print("Purchase amount: $" + format(purchase_amount, ".2f"),
      "\nState tax: $" + format(stateTax, ".2f"), "\nCounty tax: $" +
      format(countyTax, ".2f"), "\nTotal tax: $" + format(totalTax, ".2f"),
      "\nTotal sales: $" + format(totalSale, ".2f"))
