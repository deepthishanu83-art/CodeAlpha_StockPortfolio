# CODEALPHA STOCK PORTFOLIO TRACKER

## Project Description
A simple, beginner-friendly Python command-line application that acts as a stock portfolio tracker. This project is developed as Task 2 for the CodeAlpha Python Internship. It allows users to add stocks to a portfolio, calculates the investment value, displays a summary, and saves the data to a CSV file.

## Features
- Displays a hardcoded list of available stocks with their current prices.
- Allows the user to add multiple stocks by symbol and quantity.
- Calculates the total investment value for each stock (price × quantity).
- Handles invalid inputs gracefully (e.g., wrong stock symbols, non-integer or negative quantities).
- Provides a clear and professional console summary of the portfolio.
- Calculates and displays the total investment value.
- Automatically saves the portfolio data to a `portfolio.csv` file for external viewing.

## Technologies/Concepts Used
- Python 3
- Data Structures: Dictionaries and Lists
- Basic Arithmetic Operations
- Input/Output Handling
- Error Handling (`try-except`)
- File Handling (`csv` module)

## How it Works
1. The program starts and displays a list of available stocks: AAPL, TSLA, GOOGL, MSFT, and AMZN.
2. The user is prompted to enter a stock symbol.
3. The user then enters the quantity of shares they wish to "buy".
4. The system validates the input. If the symbol or quantity is invalid, it asks the user to try again.
5. The user can type `done` to finish adding stocks.
6. The program then prints a formatted summary of the portfolio, including individual stock values and the total portfolio value.
7. Finally, it exports the summary to `portfolio.csv`.

## How to Run It
1. Make sure Python 3 is installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command:
   ```bash
   python stock_portfolio.py
   ```

## Sample Input/Output
```text
==================================================
      CODEALPHA STOCK PORTFOLIO TRACKER      
==================================================

Available Stocks to add:
- AAPL: $180.0
- TSLA: $250.0
- GOOGL: $150.0
- MSFT: $420.0
- AMZN: $180.0

Enter 'done' to finish adding stocks.
Enter a stock symbol: AAPL
Enter quantity for AAPL: 5
Successfully added 5 shares of AAPL.

Available Stocks to add:
...
Enter a stock symbol: done

==================================================
              PORTFOLIO SUMMARY              
==================================================
Stock      | Quantity   | Price      | Value     
--------------------------------------------------
AAPL       | 5          | $180.00    | $900.00   
--------------------------------------------------
Total Investment Value: $900.00

Portfolio successfully saved to portfolio.csv
```

## CSV File Explanation
The generated `portfolio.csv` file contains the final state of your portfolio with the following columns:
- **Stock Symbol**: The ticker symbol of the stock.
- **Quantity**: The number of shares owned.
- **Price**: The price per share.
- **Investment Value**: The total value (Quantity × Price).

## CodeAlpha Task 2
This project satisfies all requirements for Task 2 of the CodeAlpha Python Internship.
