import yfinance as yf

# Portfolio list to store stock data
portfolio = []

# Add Stock
def add_stock(symbol, shares, buy_price):
    for stock in portfolio:
        if stock['symbol'] == symbol:
            stock['shares'] += shares
            print(f"{symbol}: Now Holding {stock['shares']} Shares.")
            return
    portfolio.append({"symbol": symbol, "shares": shares, "buy_price": round(buy_price, 2)})
    print(f"✅ Added {symbol}: {shares} shares at ${buy_price:.2f} each.")

# Get Current Price
def get_current_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        current_price = stock.history(period="1d")['Close'].iloc[-1]
        return round(current_price, 2)
    except Exception as e:
        print(f"❌ Failed to fetch the current price for {symbol}: {e}")
        return None

# Calculate Stock Value
def calculate_stock_value(shares, current_price):
    return round(shares * current_price, 2)

# Calculate Profit or Loss
def calculate_profit_loss(shares, current_price, buy_price):
    return round(shares * (current_price - buy_price), 2)

# Display Portfolio
def display_portfolio():
    if not portfolio:
        print("\n📭 Your portfolio is empty!")
        return

    total_portfolio_value = 0

    print("\n📊 Portfolio Overview:")
    print("-" * 40)

    for stock in portfolio:
        symbol, shares, buy_price = stock['symbol'], stock['shares'], stock['buy_price']
        current_price = get_current_price(symbol)

        if current_price is not None:
            stock_value = calculate_stock_value(shares, current_price)
            profit_or_loss = calculate_profit_loss(shares, current_price, buy_price)
            total_portfolio_value += stock_value

            print(f"\n📈 {symbol}: {shares} Shares")
            print(f"💰 Buy Price: ${buy_price:.2f}, Current Price: ${current_price:.2f}")
            print(f"🏷️ Total Value: ${stock_value:.2f}")

            if profit_or_loss > 0:
                print(f"✅ Profit: ${profit_or_loss:.2f}")
            elif profit_or_loss < 0:
                print(f"❌ Loss: ${-profit_or_loss:.2f}")
            else:
                print("⚖️ No Profit or Loss.")
        else:
            print(f"\n🚫 Skipped {symbol} due to missing price.\n")

    print("-" * 40)
    print(f"💼 Total Portfolio Value: ${total_portfolio_value:.2f}\n")

# Remove Stock From Portfolio
def remove_stock(symbol):
    for stock in portfolio:
        if stock['symbol'] == symbol:
            portfolio.remove(stock)
            print(f"🗑️ Removed {symbol} from portfolio.")
            return
    print(f"⚠️ {symbol} not found in portfolio.")

# Main Program Loop
running = True
while running:
    print("""
=========== 📊 Stock Portfolio Menu ===========
1️⃣ Add Stock
2️⃣ Display Portfolio
3️⃣ Remove Stock
0️⃣ Exit
==============================================
""")
    try:
        choice = int(input("👉 Choose an option (0-3): "))
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
        continue

    if choice == 1:
        symbol = input("📜 Enter Stock Symbol: ").upper()
        try:
            shares = int(input("🔢 Enter number of shares: "))
            buy_price = float(input("💵 Enter buy price per share: "))
            add_stock(symbol, shares, buy_price)
        except ValueError:
            print("❌ Invalid input. Please enter valid numbers.")
    elif choice == 2:
        display_portfolio()
    elif choice == 3:
        symbol = input("🗑️ Enter stock symbol to remove: ").upper()
        remove_stock(symbol)
    elif choice == 0:
        print("👋 Exiting program... Goodbye!")
        running = False
    else:
        print("❌ Invalid choice. Please try again.")