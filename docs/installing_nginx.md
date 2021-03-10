[Nginx :material-open-in-new:][nginx]{target=_blank rel=noopener}
is a powerful server that can be used as a reverse proxy for Endrpi.

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

!!! info "Automatically Running"
    Nginx should start running automatically after the installation.

To verify Nginx is running, run the following command:

```
systemctl status nginx --no-pager
```

The output should contain the status <span style="color: #00c853">● active (running)</span> with some additional
information.

Additionally, 
[http://localhost :material-open-in-new:][localhost]{target=_blank rel=noopener}
should now show the default Nginx HTML page.

--8<-- "docs/includes/abbreviations.md"
--8<-- "docs/includes/links.md"
