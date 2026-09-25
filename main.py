import os
import requests


# Configuration
URL_TOKEN = os.getenv(
    "API_TOKEN_URL",
    "https://example.com/api/restconf/operations/auth-token:request-token"
)

URL_EVENTS = os.getenv(
    "API_EVENTS_URL",
    "https://example.com/api/restconf/operations/event-workflow:get-events"
)

USERNAME = os.getenv("API_USERNAME")
PASSWORD = os.getenv("API_PASSWORD")


def get_token():
    credentials = {
        "username": USERNAME,
        "password": PASSWORD
    }

    response = requests.post(
        URL_TOKEN,
        verify=False,
        json=credentials
    )

    response.raise_for_status()

    return response.json()["token"]


def get_events(token):
    request_body = {
        "input": {
            "summary-field": "severity",
            "current": True,
            "cursor": 0,
            "result-size": 25,
            "exact-match": True
        }
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        URL_EVENTS,
        verify=False,
        headers=headers,
        json=request_body
    )

    response.raise_for_status()

    return response.json()["output"]["events"]["event"]


def events_by_severity(events, severity):
    return [
        event
        for event in events
        if event["severity"] == severity
    ]


def main():
    token = get_token()

    events = get_events(token)

    print("------------ Major Events ------------")

    for event in events_by_severity(events, "Major"):
        print(event)

    print("------------ Critical Events ------------")

    for event in events_by_severity(events, "Critical"):
        print(event)


if __name__ == "__main__":
    main()
"""
Output : 

------------ Major Events ------------

{
    'description': 'Operational status went down due to link failure',
    'event-identity': 'interface-oper-status-down-alarm',
    'object-name': 'device-01',
    'object-type': 'interface',
    'processed-timestamp': '2026-01-15T10:30:00.000Z',
    'raised-timestamp': '2026-01-15T10:29:59+00:00',
    'received-timestamp': '2026-01-15T10:29:59.900Z',
    'severity': 'Major',
    'source': 'device-01:interface-1',
    'timestamp': '2026/01/15 10:29:59AM+0000',
    'timestamp-iso': '2026-01-15T10:29:59+00:00'
}

{
    'description': 'Operational status went down due to link failure',
    'event-identity': 'interface-oper-status-down-alarm',
    'object-name': 'device-02',
    'object-type': 'interface',
    'processed-timestamp': '2026-01-15T10:25:00.000Z',
    'raised-timestamp': '2026-01-15T10:24:59+00:00',
    'received-timestamp': '2026-01-15T10:24:59.900Z',
    'severity': 'Major',
    'source': 'device-02:interface-2',
    'timestamp': '2026/01/15 10:24:59AM+0000',
    'timestamp-iso': '2026-01-15T10:24:59+00:00'
}

------------ Critical Events ------------

{
    'description': 'The transmit power has fallen below the configured alarm threshold',
    'event-identity': 'transmit-power-alarm',
    'object-name': 'device-03',
    'object-type': 'device',
    'processed-timestamp': '2026-01-15T09:45:00.000Z',
    'raised-timestamp': '2026-01-15T09:44:59+00:00',
    'received-timestamp': '2026-01-15T09:44:59.900Z',
    'severity': 'Critical',
    'source': 'device-03:interface-1',
    'timestamp': '2026/01/15 09:44:59AM+0000',
    'timestamp-iso': '2026-01-15T09:44:59+00:00'
}

"""
