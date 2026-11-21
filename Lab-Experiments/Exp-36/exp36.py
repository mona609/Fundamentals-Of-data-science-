import pandas as pd
import matplotlib.pyplot as plt

stock = pd.read_csv("stock_data.csv")
stock["date"] = pd.to_datetime(stock["date"])
price = stock["close"]

# ---------- Variability of the closing price ----------
print("Closing price statistics:")
print(f"  Mean                      : {price.mean():.2f}")
print(f"  Variance                  : {price.var():.2f}")
print(f"  Standard deviation        : {price.std():.2f}")
print(f"  Range (max - min)         : {price.max() - price.min():.2f}")
print(f"  Coefficient of variation  : {price.std() / price.mean() * 100:.2f}%")

# ---------- Daily returns ----------
stock["return"] = price.pct_change() * 100
print("\nDaily return statistics:")
print(f"  Average daily return      : {stock['return'].mean():.3f}%")
print(f"  Volatility (std of return): {stock['return'].std():.3f}%")

best = stock.loc[stock["return"].idxmax()]
worst = stock.loc[stock["return"].idxmin()]
print(f"  Best day  : {best['date'].date()} ({best['return']:.2f}%)")
print(f"  Worst day : {worst['date'].date()} ({worst['return']:.2f}%)")

# ---------- Moving average and rolling variability ----------
stock["ma7"] = price.rolling(7).mean()
stock["std7"] = price.rolling(7).std()
print(f"\nHighest 7-day rolling std: {stock['std7'].max():.2f}")

# ---------- Plots ----------
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

axes[0].plot(stock["date"], price, label="Close")
axes[0].plot(stock["date"], stock["ma7"], label="7-day average", color="red")
axes[0].set_title("Closing Price")
axes[0].set_xlabel("Date")
axes[0].set_ylabel("Price")
axes[0].tick_params(axis="x", rotation=45)
axes[0].legend()

axes[1].hist(stock["return"].dropna(), bins=12, color="orange", edgecolor="black")
axes[1].set_title("Distribution of Daily Returns")
axes[1].set_xlabel("Daily return (%)")
axes[1].set_ylabel("Number of days")

plt.tight_layout()
plt.show()
