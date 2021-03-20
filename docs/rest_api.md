---
description: 
    Learn about Endrpi's fully documented, RESTful web API that can be used to read various system statuses 
    and control GPIO pin configurations on the Raspberry Pi®.   
---

!!! danger ":material-lightning-bolt: No authentication"
    The endpoints described below are **not authenticated**
    and should only be used on a secure, private LAN.  

!!! info ":material-information-outline: GPIO Mocking"
    GPIO interaction is mocked when Endrpi is run on non-rpi systems for the purpose of testing.

## Prerequisites

1. [Installation](installation.md)
2. [Running the server](running_the_server.md)

## Local documentation

While Endrpi is running, access interactive REST documentation by navigating to
[http://localhost:5000/docs :material-open-in-new:][localhost-port-docs]{target=_blank rel=noopener}.

## Examples

Example requests for server platform information.

=== "JavaScript"

    ```javascript
    // Using a built-in library
    fetch('http://localhost:5000/system/platform')
      .then(response => response.json())
      .then(data => console.log(data));

    // Using the axios library
    axios.get('http://localhost:5000/system/platform')
         .then(data => console.log(data));
    ```

=== "Python"

    ```python
    # Using a built-in library
    import urllib.request
    response = urllib.request.urlopen('http://localhost:5000/system/platform').read()
    print(response)

    # Using the requests library
    import requests
    response = requests.get('http://localhost:5000/system/platform')
    print(response.json())
    ```

=== "curl"

    ```
    curl http://localhost:5000/system/platform
    ```

--8<-- "docs/includes/abbreviations.md"
--8<-- "docs/includes/links.md"
