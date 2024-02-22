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
eval "$(pyenv init -)"
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

4. Run app

```
npm run pyhipster
```
