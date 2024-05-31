import random

class Stock:
    def _init_(self, symbol, shares, purchase_price):
        self.symbol = symbol
        self.shares = shares
        self.purchase_price = purchase_price

    def current_price(self):
        # In a real-world application, you would fetch real-time data from financial APIs
        # For simplicity, generate random prices for demonstration
        return round(random.uniform(10, 200), 2)

    def current_value(self):
        return self.current_price() * self.shares

    def profit_loss(self):
        return (self.current_price() - self.purchase_price) * self.shares

class Portfolio:
    def _init_(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, symbol):
        for s in self.stocks:
            if s.symbol == symbol:
                self.stocks.remove(s)
                print(f"Stock {symbol} removed from portfolio.")
                return
        print(f"Stock {symbol} not found in portfolio.")

    def portfolio_value(self):
        return sum(stock.current_value() for stock in self.stocks)

    def total_profit_loss(self):
        return sum(stock.profit_loss() for stock in self.stocks)

def main():
    portfolio = Portfolio()

    while True:
        print("\n===== Stock Portfolio Tracker =====")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ")
            shares = int(input("Enter number of shares: "))
            purchase_price = float(input("Enter purchase price per share: "))
            stock = Stock(symbol, shares, purchase_price)
            portfolio.add_stock(stock)
            print(f"Stock {symbol} added to portfolio.")

        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ")
            portfolio.remove_stock(symbol)

        elif choice == "3":
            print("\n===== Portfolio Summary =====")
            for stock in portfolio.stocks:
                print(f"Stock: {stock.symbol}, Shares: {stock.shares}, Current Price: ${stock.current_price()}, Current Value: ${stock.current_value()}, Profit/Loss: ${stock.profit_loss()}")
            print(f"\nTotal Portfolio Value: ${portfolio.portfolio_value()}")
            print(f"Total Profit/Loss: ${portfolio.total_profit_loss()}")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()