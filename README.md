# Analysis of the Impact of Economic Crises on US Stock Markets (1999-2025)

## Project Description
This project is an interactive dashboard built with Streamlit to visualize and analyze the relationship between three major US stock market indices (S&P 500, NASDAQ, Dow Jones Industrial Average) and the VIX (Volatility Index). The dashboard's purpose is to illustrate market patterns during three significant economic crises: **the Dot-Com Bubble, the 2008 Financial Crisis, and the COVID-19 Pandemic**.

Users can select which index to visualize, view historical data, and read in-depth analysis of each crisis's impact on stock prices and volatility.

## Key Features
-   **Dynamic Index Selection**: Choose from one of three major US market indices (S&P 500, NASDAQ, Dow Jones) to view its performance.
-   **Price & Volatility Visualization**: A dual-axis chart comparing the selected index's price with the Volatility Index (VIX).
-   **Analysis of Key Events**: Detailed explanations of the causes, impacts, and characteristics of the three major economic crises.
-   **Explanation of Market Patterns**: A description of the consistent inverse relationship between market prices and volatility (VIX).
-   **Interactive Data Display**: Historical data tables that can be sorted and resized.

## How to Install and Run the Project
1.  **Clone this repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```
    *(Replace `your-username` and `your-repository-name` with your repository details.)*

2.  **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate      # For Windows
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: Ensure you create a `requirements.txt` file containing the necessary libraries such as `streamlit`, `yfinance`, `pandas`, and `matplotlib`.*

4.  **Run the Streamlit application:**
    ```bash
    streamlit run dashboard.py
    ```
    The application will automatically open in your web browser.

## Project Structure
