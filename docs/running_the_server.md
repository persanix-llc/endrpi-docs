---
description: 
    Start Endrpi with optional command-line arguments such as port and host.
---

The Endrpi server accepts a few optional parameters such as port and host.
By default, Endrpi will run on port 5000 and be accessible by other devices on the LAN.


## Prerequisites

1. [Installation](installation.md)


## Optional arguments

`-p, --port`
:   Sets the port to start the server on.

`-h, --host`
:   Sets the host to start the server on.

##### Example

```
endrpi -p 6000 -h 0.0.0.0
```


--8<-- "docs/includes/abbreviations.md"
--8<-- "docs/includes/links.md"
