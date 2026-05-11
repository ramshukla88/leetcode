import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error

train = pd.read_csv("train.csv", parse_dates=["date"], index_col="date")
test = pd.read_csv("incremental.csv", parse_dates=["date"], index_col="date")
ground_truth = pd.read_csv("ground_truth.csv", parse_dates=["date"], index_col="date")

# Fit ARIMA(1,1,1) on training sales
mod = ARIMA(train["sales"], order=(1, 1, 1))
mod_fit = mod.fit()
print(mod_fit.summary())

# Forecast daily sales for the test period
print("\n=== Forecast Predictions ===")
forecast = mod_fit.forecast(steps=len(test))
forecast.index = test.index
forecast.name = "predicted_sales"

# Display predictions alongside ground truth
results = pd.DataFrame({
    "predicted_sales": forecast.round(2),
    "actual_sales": ground_truth["actual_sales"],
})
print(results.to_string())

# Evaluate forecast accuracy
mae = mean_absolute_error(ground_truth["actual_sales"], forecast)
print(f"\nMAE: {mae:.2f}")
