from fastapi import FastAPI
import random
import time
import datetime 
from datetime import datetime, timedelta
from typing import List
import json

app = FastAPI()

# Function to generate a list of dummy errors
def generate_dummy_errors():
    return [
        {
            "idFailure": random.randint(1000, 9999),
            "startTime": (datetime.now() - timedelta(hours=random.randint(1, 24))).strftime('%Y-%m-%dT%H:%M:%S.000Z'),
            "failureType": random.choice(["HighWT", "LowCF"]),
            "description": random.choice([
                "High Input Water Temperature",
                "Low Coolant Flow",
                "Pump Failure",
                "Fan Speed Failure"
            ])
        }
    ]

# Function to generate a list of dummy warnings
def generate_dummy_warnings():
    return [
        {
            "idWarning": random.randint(1000, 9999),
            "startTime": (datetime.now() - timedelta(hours=random.randint(1, 24))).strftime('%Y-%m-%dT%H:%M:%S.000Z'),
            "warningType": random.choice(["LowCF", "HighWT"]),
            "description": random.choice([
                "Low Coolant Flow",
                "High Water Temperature Warning"
            ])
        }
    ]



# Function to generate a list of fixed dummy errors
def generate_dummy_fixed_errors():
    start_time = (datetime.now() - timedelta(hours=random.randint(1, 24))).strftime('%Y-%m-%dT%H:%M:%S.000Z')
    end_time = (datetime.now() - timedelta(hours=random.randint(0, 1))).strftime('%Y-%m-%dT%H:%M:%S.000Z')
    return [
        {
            "idFailure": random.randint(1000, 9999),
            "startTime": start_time,
            "failureType": "HighWT",
            "description": "High Input Water Temperature",
            "endTime": end_time
        }
    ]




# Function to generate a list of fixed dummy warnings
def generate_dummy_fixed_warnings():
    start_time = (datetime.now() - timedelta(hours=random.randint(1, 24))).strftime('%Y-%m-%dT%H:%M:%S.000Z')
    end_time = (datetime.now() - timedelta(hours=random.randint(0, 1))).strftime('%Y-%m-%dT%H:%M:%S.000Z')
    return [
        {
            "idWarning": random.randint(1000, 9999),
            "startTime": start_time,
            "warningType": "LowCF",
            "description": "Low Coolant Flow",
            "endTime": end_time
        }
    ]

# Function to generate dummy live measurements
def generate_live_measurements():
    live_data = {
        "meta": ["Dummy data generated for testing purposes"],
        "data": {
            "temperature": round(random.uniform(20.0, 50.0), 2),
            "cti": round(random.uniform(30.0, 55.0), 2),  # Coolant temperature inlet
            "cto": round(random.uniform(30.0, 55.0), 2),  # Coolant temperature outlet
            "cf": round(random.uniform(1.0, 10.0), 2),  # Coolant flow
            "wti": round(random.uniform(20.0, 40.0), 2),  # Water temperature inlet
            "wto": round(random.uniform(25.0, 45.0), 2),  # Water temperature outlet
            "wf": round(random.uniform(1.0, 5.0), 2),  # Water flow
            "consumption": random.randint(500, 1000),  # Smartpod consumption
            "dissipation": round(random.uniform(1.0, 5.0), 2),  # Dissipation in kW
            "mpue": round(random.uniform(0.9, 1.5), 2),  # mPUE
            "errors": generate_dummy_errors(),  # Current list of errors
            "fixedErrors": generate_dummy_fixed_errors(),  # List of fixed errors
            "warnings": generate_dummy_warnings(),  # Current list of warnings
            "fixedWarnings": generate_dummy_fixed_warnings(),  # List of fixed warnings
            "pump1status": random.choice([0, 1]),  # 0: Stopped, 1: Running
            "pump1rpm": random.randint(1000, 3000),  # Pump 1 RPM
            "pump2status": random.choice([0, 1]),  # 0: Stopped, 1: Running
            "pump2rpm": random.randint(1000, 3000),  # Pump 2 RPM
            "dissipationC": 0,  # Dissipation of the coolant (in kW)
            "dissipationW": 0,  # Dissipation of the water (in kW)
            "setpoint": random.randint(45, 55),  # Coolant temperature setpoint
            "alarm": random.randint(50, 60),  # Coolant alarm temperature
            "cpu0temp": random.randint(45, 60),  # CPU 0 temperature
            "cpu1temp": random.randint(45, 60),  # CPU 1 temperature
            "mode": "normal",  # Current mode of the Smartpod
            "test": None,  # Test routine status
            "maintenance": None,  # Maintenance routine status
            "demo": False,  # Demo routine status
            "factory": False  # Factory mode status
        }
    }
    return live_data


# Function to generate dummy average measurements
def generate_average_measurements():
    dummy_data = {
        "meta": [
            "Dummy data generated for testing purposes"
        ],
        "data": [
            {
                "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z'),
                "temperature": round(random.uniform(20.0, 50.0), 2),
                "consumption": round(random.uniform(500, 1000), 2),
                "dissipation": round(random.uniform(1.0, 5.0), 2),
                "mpue": round(random.uniform(0.9, 1.5), 2),
                "pump1rpm": str(random.randint(1000, 3000)),
                "pump2rpm": str(random.randint(1000, 3000)),
                "cti": round(random.uniform(30.0, 50.0), 2),  # Coolant temperature inlet
                "cto": round(random.uniform(30.0, 50.0), 2),  # Coolant temperature outlet
                "cf": round(random.uniform(3.0, 6.0), 2),  # Coolant flow
                "wti": round(random.uniform(20.0, 40.0), 2),  # Water temperature inlet
                "wto": round(random.uniform(25.0, 45.0), 2),  # Water temperature outlet
                "wf": round(random.uniform(3.0, 6.0), 2),  # Water flow
                "errors": generate_dummy_errors(),
                "warnings": generate_dummy_warnings(),
                "setpoint": random.randint(45, 55),
                "cpu0temp": random.randint(45, 60),
                "cpu1temp": random.randint(45, 60)
            }
        ]
    }
    return dummy_data

# Function to generate dummy configuration data
def generate_configuration_data():
    config_data = {
        "data": {
            "values": {
                "ctAlarm": random.randint(30, 70),
                "wtAlarm": random.randint(30, 70),
                "wfAlarm": random.randint(30, 70),
                "timezone": "UTC",
            },
            "limits": {
                "setpoint": {
                    "max": random.randint(60, 80),
                    "min": random.randint(20, 40),
                    "required": True
                },
                "ctAlarm": {
                    "max": random.randint(60, 80),
                    "min": random.randint(20, 40),
                    "required": True
                },
                "wtAlarm": {
                    "max": random.randint(60, 80),
                    "min": random.randint(20, 40),
                    "required": True
                },
                "wfAlarm": {
                    "max": random.randint(60, 80),
                    "min": random.randint(20, 40),
                    "required": True
                }
            }
        }
    }
    return config_data

# API Endpoint to fetch live measurements
@app.get("/realTime")
def get_live_measurements():
    return generate_live_measurements()

# API Endpoint to fetch average measurements
@app.get("/average")
def get_average_measurements(period: int = 10):
    return generate_average_measurements()

# API Endpoint to fetch current configuration
@app.get("/podConfiguration")
def get_configuration():
    return generate_configuration_data()

# Run the server using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
