![Pylint](https://github.com/bsa7/SimpleMLPipeline/actions/workflows/pylint.yml/badge.svg)&nbsp;
![Pytest](https://github.com/bsa7/SimpleMLPipeline/actions/workflows/pytest.yml/badge.svg)&nbsp;

# Simple Machine Learning Pipeline

This application implements the simplest pipeline, including:
  - CI - continious integration;
  - CD - continious deployment;
  - CT - continious training;

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

