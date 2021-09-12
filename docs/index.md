---
description: 
    Endpoints for Raspberry Pi® (Endrpi) is a web API server for the Raspberry Pi® that provides basic
    statuses and GPIO controls through a collection of REST and Websocket HTTP endpoints.
---

![Endrpi logo](https://assets.persanix.com/endrpi/logo-padded/logo-padded.svg)

# Welcome to the Endrpi Docs

Endpoints for Raspberry Pi® (Endrpi) is a web API server for the 
[Raspberry Pi® :material-open-in-new:][raspberry-pi-org]{target=_blank rel=noopener}
that provides basic statuses and GPIO controls through a collection of HTTP endpoints.

Powered by 
[Fast API :material-open-in-new:][fast-api-github]{target=_blank rel=noopener}, 
[GPIO Zero :material-open-in-new:][gpio-zero-github]{target=_blank rel=noopener}, 
and 
[others :material-open-in-new:][endrpi-server-github-requirements]{target=_blank rel=noopener}.


## Features

#### REST API
* Reads system statuses such as temperature, memory usage, throttling, etc.
* Reads and updates GPIO pin state, function, and pull.
* Generates interactive API documentation via 
  [Swagger UI :material-open-in-new:][swagger-ui]{target=_blank rel=noopener}.

#### Websocket
* Supports a persistent, low-latency WebSocket connection.
* Mirrors the REST API through a request/response pattern.


## Requirements

* :material-greater-than-or-equal: Python 3.7
* :material-greater-than-or-equal: Raspberry Pi® 3
    * Compatible with the standard
      [Raspberry Pi® OS :material-open-in-new:][raspberry-pi-org-raspbian]{target=_blank rel=noopener}
      image
    * Previous Raspberry Pi® versions may work but have not been verified


## Quickstart

```
pip3 install -U endrpi && endrpi
```

Endrpi will start running on port 5000; for a list of run options see [Running the Server](running_the_server.md).


## Example Request

The following request returns the temperature of the Raspberry Pi® System on Chip.

###### Request
```
GET http://localhost:5000/system/temperature
```

###### Response
```json
{
  "systemOnChip": {
      "quantity": 45.622,
      "prefix": null,
      "unitOfMeasurement": "CELSIUS"
  }
}
```

Endrpi generates live, interactive API documentation. 
A complete list of REST endpoints can be found hosted at
[localhost:5000/docs][localhost-port-docs]{target=_blank rel=noopener}.


## License

Licensed under the Apache License, Version 2.0.

Copyright &copy; 2020 - 2021 Persanix LLC. All rights reserved.


## Disclaimers

BY CLICKING ON THE GITHUB LINK ABOVE YOU AGREE TO OUR 
[WEBSITE DISCLAIMERS :material-open-in-new:][persanix-disclaimers]{target=_blank rel=noopener}
ON YOUR OWN BEHALF AND ON BEHALF OF ALL PERSONS IN YOUR ORGANIZATION WHO MAY USE THE PERSANIX™ APPLICATION.
YOU REPRESENT AND WARRANT THAT YOU HAVE FULL AUTHORITY TO BIND THE ENTITY THAT YOU WORK FOR AND YOURSELF TO 
THESE DISCLAIMERS. 
IF YOU DO NOT AGREE TO THESE DISCLAIMERS AND DO NOT HAVE THE AUTHORITY AS PROVIDED HEREIN, DO NOT ACCESS, OR USE THE PERSANIX™ APPLICATION.


[interactive-docs-installation]: /installation/#interactive-api-documentation

--8<-- "docs/includes/abbreviations.md"
--8<-- "docs/includes/links.md"
