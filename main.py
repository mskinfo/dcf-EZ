# This package is not financial advice
# The creator(s) will not be held liable for any financial loss or other loss as a result of the use of this package.
# The package allows users to enter a ticker and get historical financial data
print("***DISCLAIMER***")
print("PAST RETURNS ARE NOT INDICATIVE OF FUTURE RESULTS.")
print("THE DISCOUNTED CASHFLOW MODEL IS ONE OF MANY TOOLS THAT SHOULD BE USED IN VALUATION")
print("THIS SIMPLE DCF IS FOR EDUCATIONAL PURPOSES ONLY, AND IT IS NOT FINANCIAL ADVICE")
print("***DISCLAIMER***")
print()

interest_rate = float(0.04286)

print("Enter the average projected growth rate of the company's free cash flow/dividend.  Enter 5 for 5% YoY growth.")
CAGR_cashflow = float(input())

print("Enter your company's total cashflow.  do not use commas:")
cashflow = float(input())

print("Enter your time horizon for receiving the cashflows:")
time_horizon = int(input())

x = range(1, (time_horizon+1))

cashflows = []
for i in x:
    y = (cashflow*(1+.01*CAGR_cashflow)**i)/((1+interest_rate)**i)
    cashflows.append(y)

ending_value = sum(cashflows)
print("enter the market capitalization of the company")
market_cap = float(input())

market_value_div_user_value = (ending_value/market_cap)

print("The ratio of your valuation to the market's valuation is", market_value_div_user_value)

if 1.05 > market_value_div_user_value > 0.95:
    print("Your valuation implies the company is worth about the same as the current market value.")
else:
    if market_value_div_user_value > 1.05:
        print("Your valuation implies the company is undervalued")
    if market_value_div_user_value < 0.95:
        print("Your valuation implies the company is overvalued")
