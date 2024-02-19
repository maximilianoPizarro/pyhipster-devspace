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

3. Run app

```
npm run pyhipster
```