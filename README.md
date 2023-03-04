![Pylint](https://github.com/bsa7/SimpleMLPipeline/actions/workflows/pylint.yml/badge.svg)&nbsp;
![Pytest](https://github.com/bsa7/SimpleMLPipeline/actions/workflows/pytest.yml/badge.svg)&nbsp;

# Simple Machine Learning Pipeline

This application implements the simplest pipeline, including:
  - CI - continious integration;
  - CD - continious deployment;
  - CT - continious training;

## A complete iteration consists of the following operations:
1. Receiving new data from a third-party API - obtaining information about candles for a particular instrument: maximum and minimum prices, as well as opening and closing prices;
2. Pre-processing of data received in the API - for each candle, the average value is calculated, between the maximum and minimum prices for the candle;
3. Saving new data in the data warehouse. The key for the record is the timestamp, and the value is the average price of the instrument per candle;
4. The model is retrained according to the newly obtained values. In this case, before training, the previously obtained weights of the model are loaded from the storage;
5. The quality of the model training is assessed;

### Getting new data from a third party API:
* First, a time limit is determined, before which information on candlesticks has already been obtained in previous iterations;

* One or more requests are made to the API for fresh data;

### Pre-processing of data received in the API
Before storing the data in the storage, they are preliminarily prepared. For each candle, the average value is calculated, according to its maximum and minimum values. Thus, each moment of time in the data corresponds to one number - the average value of the candle for a time interval equal to the difference between the current and previous moments.

### Saving new data in the data warehouse
Data is saved to the key-value database so that each candlestick has one record with timestamp `ds` and one numeric value `y`.

### Training of the model
The first time we train the model on all available data.
After replenishing the time series, each time we retrain the model, adding to the time series used in previous iterations, a small part of the fresh data in comparison. With each such training, the model is restored from previously saved settings, retrained, and its settings are saved for subsequent iterations.

## Application settings
The application has several environments. For development, this environment is called development. For testing - test. For a working server, this environment is called production.
All development environment settings are described in the ./.env file.
You would to copy file ./.env.example to ./.env for first time in your local development environment and customize settings.

## Continious Integration

There are several types of checks that should be run before submitting code to make sure everything is fine.

### Linters

To run pylint:

```bash
./scripts/run_pylint
```

### Unit testing

To run unit tests:

```bash
./scripts/run_pytest
```

