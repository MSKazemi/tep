import json
from datetime import datetime

def json_to_examon_data_model(data):
    # Get the current timestamp in ISO format
    timestamp = datetime.utcnow().isoformat() + 'Z'
    
    # Keys to exclude from the initial processing
    exclude_keys = {"fixedWarnings", "fixedErrors", "errors", "warnings"}
    
    # Iterate over the data dictionary and process general keys
    for key, value in data['data'].items():
        if key not in exclude_keys:
            line = f'org/tep/submer/{key}/topic_end {value}; {timestamp}'
            yield line
    
    # Process fixedWarnings
    if 'fixedWarnings' in data['data']:
        for item in data['data']['fixedWarnings']:
            idWarning = item.get('idWarning', '')
            startTime = item.get('startTime', '')
            description = item.get('description', '')
            endTime = item.get('endTime', '')
            warningType = item.get('warningType', '')
            
            dt_model = (f'org/tep/submer/fixedWarnings/{idWarning}/startTime/{startTime}/description/{description}/endTime/{endTime}/warningType/{warningType}/idWarning/topic_end {idWarning}; {timestamp}')
            yield dt_model
    
    # Process fixedErrors
    if 'fixedErrors' in data['data']:
        for item in data['data']['fixedErrors']:
            idFailure = item.get('idFailure', '')
            startTime = item.get('startTime', '')
            description = item.get('description', '')
            endTime = item.get('endTime', '')
            failureType = item.get('failureType', '')
            # Form the path
            dt_model = (f'org/tep/submer/fixedErrors/{idFailure}/startTime/{startTime}/description/{description}/endTime/{endTime}/failureType/{failureType}/idFailure/topic_end {idFailure}; {timestamp}')
            yield dt_model
    
    # Process errors
    if 'errors' in data['data']:
        for item in data['data']['errors']:
            idFailure = item.get('idFailure', '')
            startTime = item.get('startTime', '')
            description = item.get('description', '')
            failureType = item.get('failureType', '')
            # Form the path
            dt_model = (f'org/tep/submer/errors/{idFailure}/startTime/{startTime}/description/{description}/failureType/{failureType}/idFailure/topic_end {idFailure}; {timestamp}')
            yield dt_model
    
    # Process warnings
    if 'warnings' in data['data']:
        for item in data['data']['warnings']:
            idWarning = item.get('idWarning', '')
            startTime = item.get('startTime', '')
            description = item.get('description', '')
            warningType = item.get('warningType', '')
            # Form the path
            path = (f'org/tep/submer/warnings/{idWarning}/startTime/{startTime}/description/{description}/warningType/{warningType}/idWarning/topic_end {idWarning}; {timestamp}')
            yield path


def parse_line(line):
    """
    Parses a line in the format:
    'org/tep/submer/<path> <value>; <timestamp>'
    and returns the topic and message separately.
    """
    try:
        # Split the line at the first space
        topic_part, rest = line.split('/topic_end', 1)
        # The message includes the value and timestamp
        message = rest.strip()
        # The topic is the topic_part without trailing slash
        topic = topic_part.rstrip('/')
        return topic, message
    except ValueError:
        # If the line doesn't match the expected format
        return None, None
    
# Sample JSON data as a string
json_data = '''
{
  "meta": [
    "Dummy data generated for testing purposes"
  ],
  "data": {
    "temperature": 32.05,
    "cti": 51.15,
    "cto": 53.78,
    "cf": 4.57,
    "wti": 32.8,
    "wto": 42.43,
    "wf": 2.43,
    "consumption": 992,
    "dissipation": 1.95,
    "mpue": 1.2,
    "errors": [
      {
        "idFailure": 2080,
        "startTime": "2024-09-25T09:12:01.000Z",
        "failureType": "HighWT",
        "description": "Fan Speed Failure"
      }
    ],
    "fixedErrors": [
      {
        "idFailure": 1900,
        "startTime": "2024-09-25T13:12:01.000Z",
        "failureType": "HighWT",
        "description": "High Input Water Temperature",
        "endTime": "2024-09-25T17:12:01.000Z"
      }
    ],
    "warnings": [
      {
        "idWarning": 5539,
        "startTime": "2024-09-25T06:12:01.000Z",
        "warningType": "HighWT",
        "description": "High Water Temperature Warning"
      }
    ],
    "fixedWarnings": [
      {
        "idWarning": 5617,
        "startTime": "2024-09-25T07:12:01.000Z",
        "warningType": "LowCF",
        "description": "Low Coolant Flow",
        "endTime": "2024-09-25T17:12:01.000Z"
      }
    ],
    "pump1status": 1,
    "pump1rpm": 1017,
    "pump2status": 0,
    "pump2rpm": 1188,
    "dissipationC": 0,
    "dissipationW": 0,
    "setpoint": 45,
    "alarm": 58,
    "cpu0temp": 46,
    "cpu1temp": 53,
    "mode": "normal",
    "test": null,
    "maintenance": null,
    "demo": false,
    "factory": false
  }
}
'''
