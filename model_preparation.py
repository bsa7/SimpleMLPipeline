''' This file contains script which creates and trains
    a machine learning model on the built data '''

from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
import itertools
import matplotlib.pyplot as plt
import pandas as pd
import warnings

from app.models.candle import Candle
from app.models.best_hyperparameter import BestHyperparameter
from app.lib.utils import current_timestamp, days, timestamp_to_formatted_date

warnings.simplefilter('ignore')
INSTRUMENT_NAME = 'BTC_USDT'
DATE_FORMAT = '%Y-%m-%d'

print('1. Initializes DataFrame, collect information about time series.')
df = pd.DataFrame({ 'ds': [], 'y': [], 'y_test': [], 'y_hat': [] })
latest_candle = Candle.get_latest(instrument = INSTRUMENT_NAME).limit(1).next()
latest_candle_timestamp = latest_candle.get('ds')
latest_candle_date = timestamp_to_formatted_date(latest_candle_timestamp)
oldest_candle = Candle.get_oldest(instrument = INSTRUMENT_NAME).limit(1).next()
oldest_candle_timestamp = oldest_candle.get('ds')
oldest_candle_date = timestamp_to_formatted_date(oldest_candle_timestamp)
splitting_timestamp = latest_candle_timestamp - days(30)
splitting_date = timestamp_to_formatted_date(splitting_timestamp)

print(f'2. Loading data for training from {oldest_candle_date} to {splitting_date}')
for item in Candle.where(ds = { '$lt': splitting_timestamp }).sort([('ds', 1)]):
  ds = item.get('ds')
  y = item.get('y')
  if ds is not None and y is not None:
    df = df.append({ 'ds': timestamp_to_formatted_date(ds), 'y': y }, ignore_index = True)

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

# Make predictions
future = best_model.make_future_dataframe(periods = 32, freq = 'D', include_history = True)
forecast_df = best_model.predict(future)
forecast_df['ds'] = forecast_df['ds'].apply(lambda ds: str(ds)[:10])

# Fill the dataframe with test values
for item in Candle.where(ds = { '$gte': splitting_timestamp }).sort([('ds', 1)]):
  ds = item.get('ds')
  ds_formatted = timestamp_to_formatted_date(ds)
  y = item.get('y')
  if ds is not None and y is not None:
    df = df.append({ 'ds': ds_formatted, 'y_test': y }, ignore_index = True)

# Fill the dataframe with predicted values
df = df.set_index('ds').join(forecast_df[['ds', 'yhat']].set_index('ds'))

# Plot training, test and predicted values
figure, ax = plt.subplots(figsize = (12, 4), layout = 'constrained')
y_train_plot = ax.plot(df['y'], label = 'y_train')
y_test_plot = ax.plot(df['y_test'], label = 'y_test')
y_hat_plot = ax.plot(df['yhat'], label = 'y_hat')
ax.legend()
ax.set_xlabel('Date')
ax.xaxis.set_major_locator(plt.MaxNLocator(30))
ax.tick_params(axis = 'x', labelrotation = 45, color = 'r', labelcolor = 'r')
ax.set_ylabel('Cost')
ax.set_title(f'{INSTRUMENT_NAME} cost Plot')
# plt.savefig('./tmp/plot.png')
plt.show()
