import requests


def collect_live_measurements():
    url = "http://127.0.0.1:8000/realTime"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("Live Measurements:")
        print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Failed to get live measurements: {e}")
        return None


def collect_average_measurements(period=10):
    url = f"http://127.0.0.1:8000/average?period={period}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("\nAverage Measurements:")
        print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Failed to get average measurements: {e}")
        return None


def collect_configuration():
    url = "http://127.0.0.1:8000/podConfiguration"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("\nConfiguration Data:")
        print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Failed to get configuration data: {e}")
        return None



