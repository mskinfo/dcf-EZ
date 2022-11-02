# This package is not financial advice
# The creator(s) will not be held liable for any financial loss or other loss as a result of the use of this package.
# The package allows users to enter a ticker and get historical financial data
print("***DISCLAIMER***")
print("PAST RETURNS ARE NOT INDICATIVE OF FUTURE RESULTS.")
print("THE DISCOUNTED CASHFLOW MODEL IS ONE OF MANY TOOLS THAT SHOULD BE USED IN VALUATION")
print("THIS SIMPLE DCF IS FOR EDUCATIONAL PURPOSES ONLY, AND IT IS NOT FINANCIAL ADVICE")
print("***DISCLAIMER***")
print()

from fredapi import Fred
fred = Fred(api_key='d355e18cbdd60307c8100671ba120dd5')
import yfinance as yf
import pandas as pd

print("enter a stock ticker.")
stock_ticker_input = input()

stock_ticker = yf.Ticker(stock_ticker_input)
dict_stock_info = stock_ticker.info

# parsing the income statement
df_financials = stock_ticker.financials

df_top = []

for col in df_financials.columns:
    df_top.append(col)

date_1_i = df_top[0]
date_2_i = df_top[1]
date_3_i = df_top[2]
date_4_i = df_top[3]

operating_income_t = df_financials.loc["Operating Income", date_1_i]
operating_income_t1 = df_financials.loc["Operating Income", date_2_i]
operating_income_t2 = df_financials.loc["Operating Income", date_3_i]
operating_income_t3 = df_financials.loc["Operating Income", date_4_i]

tax_expense_t = df_financials.loc["Income Tax Expense", date_1_i]
tax_expense_t1 = df_financials.loc["Income Tax Expense", date_2_i]
tax_expense_t2 = df_financials.loc["Income Tax Expense", date_3_i]
tax_expense_t3 = df_financials.loc["Income Tax Expense", date_4_i]

income_after_taxes_t = operating_income_t-tax_expense_t
income_after_taxes_t1 = operating_income_t1-tax_expense_t1
income_after_taxes_t2 = operating_income_t2-tax_expense_t2
income_after_taxes_t3 = operating_income_t3-tax_expense_t3

# parsing the balance sheet
df_balance_sheet = stock_ticker.balance_sheet

df_top2 = []

for col in df_balance_sheet.columns:
    df_top2.append(col)

date_1_b = df_top2[0]
date_2_b = df_top2[1]
date_3_b = df_top2[2]
date_4_b = df_top2[3]

current_assets_t = df_balance_sheet.loc["Total Current Assets", date_1_b]
current_assets_t1 = df_balance_sheet.loc["Total Current Assets", date_2_b]
current_assets_t2 = df_balance_sheet.loc["Total Current Assets", date_3_b]
current_assets_t3 = df_balance_sheet.loc["Total Current Assets", date_4_b]

current_liabilities_t = df_balance_sheet.loc["Total Current Liabilities", date_1_b]
current_liabilities_t1 = df_balance_sheet.loc["Total Current Liabilities", date_2_b]
current_liabilities_t2 = df_balance_sheet.loc["Total Current Liabilities", date_3_b]
current_liabilities_t3 = df_balance_sheet.loc["Total Current Liabilities", date_4_b]

working_capital_t = current_assets_t - current_liabilities_t
working_capital_t1 = current_assets_t1 - current_liabilities_t1
working_capital_t2 = current_assets_t2 - current_liabilities_t2
working_capital_t3 = current_assets_t3 - current_liabilities_t3

change_in_working_capital_t = working_capital_t - working_capital_t1
change_in_working_capital_t1 = working_capital_t1 - working_capital_t2
change_in_working_capital_t2 = working_capital_t2 - working_capital_t3

# parsing the cash flow statement
df_cash_flow = stock_ticker.cashflow
df_top3 = []

for col in df_cash_flow.columns:
    df_top3.append(col)

date_1_c = df_top3[0]
date_2_c = df_top3[1]
date_3_c = df_top3[2]
date_4_c = df_top3[3]

capex_t = df_cash_flow.loc["Capital Expenditures", date_1_c]
capex_t1 = df_cash_flow.loc["Capital Expenditures", date_2_c]
capex_t2 = df_cash_flow.loc["Capital Expenditures", date_3_c]
capex_t3 = df_cash_flow.loc["Capital Expenditures", date_4_c]

depreciation_t = df_cash_flow.loc["Depreciation", date_1_c]
depreciation_t1 = df_cash_flow.loc["Depreciation", date_2_c]
depreciation_t2 = df_cash_flow.loc["Depreciation", date_3_c]
depreciation_t3 = df_cash_flow.loc["Depreciation", date_4_c]

# calculating the free cash flows and other metrics required to predict future cash flows
free_cash_flow_t = income_after_taxes_t-(capex_t-depreciation_t)-change_in_working_capital_t
free_cash_flow_t1 = income_after_taxes_t1-(capex_t1-depreciation_t1)-change_in_working_capital_t1
free_cash_flow_t2 = income_after_taxes_t2-(capex_t2-depreciation_t2)-change_in_working_capital_t2

print(df_balance_sheet)
print(df_financials)
print(df_cash_flow)

return_on_invested_capital_t = (df_financials.loc["Net Income", date_1_i] + df_cash_flow.loc["Dividends Paid", date_1_c])/(working_capital_t)
return_on_invested_capital_t1 = (df_financials.loc["Net Income", date_2_i] + df_cash_flow.loc["Dividends Paid", date_2_c])/(working_capital_t1)
return_on_invested_capital_t2 = (df_financials.loc["Net Income", date_3_i] + df_cash_flow.loc["Dividends Paid", date_3_c])/(working_capital_t2)
return_on_invested_capital_t3 = (df_financials.loc["Net Income", date_4_i] + df_cash_flow.loc["Dividends Paid", date_4_c])/(working_capital_t3)

reinvestment_rate_t = (-capex_t - depreciation_t)/(df_financials.loc["Ebit", date_1_i]*(df_financials.loc["Ebit", date_1_i]/df_financials.loc["Income Tax Expense", date_1_i]))
reinvestment_rate_t1 = (-capex_t1 - depreciation_t1)/(df_financials.loc["Ebit", date_2_i]*(df_financials.loc["Ebit", date_2_i]/df_financials.loc["Income Tax Expense", date_2_i]))
reinvestment_rate_t2 = (-capex_t2 - depreciation_t2)/(df_financials.loc["Ebit", date_3_i]*(df_financials.loc["Ebit", date_3_i]/df_financials.loc["Income Tax Expense", date_2_i]))
reinvestment_rate_t3 = (-capex_t3 - depreciation_t3)/(df_financials.loc["Ebit", date_4_i]*(df_financials.loc["Ebit", date_4_i]/df_financials.loc["Income Tax Expense", date_4_i]))

# cost of capital and equity
# economic data for growth projections
#   key performance indicators by industry
# terminal growth rate
# summation of total value
# fair market cap
# fair share price
