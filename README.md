# dcf-EZ

## How to Use

This application is a console app that allows users to input the ticker of a stock they would like to evaluate, and using the yfinance package @ https://github.com/ranaroussi/yfinance, a vertical dataframe is printed with a single estimate of the company's intrinsic value.

## What is a Discounted Cash Flow Valuation

A discounted cash flow valuation, or "DCF" valuation, is the most common technique financial analysts use to calculate the intrinsic ability of a company to continuously add value to itself.  Essentially, a DCF valuation is an equation where the summation of discounted future cash flows and a terminal value are added together to find the future value, and divided by the number of shares outstanding to find the present intrinsic value of a share.  There are many issues with the discounted cash flow valuation, and with intrinsic valuation in general, but it is an important part of an investor's toolbox for the evaluation of a potential cash-generating investment.

### Weaknesses of the DCF Valuation

It is best to examine the limitations of a tool, and to keep these in mind constantly.  Just because a DCF valuation yields a future value 9,999.56% higher than the current market capitalization of an asset does not mean that the asset is a good investment.  A result like this may mean that the DCF equation is using incorrect numbers, is not accounting for specific risks facing the company, or ignoring environmental, social, or governmental factors.  

#### Markets Determine Value

In an monetary economy, the price of a good is the intersection between the marginal buyer's monetary willingness to pay for a good, and the marginal seller's monetary willingness to reliniquish their good.  For normal goods, this usually implies that the price will be equivalent to the highest price a buyer is willing to pay, and the lowest price a seller will pay.  This might mean that a good, regardless of what it is "intrinsically" worth, will never be priced at the intrinsic value,because the average of the market's intrinsic values are different.

#### Systemic Risk and Unknown Risks

The discounted cashflow valuation does not account for risks facing global financial markets.  Assets are not priced to account for systemic collapse, radical changes in the global socio-economic system, or future litigation for externalities the asset might be causing.  While it is impossible to account for things we *truly* do not know, the job of many people in the financial sector is to downplay risks and convince people that supporting businesses ***they have a financial stake in*** is the right thing to do, regardless of the realities of the risks. A discounted cash flow valuation is a tool that can be used to see through most of the nonsense put forth by people in the financial world, but it is not enough to see through all of it.

#### Voting Power

The strategic actions of publicly traded companies are determined by the collective votes of a company's shareholders.  A shareholder's best interests may be different from yours. Shareholder voting decisions may degrade the value of a company regardless of the competence of the company's leadership, the strategic utility of assets.  There is nothing stopping a company from being hijacked by activist investors and liquidated, or driven into ruin by misinformed shareholder decisions.

### Strength of the DCF Valuation

The greatest strength of the DCF valuation is that it is desinged to be completely customizable.  An analyst can use this framework to account for almost any risk or upside, simulate multiple scenarios, and weight the probability of the scenario.  
