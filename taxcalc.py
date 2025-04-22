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
# - State tax rate is 5% with graduated rates: half rate for first $100, 3/4
#   rate for $100-$500, full rate after $500
# - County tax rate is 2.5% on full purchase amount
# - Tax law effective date is July 1, 2025
# - Taxes adjusted for inflation each year (assumed at a rate of 3% per year)
#
# Inputs:
# - Purchase amount (user-entered dollar value)
#
# Outputs:
# - Purchase amount
# - State tax amount
# - County tax amount
# - Total tax amount
# - Total sale amount (purchase + taxes)
#
# Processes:
# - Validate user input for purchase amount
# - Calculate state tax based on graduated rates
# - Calculate county tax
# - Apply inflation adjustment if current date is after effective year
# - Calculate total tax and sale amount
# - Display formatted results
#
# Begin your program after this line

# Michael Boyer (4/22/2025)
# For dates to adjust taxes for inflation; assuming a rate of 3% per year
import datetime
# ------------

# Michael Boyer (04/20/2025)
# Initialize variables for validity check and user input
purchase_amount = 0.0
valid = False

# (4/22) New tax law effective datetime, then the current date
effective_date = datetime.date(2025, 7, 1)

# (4/22) This would otherwise be datetime.date.today(), but
# for demonstration purposes of the assignment, we will use any
# arbitrary date after the effective date
current_date = datetime.date(2025, 8, 1)
years_elapsed = current_date.year - effective_date.year
# -----------

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
# ------------

# Michael Boyer (04/18/2025)
# Replaced old code with new logic on graduated tax rates.

# (4/18) If the purchase amount is less than or equal to 100, then the tax
# rate is half
if purchase_amount <= 100:
    stateTax = (0.05 / 2) * purchase_amount

# (4/18) If the purchase amount is less than or equal to 500, then the tax
# rate is half for the initial $100 from the total purchase amount, and 3/4
# the rate for the remaining amount
elif purchase_amount <= 500:
    stateTax = (0.05 / 2) * 100 + (0.05 * 3/4) * (purchase_amount - 100)

# (4/18) And if the purchase amount is greater than 500, then the tax rate is
# half for the initial $100 from the total purchase amount, 3/4 the rate for
# the next $400, and full rate for the remaining amount
else:
    stateTax = ((0.05 / 2) * 100 + (0.05 * 3/4) * 400 + 0.05 * (purchase_amount - 500))
# ------------

# Michael Boyer (4/22/2025)
# Implement logic to determine if we need to inflate taxes

# (4/22) We're initializing it at 1.00 because if the if statement
# doesn't go through, we don't need to manipulate the multiplier
inflation_multiplier = 1.00

# (4/22) If we are in the future (relative to effective date)
# We will take years_elapsed (current - effective year) and
# calculate the inflation multiplier
if current_date.year > effective_date.year:
    inflation_multiplier = 1.03 ** years_elapsed

# (4/22) Now we bump state and county taxes for inflation (if applicable)
stateTax = stateTax * inflation_multiplier
countyTax = (0.025 * purchase_amount) * inflation_multiplier
totalTax = stateTax + countyTax
totalSale = purchase_amount + totalTax
# ------------

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
