---
description: 
    Start using Endrpi by installing a pip package or downloading the Endrpi source. 
---

Endrpi can be installed by installing the `endrpi` package or by downloading the source code from Github®.

For more information about running Endrpi, see [Running the Server](running_the_server.md).


## :fontawesome-brands-python: Pip

Endrpi is available as a `pip` package which provides the `endrpi` command.

##### 1. Install the endrpi package

```
pip3 install -U endrpi
```

##### 2. Run the endrpi command

```
endrpi
```


## :fontawesome-solid-code: Source Code

Endrpi can be installed and run directly from source code.

#### :fontawesome-brands-git-alt: Option One: Git clone

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

##### 4. Run the server

```
python3 endrpi/cli.py
```


#### :fontawesome-regular-file-archive: Option Two: Tarball

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

##### 5. Run the server

```
python3 endrpi/cli.py
```


--8<-- "docs/includes/abbreviations.md"
--8<-- "docs/includes/links.md"
