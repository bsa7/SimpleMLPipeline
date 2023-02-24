# Simple Machine Learning Pipeline

This application implements the simplest pipeline, including:
  - CI - continious integration;
  - CD - continious deployment;
  - CT - continious training;

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
