#!/usr/bin/env bash

./docker/run "python -m tasks.data_creation"
./docker/run "python -m tasks.model_preprocessing"
./docker/run "python -m tasks.model_preparation"
./docker/run "python -m tasks.model_testing"
