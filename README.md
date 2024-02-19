# PyHipster v0.0.9 Monolithic application on Red Hat OpenShift Dev Spaces

<p align="left">
<img src="https://img.shields.io/badge/python-306998?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">     
<img src="https://img.shields.io/badge/nodejs-68a063?style=for-the-badge&logo=javascript&logoColor=white" alt="nodejs">
<img src="https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D" alt="VueJS">
<img src="https://img.shields.io/badge/redhat-CC0000?style=for-the-badge&logo=redhat&logoColor=white" alt="Redhat">
<img src="https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white" alt="kubernetes">
<img src="https://img.shields.io/badge/docker-0db7ed?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white" alt="shell">
<a href="https://www.linkedin.com/in/maximiliano-gregorio-pizarro-consultor-it"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="linkedin">     
</p>


<p align="left">
  <img src="https://github.com/maximilianoPizarro/pyhipster-devspace/blob/main/screenshot/pyhipster-devspace.PNG?raw=true" width="684" title="Run On Openshift">
</p>
<p align="left">
    <img src="https://github.com/maximilianoPizarro/pyhipster-devspace/blob/main/screenshot/pyhipster-devspace-app.PNG?raw=true" width="684" title="Run On Openshift">
</p>

## Install JHipster DevSpace on OpenShift Dev Spaces

1. Login with your Red Hat Account. https://console.redhat.com/openshift/sandbox. Select "OpenShift Dev Spaces".

<p align="left">
  <img src="https://github.com/maximilianoPizarro/jhipster-devspace/blob/master/screenshot/redhat-console.PNG?raw=true" width="684" title="Run On Openshift">
</p>

2. Fork this repo and complete Git Repo URL parameter with your repo info.

<p align="left">
  <img src="https://github.com/maximilianoPizarro/pyhipster-devspace/blob/main/screenshot/install-pyhipster-devspace.PNG?raw=true" width="684" title="Run On Openshift">
</p>



## Re-generate JHipster application from JDL File on Red Hat OpenShift Dev Spaces

1. Open terminal on Red Hat OpenShift Dev Spaces and run.

jhipster-devspace (master) $ rm -r app && mkdir app

```
rm -r app && mkdir app
```

2. Copy jhipster-devspace-model.jdl to app directory.

```
cp template-jdl/pyhipster-devspace-model.jdl app
```

3. Run 'pyhipster jdl' command. info https://www.jhipster.tech/jdl/getting-started JDL Studio.

jhipster-devspace (master) $cd app && jhipster jdl jhipster-devspace-model.jdl

```
cd app
pyhipster jdl pyhipster-devspace-model.jdl
```

```
Output
app (main) $ pyhipster jdl pyhipster-devspace-model.jdl
INFO! Using bundled PyHipster


██████╗░██╗░░░██╗██╗░░██╗██╗██████╗░░██████╗████████╗███████╗██████╗░
██╔══██╗╚██╗░██╔╝██║░░██║██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██████╔╝░╚████╔╝░███████║██║██████╔╝╚█████╗░░░░██║░░░█████╗░░██████╔╝
██╔═══╝░░░╚██╔╝░░██╔══██║██║██╔═══╝░░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗
██║░░░░░░░░██║░░░██║░░██║██║██║░░░░░██████╔╝░░░██║░░░███████╗██║░░██║
╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
Welcome to PyHipster v0.0.9

INFO! Executing import-jdl pyhipster-devspace-model.jdl
INFO! The JDL is being parsed.
warn: In the One-to-Many relationship from Cliente to User, only bidirectionality is supported for a One-to-Many association. The other side will be automatically added.
warn: In the One-to-Many relationship from ProductoOrden to Producto, only bidirectionality is supported for a One-to-Many association. The other side will be automatically added.
warn: An Entity name 'User' was used: 'User' is an entity created by default by JHipster. All relationships toward it will be kept but any attributes and relationships from it will be disregarded.
INFO! Found entities: Producto, ProductoCategoria, Cliente, Carrito, ProductoOrden.
INFO! The JDL has been successfully parsed
INFO! Generating 1 application.
Application files will be generated in folder: /projects/pyhipster-devspace/app
 _______________________________________________________________________________________________________________

     info Your Java version is: 17.0.3
     info Your Python version is: 3.11
     info Your Node version is: v18.16.1
     info Your Git version is: 2.39.3
This is an existing project, using the configuration from your .yo-rc.json file 
to re-generate the project...

     info Disabling hibernate cache for cache provider no

Found the .pyhipster/Producto.json configuration file, entity can be automatically generated!


Found the .pyhipster/ProductoCategoria.json configuration file, entity can be automatically generated!


Found the .pyhipster/Cliente.json configuration file, entity can be automatically generated!


Found the .pyhipster/Carrito.json configuration file, entity can be automatically generated!


Found the .pyhipster/ProductoOrden.json configuration file, entity can be automatically generated!
...more lines...

If you find PyHipster useful consider sponsoring the project https://github.com/pyhipster/generator-pyhipster

Server application generated successfully.


Client application generated successfully.

Entity Producto generated successfully.
Entity ProductoCategoria generated successfully.
Entity Cliente generated successfully.
Entity Carrito generated successfully.
Entity ProductoOrden generated successfully.
INFO! Generator app succeed
Congratulations, PyHipster execution is complete!
Show us some ❤️  by sponsoring us.
```


4. Skip process when step install "typing-extensions" or pandas and update pyproject.toml file.

```
app/pyproject.toml
pandas = "*"
typing-extensions = "*"
```

Re run pyhipster jdl command and skip pyproject.toml file

```
 conflict pyproject.toml
? Overwrite pyproject.toml? do not overwrite
     skip pyproject.toml
```

6. Run npm install command

```
npm install
```

6. Run app

```
npm run pyhipster
```