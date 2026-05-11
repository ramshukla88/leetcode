# Production-Oriented Sales Forecasting System

# Background
# You are designing a simplified sales forecasting service used by downstream systems for:
# Inventory planning
# Pricing optimization
# Supply chain alerts
# You need to generate sample data by using code provided:
# Historical labeled data
# Incoming new sales data over time
# Sales patterns may change due to:
# Promotions
# Seasonality shifts
# Product lifecycle changes

# Task Requirements
# Part 1: Baseline Forecasting Model
# Train an initial forecasting model using historical data.
# Justify your choice of:
# Model type (statistical vs ML)
# Forecast horizon
# Feature strategy

# Part 2: Change / Drift Awareness
# Design and implement a mechanism to detect:
# Data drift (feature distribution changes)
# OR forecast error degradation over time
# Clearly explain your detection logic.

# Part 3: Model Lifecycle & Reliability
# Propose (and optionally implement):
# Model retraining triggers
# Model fallback strategy (e.g., simple baseline vs complex model)
# Explain how you would:
# Roll out a new model safely
# Avoid business disruption

# Output Expectations
# Clean, modular code
# Clear separation of:
# Data processing
# Forecasting logic
# Monitoring
# A short README covering:
# Assumptions
# Limitations
# Production considerations

# What We Evaluate (Internally)
# ✅ Ability to connect forecasts to business decisions
# ✅ Time-series awareness beyond “fit a model”
# ✅ Production thinking (monitoring, fallback, retraining)
# ✅ Clarity of communication
# ⚠️ Strong senior signals:
# Multiple baselines
# Error-based retraining triggers
# Sensible simplifications
# Awareness of forecast stability

import pandas as pd
import numpy as np
from datetime import timedelta

np.random.seed(42)

stores = ["S001", "S002", "S003"]
products = ["P001", "P002"]
start_date = pd.to_datetime("2023-01-01")

def generate_sales(base, day, promo, drift=False):
    seasonality = 8 * np.sin(2 * np.pi * day / 7)
    promo_boost = 25 if promo else 0
    drift_boost = 20 if drift else 0
    noise = np.random.normal(0, 4)
    return max(0, int(base + seasonality + promo_boost + drift_boost + noise))

train_rows = []
incremental_rows = []
truth_rows = []

# -------- TRAIN DATA (Stable Period) --------
for store in stores:
    for product in products:
        base = np.random.randint(60, 120)
        price = np.random.uniform(10, 18)

        for day in range(120):
            date = start_date + timedelta(days=day)
            promo = 1 if day % 28 in [0, 1, 2] else 0

            sales = generate_sales(base, day, promo)
            train_rows.append([
                date.date(), store, product, sales,
                round(price * (0.9 if promo else 1.0), 2),
                promo, 800 - day * 2
            ])

# -------- INCREMENTAL DATA (With Drift) --------
for store in stores:
    for product in products:
        base = np.random.randint(60, 120) * 1.2  # demand shift
        price = np.random.uniform(9, 15)        # price regime change

        for day in range(120, 180):
            date = start_date + timedelta(days=day)
            promo = 1 if day % 14 in [0, 1, 2, 3] else 0

            sales = generate_sales(base, day, promo, drift=True)
            incremental_rows.append([
                date.date(), store, product,
                round(price * (0.85 if promo else 1.0), 2),
                promo, 500 - day
            ])
            truth_rows.append([
                date.date(), store, product, sales
            ])

# Convert to DataFrames
train_df = pd.DataFrame(train_rows, columns=[
    "date", "store_id", "product_id",
    "sales", "price", "promotion_flag", "inventory_level"
])

incremental_df = pd.DataFrame(incremental_rows, columns=[
    "date", "store_id", "product_id",
    "price", "promotion_flag", "inventory_level"
])

truth_df = pd.DataFrame(truth_rows, columns=[
    "date", "store_id", "product_id", "actual_sales"
])

train_df.to_csv("train.csv", index=False)
incremental_df.to_csv("incremental.csv", index=False)
truth_df.to_csv("ground_truth.csv", index=False)

print("Files generated:")
print("train.csv:", len(train_df))
print("incremental.csv:", len(incremental_df))
print("ground_truth.csv:", len(truth_df))
