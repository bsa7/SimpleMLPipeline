''' This file contains script for model testing '''
import matplotlib.pyplot as plt
import warnings
from prophet.serialize import model_from_json
from app.models.trained_model_serialized import TrainedModelSerialized
from app.use_cases.candle_train_test_split import CandleTrainTestSplit

warnings.simplefilter('ignore')

# initializing constants
INSTRUMENT_NAME = 'BTC_USDT'

# Load data
tp = CandleTrainTestSplit().time_series_split_points(instrument_name = INSTRUMENT_NAME)
df = CandleTrainTestSplit().load_data(instrument_name = INSTRUMENT_NAME, train = True, test = True)

# Restore previously serialized model from database
json_data = TrainedModelSerialized.restore(model_name = 'prophet', instrument_name = INSTRUMENT_NAME)
best_model = model_from_json(json_data)

# Make predictions
future = best_model.make_future_dataframe(periods = 32, freq = 'D', include_history = True)
forecast_df = best_model.predict(future)
forecast_df['ds'] = forecast_df['ds'].apply(lambda ds: str(ds)[:10])

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
