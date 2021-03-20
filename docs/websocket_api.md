---
description: 
    Learn about Endrpi's low-latency WebSocket endpoint that mirrors the REST API and
    can be used to read various system statuses on the Raspberry Pi®.
---

!!! danger ":material-lightning-bolt: No authentication"
    The endpoints described below are **not authenticated**
    and should only be used on a secure, private LAN.  

!!! info ":material-information-outline: GPIO Mocking"
    GPIO interaction is mocked when Endrpi is run on non-rpi systems for the purpose of testing.

## Prerequisites

1. [Installation](installation.md)
2. [Running the server](running_the_server.md)

## Overview

The WebSocket API provides clients with a low-latency, persistent connection to the Endrpi server.

Most of the WebSocket API requires a client to send a JSON message in order to receive a response.
The message the client sends must contain a specified action and, if required by the action, 
a set of parameters.

For example, sending the following message to the websocket:

```json
{
  "action": "GET_TEMPERATURE"
}
```

will return the following response:

```json
{
  "action": "GET_TEMPERATURE",
  "success": true,
  "data": {
    "systemOnChip": { 
      "quantity": 20.0,
      "prefix": null,
      "unitOfMeasurement": "CELSIUS"
    }
  },
  "error": null
}
```

Every WebSocket message that Endrpi sends to a client will contain a stable action identifier 
(i.e. `GET_TEMPERATURE` in the above example).
This way, a client can parse message content by looking at what action was performed to generate the message.

#### Active vs. Passive Actions

Most of the WebSocket API is based on the request/response pattern.
Clients request an action to be performed, such as "measure the system temperature", in which case Endrpi will
respond with a message containing the result of the action (i.e. the temperature).
These actions are considered *active*.

Conversely, a *passive* WebSocket action can send messages to clients at any time without any input.
Passive messages are not part of the WebSocket API yet.

#### Parameters

Some active WebSocket actions require additional parameters to be sent with the request message.
These parameters are placed in the `params` field of the outgoing message.

The following message specifies both an action and a set of parameters:

```json
{
  "action": "READ_PIN_CONFIGURATIONS",
  "params": {
    "pins": [ "GPIO17", "GPIO15" ]
  }
}
```

which will result in the following response:

```json
{
  "action": "READ_PIN_CONFIGURATIONS",
  "success": true,
  "data": {
    "GPIO17": {
      "io": "OUTPUT",
      "state": 1.0,
      "pull": "FLOATING"
    },
    "GPIO15": {
      "io": "OUTPUT",
      "state": 1.0,
      "pull": "FLOATING"
    }
  },
  "error": null
}
```

## Examples

=== "JavaScript"

    ```javascript
    // Open a new WebSocket connection (note the 'ws' protocol)
    const webSocket = new WebSocket('ws://localhost:5000');

    // Create a new message to send to the WebSocket
    const data = { 'action': 'READ_TEMPERATURE' };
    const message = JSON.stringify(data);

    // Send the message as soon as the websocket opens (for demonstration purposes)
    webSocket.onopen = (event) => webSocket.send(message);
    
    // When the websocket responds with a message, log it to console
    webSocket.onmessage = (response) => console.log(response);
    
    // Note: Don't forget to close the websocket when finished!
    // webSocket.close()
    ```

## Actions

The supported WebSocket actions are categorized by their REST counterpart.

##### System

| <div style="width:9rem">Action</div>  | Type    | Params  | Model       |
| ------------------------------------- | ------- | ------- | ----------- |
| `READ_TEMPERATURE`                    | Active  | (none)  | Temperature |
| `READ_THROTTLE`                       | Active  | (none)  | Throttle    |
| `READ_UPTIME`                         | Active  | (none)  | UpTime      |
| `READ_FREQUENCY`                      | Active  | (none)  | Frequency   |
| `READ_MEMORY`                         | Active  | (none)  | Memory      |

##### Pin configuration

| <div style="width:9rem">Action</div>  | Type    | <div style="width:5rem">Params</div> | Model               |
| ------------------------------------- | ------- | ------------------------------------ | ------------------- |
| `READ_PIN_CONFIGURATIONS`             | Active  | ReadPinConfigurationsParams          | PinConfigurationMap |
| `UPDATE_PIN_CONFIGURATIONS`           | Active  | UpdatePinConfigurationsParams        | string              |

## Responses

WebSocket responses will always be wrapped in the following data structure:

| Field     | Type             | Description                                           |
| --------- | ---------------- | ----------------------------------------------------- |
| `action`  | `string | null`  | The name of the action the response corresponds to    |
| `success` | `boolean`        | Whether the action was successful                     |
| `data`    | `<Model> | null` | The data model associated with the action             |
| `error`   | `string | null`  | Any error that occurred while performing the action   |

##### Example

```json
{
  "action": "GET_TEMPERATURE",
  "success": true,
  "data": {
    "systemOnChip": { 
      "quantity": 20.0,
      "prefix": null,
      "unitOfMeasurement": "CELSIUS"
    }
  },
  "error": null
}
```

--8<-- "docs/includes/abbreviations.md"
--8<-- "docs/includes/links.md"
