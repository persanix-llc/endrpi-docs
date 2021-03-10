!!! warning "Changing Defaults"
    This configuration will proxy **all** HTTP requests for localhost port 80 to Endrpi.

## Overview

Nginx can be used as a reverse proxy for Endrpi which provides the following functionality:

* Proxy requests to Endrpi from port 80.
* Serve static content, such as websites, from a directory.
* Route API requests from clients to the Endrpi server.

## Prerequisites

1. [Installing Nginx](installing_nginx.md)

## Configuration

##### 1. Unlink the default Nginx website

```
sudo unlink /etc/nginx/sites-enabled/default
``` 

##### 2. Copy the default configuration

```
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/endrpi
``` 

##### 3. Open the Endrpi configuration for editing

```
sudo nano /etc/nginx/sites-available/endrpi
``` 

##### 4. Change the root location to be used as a proxy pass-through

```
location / {
   proxy_pass http://localhost:5000;
}
``` 

##### 5. Save changes

++ctrl+o++

##### 6. Restart Nginx

```
sudo systemctl restart nginx
```

Requests will now be passed through the proxy:
[http://localhost/docs :material-open-in-new:][localhost-docs]{target=_blank rel=noopener}.

## References

1. [Setting up an NGINX web server on a Raspberry Pi :material-open-in-new:][1]{target=_blank rel=noopener}
    <br>
    raspberrypi.org
    [Last accessed 03/07/2021]

[1]: https://www.raspberrypi.org/documentation/remote-access/web-server/nginx.md

--8<-- "docs/includes/abbreviations.md"
--8<-- "docs/includes/links.md"
