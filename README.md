# 📊 Stock Portfolio Tracker

A simple Python-based stock portfolio tracker that helps you manage your investments by adding, viewing, and removing stocks. It also calculates the current value and profit/loss for each stock.

----------

## 🚀 **Features**

-   📈 Add stocks with symbol, number of shares, and buy price.
    
-   💰 Fetch real-time stock prices using `yfinance`.
    
-   📊 Display portfolio with total value and profit/loss per stock.
    
-   🗑️ Remove stocks from the portfolio.
    
-   ⚙️ User-friendly menu for easy navigation.
    

----------

## ⚙️ **Installation**

### 1. **Clone the repository:**

```
git clone https://github.com/Shadyelsawy536/Stock-Portfolio-Tracker.git
cd Stock-Portfolio-Tracker
```

### 2. **Create virtual environment (optional but recommended):**

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. **Install dependencies:**

```
pip install yfinance
```

----------

## 📖 **Usage**

### 1. **Run the program:**

```
python portfolio_tracker.py
```

### 2. **Menu options:**

-   `1️⃣ Add Stock:` Enter stock symbol, shares, and buy price.
    
-   `2️⃣ Display Portfolio:` View current value, profit/loss.
    
-   `3️⃣ Remove Stock:` Remove stock by symbol.
    
-   `0️⃣ Exit:` Close the program.
    

----------

## 🛠️ **Example Output**

```
=========== 📊 Stock Portfolio Menu ===========
1️⃣ Add Stock
2️⃣ Display Portfolio
3️⃣ Remove Stock
0️⃣ Exit
==============================================

👉 Choose an option (0-3): 1
📜 Enter Stock Symbol: AAPL
🔢 Enter number of shares: 10
💵 Enter buy price per share: 150.0
✅ Added AAPL: 10 shares at $150.00 each.
```

----------

## 📝 **Requirements**

-   Python 3.8+
    
-   `yfinance` package
    

Install with:

```
pip install yfinance
```

----------

## 🤝 **Contributing**

Feel free to fork this repo, make your changes, and submit a pull request!

----------

## 📄 **License**

This project is licensed under the **MIT License** – see the LICENSE file for details.

----------

💡 **Made with ❤️ by** [**Your Name**](https://github.com/YourUsername)
