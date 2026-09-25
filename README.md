# RESTCONF-Event-Monitor
A Python application for interacting with a RESTCONF API, retrieving network events, and filtering them by severity.
RESTCONF Event Monitor

A Python application for interacting with a RESTCONF API, retrieving network events, and filtering them by severity.

The project demonstrates how to authenticate against an API, work with Bearer tokens, send RESTCONF requests, parse nested JSON responses, and process event data using Python.

## Features

* API authentication

* Bearer token authentication

* RESTCONF API requests

* JSON request and response handling

* Nested JSON parsing

* Event filtering by severity

* Environment-based configuration

* Basic HTTP error handling

## Technologies
* Python 3
* Requests
* RESTCONF
* REST API
* JSON


## Installation


* cd restconf-event-monitor
* Create a virtual environment:
* python -m venv .venv
Install the dependencies:
* pip install -r requirements.txt


## Usage

Run the application:

python main.py


The application authenticates with the API, retrieves network events, and filters them by severity.

Example:

------------ Major Events ------------

{
    'description': 'Operational status went down...',
    'event-identity': 'interface-oper-status-down-alarm',
    'severity': 'Major',
    ...
}

------------ Critical Events ------------

{
    'description': 'The internal tx power...',
    'event-identity': 'transceiver-low-tx-power-alarm',
    'severity': 'Critical',
    ...
}

## API Response

The API returns a nested JSON structure containing event information.

Simplified example:

{
  "output": {
    "events": {
      "cursor": 25,
      "event": [
        {
          "description": "Example event",
          "event-identity": "example-alarm",
          "object-name": "device-1",
          "severity": "Critical"
        }
      ],
      "total-count": 87
    }
  }
}


The event list can be extracted using:

events = response.json()["output"]["events"]["event"]


Individual event properties can then be accessed:

event["description"]
event["severity"]
event["object-name"]
event["event-identity"]


## Purpose

This project was created as a practical Python example for working with RESTCONF APIs and network event data.

It focuses on:
* API authentication
* HTTP requests
* JSON parsing
* RESTCONF communication
* Processing structured network events
* Filtering events by severity


