# pyhipster-devspace


## Re-generate JHipster application from JDL File on Red Hat OpenShift Dev Spaces

1. Open terminal on Red Hat OpenShift Dev Spaces and run.

jhipster-devspace (master) $ rm -r app && mkdir app

```
rm -r app && mkdir app
```

1. Copy jhipster-devspace-model.jdl to app directory.

```
cp template-jdl/pyhipster-devspace-model.jdl app
```

2. Run 'pyhipster jdl' command. info https://www.jhipster.tech/jdl/getting-started JDL Studio.

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
```


3. Run app

```
npm run pyhipster
```