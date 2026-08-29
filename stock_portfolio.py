import csv

def main():
    print("=" * 50)
    print("      CODEALPHA STOCK PORTFOLIO TRACKER      ")
    print("=" * 50)

    # Hardcoded dictionary of stock symbols and prices
    stocks_db = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "GOOGL": 150.0,
        "MSFT": 420.0,
        "AMZN": 180.0
    }

    portfolio = []

    while True:
        print("\nAvailable Stocks to add:")
        for symbol, price in stocks_db.items():
            print(f"- {symbol}: ${price}")
        
        print("\nEnter 'done' to finish adding stocks.")
        symbol_input = input("Enter a stock symbol: ").strip().upper()
        
        if symbol_input == 'DONE':
            break
            
        if symbol_input not in stocks_db:
            print("Invalid stock symbol. Please try again.")
            continue
            
        quantity_input = input(f"Enter quantity for {symbol_input}: ").strip()
        
        try:
            quantity = int(quantity_input)
            if quantity <= 0:
                print("Quantity must be a positive integer. Please try again.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a valid number.")
            continue
            
        price = stocks_db[symbol_input]
        investment_value = price * quantity
        
        # Check if already in portfolio and update, or add new
        found = False
        for item in portfolio:
            if item['symbol'] == symbol_input:
                item['quantity'] += quantity
                item['investment_value'] += investment_value
                found = True
                break
                
        if not found:
            portfolio.append({
                'symbol': symbol_input,
                'quantity': quantity,
                'price': price,
                'investment_value': investment_value
            })
            
        print(f"Successfully added {quantity} shares of {symbol_input}.")

    print("\n" + "=" * 50)
    print("              PORTFOLIO SUMMARY              ")
    print("=" * 50)
    
    if not portfolio:
        print("Your portfolio is empty.")
    else:
        total_investment = 0
        print(f"{'Stock':<10} | {'Quantity':<10} | {'Price':<10} | {'Value':<10}")
        print("-" * 50)
        
        for item in portfolio:
            print(f"{item['symbol']:<10} | {item['quantity']:<10} | ${item['price']:<9.2f} | ${item['investment_value']:<9.2f}")
            total_investment += item['investment_value']
            
        print("-" * 50)
        print(f"Total Investment Value: ${total_investment:.2f}")
        
        # Save to CSV
        csv_filename = "portfolio.csv"
        try:
            with open(csv_filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Stock Symbol", "Quantity", "Price", "Investment Value"])
                for item in portfolio:
                    writer.writerow([item['symbol'], item['quantity'], item['price'], item['investment_value']])
            print(f"\nPortfolio successfully saved to {csv_filename}")
        except Exception as e:
            print(f"\nError saving to CSV: {e}")

if __name__ == "__main__":
    main()
