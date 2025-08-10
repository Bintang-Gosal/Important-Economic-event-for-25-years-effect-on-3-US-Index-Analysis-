import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

index_options = {
    "S&P 500": "SPY",
    "NASDAQ 100": "^IXIC",
    "Dow Jones Industrial Average": "^DJI"
}

selected_index_name = st.selectbox(
    "Choose what index you want to see:",
    list(index_options.keys())
)
selected_ticker = index_options[selected_index_name]

@st.cache_data
def get_data(ticker, start_date, end_date):
    return yf.download(ticker, start=start_date, end=end_date)

start_date = "1999-11-01"
end_date = "2025-08-08"

df_index = get_data(selected_ticker, start_date, end_date)
df_vix = get_data('^VIX', start_date, end_date)

# ---------------------------------------------------------------
# Data Vizualation

fig, ax1 = plt.subplots(facecolor="black")
ax1.set_title("\nINDEX PRICE AND VOTALITY (25 YEARS PERIOD)\n", color='white')

ax1.plot(df_index.index , df_index["Close"], color="white")
ax1.grid(color='white', linestyle='--', linewidth=0.5, alpha=0.5)
ax1.set_xlabel("Date Period", color="white")
ax1.set_ylabel("Close Priced (USD)", color="white")

ax1.set_facecolor('black')

ax2 = ax1.twinx()

ax2.set_ylabel("Votality Index", color="white")
ax2.set_facecolor('black')
ax2.spines['bottom'].set_color('white')
ax2.spines['left'].set_color('white')
ax2.spines['right'].set_color('white')

ax2.plot(df_index.index, df_vix, color="green")

ax1.tick_params(axis="x", colors="white")
ax1.tick_params(axis="y", colors="white")
ax2.tick_params(axis="y", colors="white")

# ----------------------------------------------------------------------------
# Dashboard

plt.tight_layout()

st.header("Data Analysis  (Bintang Fridel Putra Gosal)")

st.title("Relation Beetween Important Economic Event For The Past 25 Years to Top 3 US Index and the Votality Index")

st.pyplot(fig)

st.markdown("""
# Overview of US Economic Crises and Their Impact

Analyzing the three major economic crises of the last 25 years—**the Dot-Com Bubble (2000-2002), the 2008 Financial Crisis, and the COVID-19 Pandemic (2020)**—reveals a consistent pattern in the US stock market. While the triggers and scale of each crisis differed, their impact on major indices like the S&P 500, NASDAQ, and Dow Jones Industrial Average showed striking similarities.

### Key Observed Patterns:

1. **Synchronized Decline in Index Prices:** During each crisis, these three indices experienced a sharp and synchronized price drop. This happened because systemic economic shocks affect the entire market, not just one sector. The most drastic declines occurred during the 2008 Financial Crisis and the COVID-19 Pandemic, where the market lost a significant portion of its value in a short period.
2. **Spike in Volatility (VIX):** Every time index prices fell, the VIX spiked dramatically. This reinforces the VIX's role as the market's "fear index." A VIX spike indicates high uncertainty and fear among investors, which leads to extreme daily price fluctuations. The highest peak of the VIX occurred in October 2008, reflecting the extraordinary panic resulting from the banking crisis.

This pattern proves a strong **inverse relationship** between market index prices and volatility. When investor confidence is low, the VIX rises, and prices fall. Conversely, when the market is calm and confident, the VIX remains low.

***

### 1. Dot-Com Bubble 🫧

* **Year:** 2000 - 2002
* **Cause:** This crisis was triggered by euphoria and excessive speculation on internet and technology company stocks. Investors bought shares of these new companies at very high valuations, even though many had yet to turn a profit. Low interest rate policies from the central bank also encouraged risky investments.
* **Impact:**
    * **Market Crash:** After peaking in March 2000, the NASDAQ Composite—which was heavily focused on technology—lost nearly 80% of its value. The S&P 500 and Dow Jones also experienced significant declines.
    * **Company Failures:** Many dot-com companies went bankrupt, resulting in the loss of millions of jobs and investor capital.

***

### 2. Global Financial Crisis 2008 📉

* **Year:** 2007 - 2009
* **Cause:** The primary trigger was the collapse of the US housing market. Banks issued subprime mortgages (high-risk loans) to borrowers who could not afford to repay them. These loans were then packaged into complex financial instruments sold worldwide. When the housing bubble burst, many borrowers defaulted, causing these instruments to lose their value.
* **Impact:**
    * **Global Recession:** The crisis triggered the Great Recession, considered the worst recession since the Great Depression. The global economy shrank, unemployment rates surged, and consumer confidence plummeted.
    * **Bank Failures:** Several major financial institutions went bankrupt (like Lehman Brothers) or were bailed out by the government, exposing the fragility of the global financial system.

***

### 3. COVID-19 Pandemic 😷

* **Year:** 2020 - 2021
* **Cause:** This crisis was triggered by the global spread of the COVID-19 virus. Governments worldwide imposed lockdowns and restrictions, which abruptly halted much of the economic activity.
* **Impact:**
    * **Rapid Market Collapse:** The stock market experienced one of its fastest crashes in history, with the S&P 500 and other indices losing about 30% of their value in just a few weeks.
    * **Government Intervention:** Central banks and governments responded with massive fiscal and monetary stimulus (such as interest rate cuts and aid packages), which helped the market recover quickly, although the real economic recovery took longer.
    * **Economic Shift:** The pandemic accelerated digital trends, such as e-commerce and remote work, which had a long-term impact on the global economy.

***

### Glossary of Technical Terms

* **S&P 500:** An index that tracks the performance of the 500 largest US companies. It is often considered the best benchmark for the health of the US economy.
* **NASDAQ Composite:** An index containing over 3,000 stocks, mostly from technology and biotechnology companies. It is highly sensitive to trends in the tech sector.
* **Dow Jones Industrial Average:** An index of 30 large, well-established (*blue-chip*) US companies. Although its scope is small, it is one of the most well-known market indicators.
* **VIX (Volatility Index):** Known as the "fear index," the VIX measures the market's expectation of S&P 500 volatility over the next 30 days. A high VIX indicates uncertainty and fear.
* **Bull Market:** A period when the stock market is in an upward trend, driven by investor optimism.
* **Bear Market:** A period when the stock market is in a downward trend, driven by pessimism and fear.
* **Market Crash:** A sudden, sharp decline in stock prices over a short period, often triggered by a major event.
* **Recession:** A significant decline in economic activity lasting for several months, typically marked by a drop in GDP.
""")