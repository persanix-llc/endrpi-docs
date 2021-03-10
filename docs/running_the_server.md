The Endrpi server can be started by running the Python script `endr.py`.

## Prerequisites

1. [Installation](installation.md)

## Default configuration

The Endrpi server will run without any configuration on localhost port 5000.

##### 1. Change directory to the endrpi root

```
cd endrpi-server
```

##### 2. Run the server

```
python endr.py
```

##### 3. Navigate to the test page

[http://localhost:5000 :material-open-in-new:][localhost-port]{target=_blank rel=noopener}

## Interactive API Docs

API documentation is generated locally when Endrpi starts and will be hosted 
at [http://localhost:5000/docs :material-open-in-new:][localhost-port-docs]{target=_blank rel=noopener}.

The API documentation is usually reachable by other devices on the same LAN as the Raspberry Pi.
Run the command ```ifconfig``` on the Raspberry Pi and use the resulting IP address as the hostname to 
view the documentation on another computer.

## Optional arguments

`-p, --port`
:   Sets the port to start the server on.

`-h, --host`
:   Sets the host to start the server on.

##### Example

```
python endr.py -p 6000 -h 0.0.0.0
```

--8<-- "docs/includes/abbreviations.md"
--8<-- "docs/includes/links.md"