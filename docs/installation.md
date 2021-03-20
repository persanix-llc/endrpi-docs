---
description: 
    Start using Endrpi by downloading the Endrpi source code to a Raspberry Pi®, 
    installing Python dependencies with pip, and adding a Swagger UI build.
---

Endrpi can be installed to a Raspberry Pi® by downloading the source code from Github® 
and then resolving its dependency tree using `pip`.

Interactive API documentation can be enabled by downloading a Swagger UI build.

## Endrpi Source Code

### :fontawesome-brands-git-alt: Option One: Git clone

##### 1. Clone the main branch of Endrpi

```
git clone https://github.com/persanix-llc/endrpi-server.git
``` 

##### 2. Change directory to the Endrpi root

```
cd endrpi-server
``` 

##### 3. Install dependencies

```
pip3 install -r requirements.txt
```

### :fontawesome-regular-file-archive: Option Two: Tarball

##### 1. Download the tarball using curl

```
curl https://github.com/persanix-llc/endrpi-server/main.tar.gz -o endrpi-server.tar.gz
```

##### 2. Un-tar the tarball

```
tar -xzf endrpi-server.tar.gz
```

##### 3. Change directory to the endrpi root

```
cd endrpi-server
``` 
##### 4. Install dependencies

```
pip3 install -r requirements.txt
```

## Interactive API Documentation
The interactive API documentation can be installed by adding the latest Swagger UI build to the 
public directory.

The following commands should be run **outside** the endrpi-server directory, preferably in the home path.

##### 1. Download the latest release of Swagger UI

```
curl -L https://github.com/swagger-api/swagger-ui/tarball/v3.44.1 -o swagger-ui.tar.gz
```

##### 2. Create swagger-ui directories

```
mkdir swagger-ui && mkdir endrpi-server/public/swagger-ui
```

##### 3. Un-tar the tarball

```
tar -xzf swagger-ui.tar.gz -C ./swagger-ui --strip-components=1
```

##### 4. Copy the JavaScript bundle to Endrpi

```
cp -r swagger-ui/dist/swagger-ui-bundle.js endrpi-server/public/swagger-ui/
```

##### 5. Copy the CSS file to Endrpi

```
cp -r swagger-ui/dist/swagger-ui.css endrpi-server/public/swagger-ui/
```


--8<-- "docs/includes/abbreviations.md"
--8<-- "docs/includes/links.md"
