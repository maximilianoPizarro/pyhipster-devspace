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

<p align="left">
  <img src="https://github.com/maximilianoPizarro/pyhipster-devspace/blob/main/screenshot/pyhipster-terminal.PNG?raw=true" width="684" title="Run On Openshift">
</p>


1. Open terminal on Red Hat OpenShift Dev Spaces and run.

```
eval "$(pyenv init -)"
rm -r app && mkdir app
```

2. Copy jhipster-devspace-model.jdl to app directory.

```
cp template-jdl/pyhipster-devspace-model.jdl app
```


3. Run 'pyhipster jdl' command. info https://www.jhipster.tech/jdl/getting-started JDL Studio.

```
cd app
pyhipster jdl pyhipster-devspace-model.jdl
```

4. Modify line 51 in the app/webpack/webpack.common.js file. The key "proxy" http://localhost:8080 for http://127.0.0.1:8080.

```
      devServer: {
        static: {
          directory: './target/classes/static/',
        },
        port: 9060,
        proxy: [
          {
            context: ['/api', '/services', '/management', '/v3/api-docs', '/h2-console', '/auth'],
            target: 'http://127.0.0.1:8080',
```
        

5. Run pyhipster app. Confirm the link ports 8080 and 9000 from the VS Code message.

```
npm run pyhipster
```

<p align="left">
  <img src="https://github.com/maximilianoPizarro/pyhipster-devspace/blob/main/screenshot/pyhipster-terminal-run.PNG?raw=true" width="684" title="Run On Openshift">
</p>



## Deploy PyHipster v0.0.9 Monolithic application on ⭕ Red Hat OpenShift Pipelines ⭕
<p align="left">
  <img src="https://github.com/maximilianoPizarro/pyhipster-devspace/blob/main/screenshot/pyhipster-pipeline.PNG?raw=true" width="684" title="Run On Openshift">
</p>

From terminal on Red Hat Openshift Dev Spaces an Red Hat OpenShift

By default, the repo contains a version generated for testing this section with the name "Delivery", if you want to change it in your fork you will need to change it to the new value in the yaml objects and the jhispter JDL file.

1. Fork this repo and modify the yaml files with your environment keys, <NAMESPACE> value.

```bash
  k8s/overlay/develop/route.yaml <---
  spec:
    host: delivery-<NAMESPACE>.apps.sandbox-m2.ll9k.p1.openshiftapps.com
```
```
  k8s/overlay/develop/deployment-patches.yaml <---
    spec:
      containers:
      - name: delivery
        image: image-registry.openshift-image-registry.svc:5000/<NAMESPACE>/delivery        
```
```
  k8s/base/configmap.yaml <---
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://delivery:delivery@postgresql.<NAMESPACE>.svc.cluster.local:5432/delivery'
```


2. Create a Tekton Pipeline and PVC with oc apply command.

```bash
pyhipster-devspace (master) $ oc apply -f pipeline.yaml
```

```bash
Output
persistentvolumeclaim/workspace created
pipeline.tekton.dev/pyhipster-devspace created
```

3. Run a Pipeline pyhipster-devspace from Red Hat OpenShift Pipelines.

<p align="left">
  <img src="https://github.com/maximilianoPizarro/pyhipster-devspace/blob/main/screenshot/pyhipster-pipeline-form.PNG?raw=true" width="684" title="Run On Openshift">
</p>

<p align="left">
  <img src="https://github.com/maximilianoPizarro/pyhipster-devspace/blob/main/screenshot/pyhipster-pipeline-run.PNG?raw=true" width="684" title="Run On Openshift">
</p>

4. View Topology and logs java POD.

<p align="left">
  <img src="https://github.com/maximilianoPizarro/pyhipster-devspace/blob/main/screenshot/pyhipster-topology.PNG?raw=true" width="684" title="Run On Openshift">
</p>

<p align="left">
  <img src="https://github.com/maximilianoPizarro/pyhipster-devspace/blob/main/screenshot/pyhipster-logs.PNG?raw=true" width="684" title="Run On Openshift">
</p>

5. Check in your browser the app run in production mode.

<p align="left">
  <img src="https://github.com/maximilianoPizarro/pyhipster-devspace/blob/main/screenshot/pyhipster-pod-entities.PNG?raw=true" width="684" title="Run On Openshift">
</p>
<p align="left">
  <img src="https://github.com/maximilianoPizarro/pyhipster-devspace/blob/main/screenshot/pyhipster-pod-test.PNG?raw=true" width="684" title="Run On Openshift">
</p>
<p align="left">
  <img src="https://github.com/maximilianoPizarro/pyhipster-devspace/blob/main/screenshot/pyhipster-pod-configuration.PNG?raw=true" width="684" title="Run On Openshift">
</p>



## Example Output terminal Red Hat OpenShift Dev Spaces

Output build:
```
pyhipster-devspace (main) $ eval "$(pyenv init -)"
pyhipster-devspace (main) $ rm -r app && mkdir app
pyhipster-devspace (main) $ cp template-jdl/pyhipster-devspace-model.jdl app
pyhipster-devspace (main) $ cd app
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
warn: In the One-to-Many relationship from Country to Region, only bidirectionality is supported for a One-to-Many association. The other side will be automatically added.
warn: In the One-to-Many relationship from Location to Country, only bidirectionality is supported for a One-to-Many association. The other side will be automatically added.
warn: In the One-to-Many relationship from Department to Location, only bidirectionality is supported for a One-to-Many association. The other side will be automatically added.
warn: In the One-to-Many relationship from Employee to Job, only bidirectionality is supported for a One-to-Many association. The other side will be automatically added.
warn: In the One-to-Many relationship from Department to Employee, only bidirectionality is supported for a One-to-Many association. The other side will be automatically added.
warn: In the One-to-Many relationship from Employee to Employee, only bidirectionality is supported for a One-to-Many association. The other side will be automatically added.
warn: In the One-to-Many relationship from JobHistory to Job, only bidirectionality is supported for a One-to-Many association. The other side will be automatically added.
warn: In the One-to-Many relationship from JobHistory to Department, only bidirectionality is supported for a One-to-Many association. The other side will be automatically added.
warn: In the One-to-Many relationship from JobHistory to Employee, only bidirectionality is supported for a One-to-Many association. The other side will be automatically added.
INFO! Found entities: Region, Country, Location, Department, Task, Employee, Job, JobHistory.
INFO! The JDL has been successfully parsed
INFO! Generating 1 application.
Application files will be generated in folder: /projects/pyhipster-devspace/app
 _______________________________________________________________________________________________________________

     info Your Java version is: 17.0.3
     info Your Python version is: 3.10
     info Your Node version is: v18.16.1
     info Your Git version is: 2.39.3
This is an existing project, using the configuration from your .yo-rc.json file 
to re-generate the project...

     info Disabling hibernate cache for cache provider no

Found the .pyhipster/Region.json configuration file, entity can be automatically generated!


Found the .pyhipster/Country.json configuration file, entity can be automatically generated!


Found the .pyhipster/Location.json configuration file, entity can be automatically generated!


Found the .pyhipster/Department.json configuration file, entity can be automatically generated!


Found the .pyhipster/Task.json configuration file, entity can be automatically generated!


Found the .pyhipster/Employee.json configuration file, entity can be automatically generated!


Found the .pyhipster/Job.json configuration file, entity can be automatically generated!


Found the .pyhipster/JobHistory.json configuration file, entity can be automatically generated!

     info Creating changelog for entities Region,Country,Location,Department,Task,Employee,Job,JobHistory
   create .prettierrc
<---------more lines--------->
    force .yo-rc.json
     info Installing Python modules
Creating virtualenv delivery in /projects/pyhipster-devspace/app/.venv
Updating dependencies
Resolving dependencies...

Package operations: 64 installs, 0 updates, 0 removals

<---------more lines--------->

Writing lock file

Installing the current project: delivery (0.0.1)
If you find PyHipster useful consider sponsoring the project https://github.com/pyhipster/generator-pyhipster

Server application generated successfully.

Client application generated successfully.

Entity Region generated successfully.
Entity Country generated successfully.
Entity Location generated successfully.
Entity Department generated successfully.
Entity Task generated successfully.
Entity Employee generated successfully.
Entity Job generated successfully.
Entity JobHistory generated successfully.
INFO! Generator app succeed
Congratulations, PyHipster execution is complete!
Show us some ❤️  by sponsoring us.

```

Output runtime:
```
app (main) $ npm run pyhipster

> delivery@0.0.0 pyhipster
> concurrently "npm:start" npm:pyhipster:backend:start

[start] 
[start] > delivery@0.0.0 start
[start] > npm run webapp:dev --
[start] 
[pyhipster:backend:start] 
[pyhipster:backend:start] > delivery@0.0.0 pyhipster:backend:start
[pyhipster:backend:start] > poetry run task run_app
[pyhipster:backend:start] 
[start] 
[start] > delivery@0.0.0 webapp:dev
[start] > npm run webpack-dev-server -- --mode development --env stats=normal
[start] 
[start] 
[start] > delivery@0.0.0 webpack-dev-server
[start] > webpack serve --config webpack/webpack.common.js "--mode" "development" "--env" "stats=normal"
[start] 
[pyhipster:backend:start] /projects/pyhipster-devspace/app/.venv/lib/python3.10/site-packages/flask_sqlalchemy/__init__.py:851: UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".
[pyhipster:backend:start]   warnings.warn(
[pyhipster:backend:start]  * Serving Flask app 'DeliveryApp' (lazy loading)
[pyhipster:backend:start]  * Environment: development
[pyhipster:backend:start]  * Debug mode: on
[pyhipster:backend:start] 22-Feb-24 12:33:01 -  * Running on http://127.0.0.1:8080 (Press CTRL+C to quit)
[pyhipster:backend:start] 22-Feb-24 12:33:01 -  * Restarting with stat
[start] <i> [webpack-dev-server] [HPM] Proxy created: /api,/services,/management,/v3/api-docs,/h2-console,/auth  -> http://127.0.0.1:8080
[start] <i> [webpack-dev-server] Project is running at:
[start] <i> [webpack-dev-server] Loopback: http://localhost:9060/
[start] <i> [webpack-dev-server] On Your Network (IPv4): http://10.131.10.155:9060/
[start] <i> [webpack-dev-server] Content not from webpack is served from './target/classes/static/' directory
[start] <i> [webpack-dev-server] 404s will fallback to '/index.html'
[pyhipster:backend:start] /projects/pyhipster-devspace/app/.venv/lib/python3.10/site-packages/flask_sqlalchemy/__init__.py:851: UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".
[pyhipster:backend:start]   warnings.warn(
[pyhipster:backend:start] 22-Feb-24 12:33:02 -  * Debugger is active!
[pyhipster:backend:start] 22-Feb-24 12:33:02 -  * Debugger PIN: 936-708-888
[start] assets by path *.js 5.01 MiB
[start]   assets by chunk 62.9 KiB (id hint: vendors) 2 assets
[start]   + 42 assets
[start] assets by path content/ 452 KiB 26 assets
[start] assets by path swagger-ui/ 3.25 MiB 16 assets
[start] assets by path ./i18n/*.json 50 KiB
[start]   asset ./i18n/es.json 17.4 KiB [emitted]
[start]   + 2 assets
[start] assets by info 20 KiB [immutable]
[start]   asset c0285e5e9ebdce9056be.svg 11.9 KiB [emitted] [immutable] [from: src/main/webapp/content/images/jhipster_family_member_0.svg] (auxiliary name: app)
[start]   asset e7c5d1f3c54c658850f0.png 8.09 KiB [emitted] [immutable] [from: src/main/webapp/content/images/logo-pyhipster.png] (auxiliary name: app)
[start] asset favicon.ico 16.6 KiB [emitted] [from: src/main/webapp/favicon.ico] [copied]
[start] asset index.html 5.75 KiB [emitted]
[start] asset manifest.webapp 751 bytes [emitted] [from: src/main/webapp/manifest.webapp] [copied]
[start] asset robots.txt 216 bytes [emitted] [from: src/main/webapp/robots.txt] [copied]
[start] cached modules 4.71 MiB (javascript) 20 KiB (asset) 30.7 KiB (runtime) [cached] 804 modules
[start] webpack 5.88.2 compiled successfully in 1687 ms
[start] [Browsersync] Proxying: http://localhost:9060
[start] [Browsersync] Access URLs:
[start]  --------------------------------------
[start]        Local: http://localhost:9000
[start]     External: http://10.131.10.155:9000
[start]  --------------------------------------
[start]           UI: http://localhost:3001
[start]  UI External: http://localhost:3001
[start]  --------------------------------------
```
