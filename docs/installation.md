Endrpi can be installed by downloading the source code from Github and then resolving its dependency tree using `pip`.

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
pip install -r requirements.txt
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
pip install -r requirements.txt
```

## Interactive API Documentation
The interactive API documentation can be installed by adding the latest Swagger UI build to the 
public directory.

##### 1. Download the latest release of Swagger UI

```
curl https://github.com/swagger-api/swagger-ui/archive/v3.44.1.tar.gz -o swagger-ui.tar.gz
```

##### 2. Un-tar the tarball

```
tar -xzf swagger-ui.tar.gz
```

##### 3. Copy the JavaScript bundle to Endrpi

```
cp -r swagger-ui-3.44.1/dist/swagger-ui-bundle.js endrpi-server/swagger-ui/
```

##### 3. Copy the CSS file to Endrpi

```
cp -r swagger-ui-3.44.1/dist/swagger-ui.css endrpi-server/swagger-ui/
```


--8<-- "docs/includes/abbreviations.md"
--8<-- "docs/includes/links.md"
