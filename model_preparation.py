''' This file contains script which creates and trains
    a machine learning model on the built data '''

from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
import itertools
import numpy as np
import pandas as pd
import warnings

from app.models.candle import Candle
from app.models.best_hyperparameter import BestHyperparameter
from app.lib.utils import timestamp_to_formatted_date

warnings.simplefilter('ignore')

print('1. Initializes DataFrame')
df = pd.DataFrame({ 'ds': [], 'y': [] })

print('2. Loading data')
for item in Candle.where():
  ds = item.get('ds')
  y = item.get('y')
  if ds is not None and y is not None:
    df = df.append({ 'ds': timestamp_to_formatted_date(ds), 'y': y }, ignore_index = True)

print('3. Initialize and fit model, search best combination of hyperparameters')
param_grid = {
  'changepoint_prior_scale': [0.001, 0.01, 0.1, 0.5],
  'seasonality_prior_scale': [0.01, 0.1, 1.0, 10.0],
}

# Generate all combinations of parameters
all_params = [dict(zip(param_grid.keys(), v)) for v in itertools.product(*param_grid.values())]
rmses = []  # Store the RMSEs for each params here

# Use cross validation to evaluate all parameters
for params in all_params:
  model = Prophet(**params).fit(df)  # Fit model with given params
  df_cv = cross_validation(model, horizon = '30 days', parallel = 'processes')
  df_p = performance_metrics(df_cv, rolling_window = 1)
  rmses.append(df_p['rmse'].values[0])

# Find the best parameters
tuning_results = pd.DataFrame(all_params)
tuning_results['rmse'] = rmses
print(tuning_results)

# Select the best params
best_params = all_params[np.argmin(rmses)]
print(f'{best_params=}')

BestHyperparameter.insert_one(ai_model = 'prophet', **best_params)
