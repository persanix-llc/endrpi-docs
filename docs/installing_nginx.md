---
description: 
    Install Nginx® alongside Endrpi on a Raspberry Pi® to start proxying API requests,
    serving static content, and offloading TLS processes.
---

[Nginx :material-open-in-new:][nginx]{target=_blank rel=noopener}
is a powerful server that can be installed on a Raspberry Pi® and used as a reverse proxy for Endrpi.

## Installation

##### 1. Install system updates

```
sudo apt update
``` 

##### 2. Install Nginx

```
sudo apt-get nginx
``` 

## Verify Nginx is running

!!! info ":material-information-outline: Automatically Running"
    Nginx should start running automatically after the installation.

To verify Nginx is running, run the following command:

```
systemctl status nginx --no-pager
```

The output should contain the status <span class="text-green">● active (running)</span> with some additional
information.

Additionally, 
[http://localhost :material-open-in-new:][localhost]{target=_blank rel=noopener}
should now show the default Nginx HTML page.

--8<-- "docs/includes/abbreviations.md"
--8<-- "docs/includes/links.md"
