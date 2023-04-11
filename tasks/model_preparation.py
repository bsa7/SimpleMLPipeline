''' This file contains script which creates and trains
    a machine learning model on the built data '''

import itertools
import pandas as pd
import warnings
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
from prophet.serialize import model_to_json

from app.models.best_hyperparameter import BestHyperparameter
from app.models.trained_model_serialized import TrainedModelSerialized
from app.lib.utils import current_timestamp
from app.use_cases.candle_train_test_split import CandleTrainTestSplit

warnings.simplefilter('ignore')

INSTRUMENT_NAME = 'BTC_USDT'
DATE_FORMAT = '%Y-%m-%d'

print('1. Initializes DataFrame, collect information about time series.')
tp = CandleTrainTestSplit().time_series_split_points(instrument_name = INSTRUMENT_NAME)

print(f"2. Loading data for training from {tp['oldest_candle_date']} to {tp['splitting_date']}")
df = CandleTrainTestSplit().load_data(instrument_name = INSTRUMENT_NAME, train = True, test = False)

print('3. Initialize and fit model, search best combination of hyperparameters')
param_grid = {
  'seasonality_prior_scale': [0.015],
  # Bulk experiments have shown that the best set of hyperparameters is the value above.
  # You can experiment:

  # 'changepoint_prior_scale': [0.01, 0.1, 1.0, 10.0],
  # 'seasonality_prior_scale': [0.01, 0.1, 1.0, 10.0],
  # 'holidays_prior_scale': [0.01, 0.1, 1.0, 10.0],
  # 'seasonality_mode': ['additive', 'multiplicative'],
}

# Generate all combinations of parameters
all_params = [dict(zip(param_grid.keys(), v)) for v in itertools.product(*param_grid.values())]
rmses = []  # Store the RMSEs for each params here

# Use cross validation to evaluate all parameters
best_model = None
for params in all_params:
  model = Prophet(**params).fit(df)  # Fit model with given params
  df_cv = cross_validation(model, horizon = '30 days', parallel = 'processes')
  df_p = performance_metrics(df_cv, rolling_window = 1)
  rmse = df_p['rmse'].values[0]
  rmses.append(rmse)
  if rmse >= max(rmses):
    best_model = model

# Find the best parameters
tuning_results = pd.DataFrame(all_params)
tuning_results['rmse'] = rmses

# Select the best params
best_params = tuning_results[tuning_results['rmse'] == tuning_results['rmse'].min()].iloc[0].to_dict()
print('4. Best hyperparameters found:')
print(best_params)
print('   Tuning_results:')
print(tuning_results)

# Store best hyperparameters in our database:
BestHyperparameter.insert_one(ai_model = 'prophet', ds = current_timestamp(), **best_params)

# Serialize model and save its into database
best_model_serialized = model_to_json(best_model)
TrainedModelSerialized.store(model_name = 'prophet',
                             model_data = best_model_serialized,
                             instrument_name = INSTRUMENT_NAME)
