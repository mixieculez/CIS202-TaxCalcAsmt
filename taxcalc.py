#
# - New tax law effective 1 July 2025
# - Changes to program that will result in graduated level of enforcement
# - Tax applied to sales is based on the purchase amount
# - State tax is half of usual tax for the first $100.
# - 3/4th of the tax for each additional $100 up to $500.
# - Full amount after $500
# - Adjusted for inflation each year
#
# - Only change what is necessary to implement the new tax law
# - Only action you can take with existing code is to leave alone or comment it out
# - Continue to output the appropriate tax information
#

# [-] --- DELETION: MICHAEL BOYER, 18 APR 2025 ---
# Lack of input validation for user's input; readability issues
# purchase_amount = float(input("Enter purchase amount: ")
# )

# [+] --- ADDITION: MICHAEL BOYER, 18 APR 2025 ------
# Better formatting for input prompt; new input validation logic
purchase_amount = 0.0
valid = False
while not valid:
      try:
            purchase_amount = float(input("Enter purchase amount (i.e. 200): $"))
            valid = True
      except ValueError:
            print("Invalid input. Please enter a numerical value for purchase amount.")

# [-] --- DELETION: MICHAEL BOYER, 18 APR 2025 ---
# Need to add the new tax graduation logic
# stateTax = 0.05 * purchase_amount
# [-] --------------------------------------------

# [+] ------ ADDITION: MICHAEL BOYER, 18 APR 2025 ------
# Add the new tax graduation logic
# noinspection PyUnboundLocalVariable
if purchase_amount <= 100:
      stateTax = (0.05 / 2) * purchase_amount
elif purchase_amount <= 500:
      stateTax = (0.05 / 2) * 100 + (0.05 * 3/4) * (purchase_amount - 100)
else:
      stateTax = ((0.05 / 2) * 100 + (0.05 * 3/4)

* 400 + 0.05 * (purchase_amount - 500))

# [+] --------------------------------------------------
countyTax = 0.025 * purchase_amount
totalTax = stateTax + countyTax
totalSale = purchase_amount + totalTax
# [-] --- DELETION: MICHAEL BOYER, 18 APR 2025 ---
# Incorrect syntax for formatting
#
# print("Purchase_amount" + format(purchase_amount.2f","), \
# "state tax: $" + format(stateTax.2f" ,"), county tax : $" + \
# format(countyTax.2f" ,"), Total tax: $" + format(totalTax.2f", "), \
# "Total sales: $" + format(totalSale.2f" ,") )
# [-] --------------------------------------------

# [+] ------ ADDITION: MICHAEL BOYER, 18 APR 2025 ------
# Corrected formatting syntax, moved values to new lines,
# corrected "Purchase_amount" to "Purchase amount"
print("Purchase amount: $" + format(purchase_amount, ".2f"),
      "\nState tax: $" + format(stateTax, ".2f"), "\nCounty tax: $" +
      format(countyTax, ".2f"), "\nTotal tax: $" + format(totalTax, ".2f"),
      "\nTotal sales: $" + format(totalSale, ".2f"))
# [+] --------------------------------------------------
