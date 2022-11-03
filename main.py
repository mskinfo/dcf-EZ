# This package is not financial advice
# The creator(s) will not be held liable for any financial loss or other loss as a result of the use of this package.
# The package allows users to enter a ticker and get historical financial data
print("***DISCLAIMER***")
print("PAST RETURNS ARE NOT INDICATIVE OF FUTURE RESULTS.")
print("THE DISCOUNTED CASHFLOW MODEL IS ONE OF MANY TOOLS THAT SHOULD BE USED IN VALUATION")
print("THIS SIMPLE DCF IS FOR EDUCATIONAL PURPOSES ONLY, AND IT IS NOT FINANCIAL ADVICE")
print("***DISCLAIMER***")
print()
import pandas as pd

value_info_list = [['Stock Ticker:', 'Net Operating Profit After Tax, Period 1',
                      'Net Operating Profit After Tax Growth Rate',
                      'Reinvestment Rate',
                      'Average Return on invested Capital:', 'Risk Free Rate',
                      'Market Return', 'Beta',
                      'Cost of Equity (using CAPM)',
                      'Cost of Debt',  'Corporate Tax Rate',
                      'Weighted Average Cost of Capital / Discount Rate:', 'Total Future Value',
                      'Current Price Per Share',
                      'Low-End Price Per Share', 'High-End Price Per Share:', 'Projected Price Per Share']]

company_list = []
ticker_input = None
while ticker_input != '':
    print("Enter a stock ticker or press enter to evaluate your portfolio, or stock if you are entering just one: ")
    ticker_input = input()
    company_list.append(ticker_input)

company_list.remove('')

print("Enter your expected average risk free rate for the duration of the time horizon (enter 5 for 5%, 2.5 for 2.5%):")
risk_free_input = float(input())
print("Enter your expected average market return for the duration of the time horizon (enter 11 for 11%, 7.5 for 7.5%):")
average_market_return_input = float(input())

rfr = risk_free_input*.01
market_return = average_market_return_input*.01

for item in company_list:
    import yfinance as yf

    stock_ticker_input = item
    stock_ticker = yf.Ticker(stock_ticker_input)
    dict_stock_info = stock_ticker.info

    # parsing the income statement
    df_financials = stock_ticker.financials
    df_balance_sheet = stock_ticker.balance_sheet
    df_cash_flow = stock_ticker.cashflow

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

    income_after_taxes_t = operating_income_t - tax_expense_t
    income_after_taxes_t1 = operating_income_t1 - tax_expense_t1
    income_after_taxes_t2 = operating_income_t2 - tax_expense_t2
    income_after_taxes_t3 = operating_income_t3 - tax_expense_t3

    # parsing the balance sheet
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

    # working capital
    working_capital_t = current_assets_t - current_liabilities_t
    working_capital_t1 = current_assets_t1 - current_liabilities_t1
    working_capital_t2 = current_assets_t2 - current_liabilities_t2
    working_capital_t3 = current_assets_t3 - current_liabilities_t3

    change_in_working_capital_t = working_capital_t - working_capital_t1
    change_in_working_capital_t1 = working_capital_t1 - working_capital_t2
    change_in_working_capital_t2 = working_capital_t2 - working_capital_t3

    net_working_capital_t = working_capital_t
    net_working_capital_t1 = working_capital_t1
    net_working_capital_t2 = working_capital_t2
    net_working_capital_t3 = working_capital_t3

    # parsing the cash flow statement
    df_top3 = []

    for col in df_cash_flow.columns:
        df_top3.append(col)

    date_1_c = df_top3[0]
    date_2_c = df_top3[1]
    date_3_c = df_top3[2]
    date_4_c = df_top3[3]

    # needs substitutes
    capex_t = df_cash_flow.loc["Capital Expenditures", date_1_c]
    capex_t1 = df_cash_flow.loc["Capital Expenditures", date_2_c]
    capex_t2 = df_cash_flow.loc["Capital Expenditures", date_3_c]
    capex_t3 = df_cash_flow.loc["Capital Expenditures", date_4_c]

    depreciation_t = df_cash_flow.loc["Depreciation", date_1_c]
    depreciation_t1 = df_cash_flow.loc["Depreciation", date_2_c]
    depreciation_t2 = df_cash_flow.loc["Depreciation", date_3_c]
    depreciation_t3 = df_cash_flow.loc["Depreciation", date_4_c]

    # net operating profit after tax
    N_O_P_A_T_t = df_financials.loc["Ebit", date_1_i] - df_financials.loc["Income Tax Expense", date_1_i]
    N_O_P_A_T_t1 = df_financials.loc["Ebit", date_2_i] - df_financials.loc["Income Tax Expense", date_2_i]
    N_O_P_A_T_t2 = df_financials.loc["Ebit", date_3_i] - df_financials.loc["Income Tax Expense", date_3_i]
    N_O_P_A_T_t3 = df_financials.loc["Ebit", date_4_i] - df_financials.loc["Income Tax Expense", date_4_i]

    # finding the return on invested capital
    invested_capital_t = df_balance_sheet.loc["Total Liab", date_1_b] + \
                         df_balance_sheet.loc["Total Stockholder Equity", date_1_b]
    invested_capital_t1 = df_balance_sheet.loc["Total Liab", date_2_b] + \
                          df_balance_sheet.loc["Total Stockholder Equity", date_2_b]
    invested_capital_t2 = df_balance_sheet.loc["Total Liab", date_3_b] + \
                          df_balance_sheet.loc["Total Stockholder Equity", date_3_b]
    invested_capital_t3 = df_balance_sheet.loc["Total Liab", date_4_b] + \
                          df_balance_sheet.loc["Total Stockholder Equity", date_4_b]

    return_on_invested_capital_t = N_O_P_A_T_t / invested_capital_t
    return_on_invested_capital_t1 = N_O_P_A_T_t1 / invested_capital_t1
    return_on_invested_capital_t2 = N_O_P_A_T_t2 / invested_capital_t2
    return_on_invested_capital_t3 = N_O_P_A_T_t3 / invested_capital_t3

    # reinvestment_rate_t =
    net_capex_t = -capex_t - depreciation_t
    net_capex_t1 = -capex_t1 - depreciation_t1
    net_capex_t2 = -capex_t2 - depreciation_t2
    net_capex_t3 = -capex_t3 - depreciation_t3

    reinvestment_rate_t = net_capex_t / N_O_P_A_T_t
    reinvestment_rate_t1 = net_capex_t1 / N_O_P_A_T_t1
    reinvestment_rate_t2 = net_capex_t2 / N_O_P_A_T_t2

    average_reinvestment_rate = (reinvestment_rate_t + reinvestment_rate_t1 + reinvestment_rate_t2) / 3
    average_ROIC = (return_on_invested_capital_t + return_on_invested_capital_t1 + return_on_invested_capital_t2 +
                    return_on_invested_capital_t3) / 4

    rate_of_increased_returns = average_ROIC*average_reinvestment_rate

    # weighted_average_cost_of_capital

    beta = dict_stock_info['beta']

    equity = df_balance_sheet.loc["Total Stockholder Equity", date_1_b]

    debt = df_balance_sheet.loc["Long Term Debt", date_1_b]

    cost_of_equity = (rfr + beta * (market_return - rfr))

    cost_of_debt = (-df_financials.loc["Interest Expense", date_1_i]) / debt

    enterprise_value = (debt + equity)

    corporate_tax_rate = df_financials.loc["Income Tax Expense", date_1_i] / df_financials.loc["Ebit", date_1_i]

    WACC = (equity / enterprise_value) * cost_of_equity + (debt / enterprise_value) * cost_of_debt * (
            1 - corporate_tax_rate)

    # 7 year time horizon
    N_O_P_A_T_period_1 = (1 + (average_reinvestment_rate * average_ROIC)) * N_O_P_A_T_t
    N_O_P_A_T_period_2 = (1 + (average_reinvestment_rate * average_ROIC)) * N_O_P_A_T_period_1
    N_O_P_A_T_period_3 = (1 + (average_reinvestment_rate * average_ROIC)) * N_O_P_A_T_period_2
    N_O_P_A_T_period_4 = (1 + (average_reinvestment_rate * average_ROIC)) * N_O_P_A_T_period_3
    N_O_P_A_T_period_5 = (1 + (average_reinvestment_rate * average_ROIC)) * N_O_P_A_T_period_4
    N_O_P_A_T_period_6 = (1 + (average_reinvestment_rate * average_ROIC)) * N_O_P_A_T_period_5
    N_O_P_A_T_period_7 = (1 + (average_reinvestment_rate * average_ROIC)) * N_O_P_A_T_period_6
    N_O_P_A_T_period_8 = (1 + (average_reinvestment_rate * average_ROIC)) * N_O_P_A_T_period_7

    free_cash_flow_period_1 = N_O_P_A_T_period_1 * (1 - average_reinvestment_rate) / (1 + WACC)
    free_cash_flow_period_2 = N_O_P_A_T_period_2 * (1 - average_reinvestment_rate) / ((1 + WACC) ** 2)
    free_cash_flow_period_3 = N_O_P_A_T_period_3 * (1 - average_reinvestment_rate) / ((1 + WACC) ** 3)
    free_cash_flow_period_4 = N_O_P_A_T_period_4 * (1 - average_reinvestment_rate) / ((1 + WACC) ** 4)
    free_cash_flow_period_5 = N_O_P_A_T_period_5 * (1 - average_reinvestment_rate) / ((1 + WACC) ** 5)
    free_cash_flow_period_6 = N_O_P_A_T_period_6 * (1 - average_reinvestment_rate) / ((1 + WACC) ** 6)
    free_cash_flow_period_7 = N_O_P_A_T_period_7 * (1 - average_reinvestment_rate) / ((1 + WACC) ** 7)
    terminal_value = N_O_P_A_T_period_8 / WACC

    FV = (terminal_value + free_cash_flow_period_7 + free_cash_flow_period_6 + free_cash_flow_period_5 +
          free_cash_flow_period_4 + free_cash_flow_period_3 + free_cash_flow_period_2 + free_cash_flow_period_1)

    market_capitalization = dict_stock_info['marketCap']
    shs = dict_stock_info['sharesOutstanding']

    current_price = dict_stock_info['currentPrice']

    DCF_EZ_price_per_share = FV / shs
    low_price_est = dict_stock_info['targetLowPrice']
    high_price_est = dict_stock_info['targetHighPrice']
    median_price_est = dict_stock_info['targetMedianPrice']
    mean_price_est = dict_stock_info['targetMeanPrice']

    upside_downside = DCF_EZ_price_per_share / current_price
    up_down_percent = (upside_downside - 1) * 100
    data_valuation = [stock_ticker_input, N_O_P_A_T_period_1, rate_of_increased_returns, average_reinvestment_rate,
                      average_ROIC, rfr, market_return, beta, cost_of_equity, cost_of_debt, corporate_tax_rate, WACC,
                      FV, current_price, low_price_est, high_price_est, DCF_EZ_price_per_share]
    value_info_list.append(data_valuation)
valuation_dataframe = pd.DataFrame(value_info_list)

print(valuation_dataframe)

print("To export to a .csv file enter 'c'.")
print("To export to an Excel file enter 'e'.")
print("To terminate the application, enter 't'.")

decision_input = input()
if decision_input == 't':
    exit()
if decision_input == 'e':
    valuation_dataframe.to_excel("valuations.xlsx")
if decision_input == 'c':
    valuation_dataframe.to_csv("valuations.csv")
