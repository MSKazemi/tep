# TEP

## Description

In this Python project we provided scripts to collect data from the Submer API endpoints and publish it to Examon monitoring system. The project runs continuously, collecting live, average, and configuration data at regular intervals.

## Requirements

- Python 3.12
- Poetry

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd tep
    ```

2. Install dependencies using Poetry:
    ```sh
    poetry install
    ```

## Usage


To run the project, execute the following command:
```sh
poetry run python data_gen.py
```

```sh
poetry run python main.py
```

The script will continuously collect data from the Submer API and publish it to Examon every 60 seconds.

## Project Structure

```
.
├── __init__.py
├── data_gen.py
├── examon_collector.py
├── examon_publisher.py
├── main.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── submer_collector.py
└── tests/
    └── __init__.py
```

## Modules

- **main.py**: Entry point of the application. Collects data and publishes it at regular intervals.
- **submer_collector.py**: Contains functions to collect live, average, and configuration data from the Submer API.
- **examon_collector.py**: (Placeholder for future use)
- **examon_publisher.py**: Contains functions to publish data to Examon.
- **data_gen.py**: Since the Submer API is not available, this script generates dummy data for testing purposes.

## Configuration

The project uses Poetry for dependency management. Ensure you have Poetry installed before running the project.

## License

This project is licensed under the MIT License.