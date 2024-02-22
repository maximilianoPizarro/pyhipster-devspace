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
   create .prettierignore
   create package.json
    force .yo-rc.json
   create .pyhipster/Region.json
   create .pyhipster/Employee.json
   create .pyhipster/Country.json
   create .pyhipster/Job.json
   create .pyhipster/JobHistory.json
   create .pyhipster/Location.json
   create .pyhipster/Department.json
   create .pyhipster/Task.json
   create .gitattributes
   create .editorconfig
   create .gitignore
   create src/main/resources/banner.txt
   create src/main/resources/config/liquibase/changelog/00000000000000_initial_schema.xml
   create src/main/resources/config/liquibase/master.xml
   create src/main/docker/jib/entrypoint.sh
   create .devcontainer/Dockerfile
   create pyproject.toml
   create poetry.toml
   create src/main/resources/i18n/messages.properties
   create src/main/python/security/AuthoritiesConstants.py
   create src/main/python/security/SecurityUtils.py
   create src/main/python/rest/UserJWTController.py
   create .devcontainer/devcontainer.json
   create src/main/python/rest/__init__.py
   create src/main/python/DeliveryApp.py
   create src/main/python/WebSerializer.py
   create src/main/docker/app.yml
   create src/main/python/DatabaseConfig.py
   create src/main/docker/jhipster-control-center.yml
   create src/main/python/MailConfiguration.py
   create src/main/python/__init__.py
   create src/main/docker/sonar.yml
   create src/main/python/security/__init__.py
   create src/main/docker/monitoring.yml
   create src/main/docker/postgresql.yml
   create src/main/python/config/BaseConfig.py
   create src/main/docker/prometheus/prometheus.yml
   create src/main/resources/templates/error.html
   create src/main/python/config/FakeDataLoader.py
   create src/main/docker/grafana/provisioning/dashboards/dashboard.yml
   create src/main/python/config/__init__.py
   create src/main/python/domain/AbstractAuditingEntity.py
   create src/main/python/schema/__init__.py
   create src/main/docker/grafana/provisioning/dashboards/JVM.json
   create src/main/python/schema/UserSchema.py
   create src/main/resources/config/application-tls.yml
   create src/main/python/schema/Authority.py
   create src/main/docker/grafana/provisioning/datasources/datasource.yml
   create src/main/python/rest/AuthorityResource.py
   create src/test/python/conftest.py
   create src/main/python/domain/User.py
   create src/test/python/unit_tests/Test_User.py
   create src/main/python/domain/Authority.py
   create src/test/python/unit_tests/Test_Authority.py
   create src/test/python/functional_tests/Test_UserJWTController.py
   create src/main/python/domain/__init__.py
   create src/main/python/rest/AccountResource.py
   create src/main/python/rest/UserResource.py
   create src/main/python/rest/PublicUserResource.py
   create src/main/python/rest/LogoutResource.py
   create src/main/resources/config/liquibase/data/user.csv
   create src/main/resources/config/liquibase/data/authority.csv
   create src/main/resources/config/liquibase/data/user_authority.csv
   create src/main/python/rest/AppManagment.py
   create src/test/resources/config/application-testcontainers.yml
   create src/test/python/functional_tests/Test_PublicUserResource.py
   create src/test/python/functional_tests/Test_UserResource.py
   create src/main/resources/templates/mail/activationEmail.html
   create src/test/python/functional_tests/Test_AuthorityResource.py
   create src/main/resources/templates/mail/creationEmail.html
   create src/test/python/functional_tests/Test_AccountResource.py
   create src/main/resources/templates/mail/passwordResetEmail.html
   create webpack/logo-jhipster.png
   create webpack/logo-pyhipster.png
   create tsconfig.json
   create tsconfig.app.json
   create tsconfig.spec.json
   create jest.conf.js
   create .eslintrc.json
   create angular.json
   create ngsw-config.json
   create .browserslistrc
   create webpack/environment.js
   create webpack/proxy.conf.js
   create webpack/webpack.custom.js
   create src/main/webapp/main.ts
   create src/main/webapp/bootstrap.ts
   create src/main/webapp/polyfills.ts
   create src/main/webapp/declarations.d.ts
   create src/main/webapp/content/scss/_bootstrap-variables.scss
   create src/main/webapp/content/scss/global.scss
   create src/main/webapp/app/app.module.ts
   create src/main/webapp/content/scss/vendor.scss
   create src/main/webapp/app/app-routing.module.ts
   create src/main/webapp/app/app.constants.ts
   create src/main/webapp/app/entities/entity-navbar-items.ts
   create src/main/webapp/app/entities/entity-routing.module.ts
   create src/main/webapp/app/home/home.module.ts
   create src/main/webapp/app/home/home.route.ts
   create src/main/webapp/app/home/home.component.ts
   create src/main/webapp/app/home/home.component.html
   create src/main/webapp/app/layouts/profiles/page-ribbon.component.ts
   create src/main/webapp/app/layouts/error/error.component.ts
   create src/main/webapp/app/home/home.component.scss
   create src/main/webapp/app/layouts/profiles/profile.service.ts
   create src/main/webapp/app/layouts/profiles/profile-info.model.ts
   create src/main/webapp/app/layouts/error/error.component.html
   create src/main/webapp/app/layouts/main/main.component.ts
   create src/main/webapp/app/layouts/main/main.component.html
   create src/main/webapp/app/login/login.service.ts
   create src/main/webapp/app/login/login.component.html
   create src/main/webapp/app/layouts/navbar/navbar.component.ts
   create src/main/webapp/app/login/login.model.ts
   create src/main/webapp/app/layouts/navbar/navbar.component.html
   create src/main/webapp/app/layouts/navbar/active-menu.directive.ts
   create src/main/webapp/app/layouts/navbar/navbar.route.ts
   create src/main/webapp/app/layouts/footer/footer.component.ts
   create src/main/webapp/app/layouts/profiles/page-ribbon.component.scss
   create src/main/webapp/app/layouts/footer/footer.component.html
   create src/main/webapp/app/layouts/error/error.route.ts
   create src/main/webapp/app/layouts/navbar/navbar.component.scss
   create src/main/webapp/app/login/login.module.ts
   create src/main/webapp/app/login/login.route.ts
   create src/main/webapp/app/login/login.component.ts
   create src/main/webapp/app/account/account.route.ts
   create src/main/webapp/app/account/account.module.ts
   create src/main/webapp/app/account/activate/activate.route.ts
   create src/main/webapp/app/account/activate/activate.component.ts
   create src/main/webapp/app/account/activate/activate.component.html
   create src/main/webapp/app/account/activate/activate.service.ts
   create src/main/webapp/app/account/password/password.route.ts
   create src/main/webapp/app/account/password/password-strength-bar/password-strength-bar.component.ts
   create src/main/webapp/app/account/password/password-strength-bar/password-strength-bar.component.html
   create src/main/webapp/app/account/password/password-strength-bar/password-strength-bar.component.scss
   create src/main/webapp/app/account/password/password.component.ts
   create src/main/webapp/app/account/password/password.component.html
   create src/main/webapp/app/account/password/password.service.ts
   create src/main/webapp/app/account/register/register.route.ts
   create src/main/webapp/app/account/register/register.component.ts
   create src/main/webapp/app/account/register/register.component.html
   create src/main/webapp/app/account/register/register.service.ts
   create src/main/webapp/app/account/register/register.model.ts
   create src/main/webapp/app/account/settings/settings.route.ts
   create src/main/webapp/app/account/settings/settings.component.ts
   create src/main/webapp/app/account/password-reset/init/password-reset-init.route.ts
   create src/main/webapp/app/account/settings/settings.component.html
   create src/main/webapp/app/account/password-reset/init/password-reset-init.component.ts
   create src/main/webapp/app/admin/admin-routing.module.ts
   create src/main/webapp/app/account/password-reset/init/password-reset-init.component.html
   create src/main/webapp/app/account/password-reset/init/password-reset-init.service.ts
   create src/main/webapp/app/admin/docs/docs.route.ts
   create src/main/webapp/app/account/password-reset/finish/password-reset-finish.route.ts
   create src/main/webapp/app/admin/docs/docs.module.ts
   create src/main/webapp/app/account/password-reset/finish/password-reset-finish.component.ts
   create src/main/webapp/app/admin/docs/docs.component.ts
   create src/main/webapp/app/account/password-reset/finish/password-reset-finish.component.html
   create src/main/webapp/app/admin/docs/docs.component.html
   create src/main/webapp/app/account/password-reset/finish/password-reset-finish.service.ts
   create src/main/webapp/app/admin/docs/docs.component.scss
   create src/main/webapp/app/admin/configuration/configuration.route.ts
   create src/main/webapp/app/admin/configuration/configuration.module.ts
   create src/main/webapp/app/admin/configuration/configuration.component.ts
   create src/main/webapp/app/admin/configuration/configuration.component.html
   create src/main/webapp/app/admin/configuration/configuration.service.ts
   create src/main/webapp/app/admin/configuration/configuration.model.ts
   create src/main/webapp/app/admin/health/health.route.ts
   create src/main/webapp/app/admin/health/health.module.ts
   create src/main/webapp/app/admin/health/health.component.ts
   create src/main/webapp/app/admin/health/health.component.html
   create src/main/webapp/app/admin/health/modal/health-modal.component.ts
   create src/main/webapp/app/admin/health/modal/health-modal.component.html
   create src/main/webapp/app/admin/health/health.service.ts
   create src/main/webapp/app/admin/health/health.model.ts
   create src/main/webapp/app/admin/logs/logs.route.ts
   create src/main/webapp/app/admin/logs/logs.module.ts
   create src/main/webapp/app/admin/logs/log.model.ts
   create src/main/webapp/app/admin/logs/logs.component.ts
   create src/main/webapp/app/admin/logs/logs.component.html
   create src/main/webapp/app/admin/logs/logs.service.ts
   create src/main/webapp/app/admin/metrics/metrics.route.ts
   create src/main/webapp/app/admin/metrics/metrics.module.ts
   create src/main/webapp/app/admin/metrics/metrics.component.ts
   create src/main/webapp/app/admin/metrics/metrics.component.html
   create src/main/webapp/app/admin/metrics/metrics.service.ts
   create src/main/webapp/app/admin/metrics/metrics.model.ts
   create src/main/webapp/app/admin/metrics/blocks/jvm-memory/jvm-memory.component.ts
   create src/main/webapp/app/admin/metrics/blocks/metrics-garbagecollector/metrics-garbagecollector.component.html
   create src/main/webapp/app/admin/metrics/blocks/jvm-memory/jvm-memory.component.html
   create src/main/webapp/app/admin/metrics/blocks/jvm-threads/jvm-threads.component.ts
   create src/main/webapp/app/admin/metrics/blocks/metrics-modal-threads/metrics-modal-threads.component.ts
   create src/main/webapp/app/admin/metrics/blocks/jvm-threads/jvm-threads.component.html
   create src/main/webapp/app/admin/metrics/blocks/metrics-modal-threads/metrics-modal-threads.component.html
   create src/main/webapp/app/admin/metrics/blocks/metrics-cache/metrics-cache.component.ts
   create src/main/webapp/app/admin/metrics/blocks/metrics-cache/metrics-cache.component.html
   create src/main/webapp/app/admin/metrics/blocks/metrics-request/metrics-request.component.ts
   create src/main/webapp/app/admin/metrics/blocks/metrics-datasource/metrics-datasource.component.ts
   create src/main/webapp/app/admin/metrics/blocks/metrics-request/metrics-request.component.html
   create src/main/webapp/app/admin/metrics/blocks/metrics-datasource/metrics-datasource.component.html
   create src/main/webapp/app/admin/metrics/blocks/metrics-endpoints-requests/metrics-endpoints-requests.component.ts
   create src/main/webapp/app/admin/metrics/blocks/metrics-system/metrics-system.component.ts
   create src/main/webapp/app/admin/metrics/blocks/metrics-endpoints-requests/metrics-endpoints-requests.component.html
   create src/main/webapp/app/admin/metrics/blocks/metrics-system/metrics-system.component.html
   create src/main/webapp/app/admin/metrics/blocks/metrics-garbagecollector/metrics-garbagecollector.component.ts
   create src/main/webapp/app/admin/user-management/user-management.route.ts
   create src/main/webapp/app/admin/user-management/user-management.module.ts
   create src/main/webapp/app/admin/user-management/user-management.model.ts
   create src/main/webapp/app/admin/user-management/list/user-management.component.ts
   create src/main/webapp/app/admin/user-management/list/user-management.component.html
   create src/main/webapp/app/admin/user-management/detail/user-management-detail.component.ts
   create src/main/webapp/app/admin/user-management/detail/user-management-detail.component.html
   create src/main/webapp/app/admin/user-management/update/user-management-update.component.ts
   create src/main/webapp/app/admin/user-management/update/user-management-update.component.html
   create src/main/webapp/app/admin/user-management/delete/user-management-delete-dialog.component.ts
   create src/main/webapp/app/admin/user-management/delete/user-management-delete-dialog.component.html
   create src/main/webapp/app/admin/user-management/service/user-management.service.ts
   create src/main/webapp/app/config/uib-pagination.config.ts
   create src/main/webapp/app/config/pagination.constants.ts
   create src/main/webapp/app/config/dayjs.ts
   create src/main/webapp/app/config/authority.constants.ts
   create src/main/webapp/app/config/datepicker-adapter.ts
   create src/main/webapp/app/core/config/application-config.service.ts
   create src/main/webapp/app/config/font-awesome-icons.ts
   create src/main/webapp/app/core/config/application-config.service.spec.ts
   create src/main/webapp/app/core/util/data-util.service.ts
   create src/main/webapp/app/config/error.constants.ts
   create src/main/webapp/app/core/util/parse-links.service.ts
   create src/main/webapp/app/core/util/alert.service.ts
   create src/main/webapp/app/core/util/event-manager.service.ts
   create src/main/webapp/app/config/input.constants.ts
   create src/main/webapp/app/core/util/operators.spec.ts
   create src/main/webapp/app/core/util/operators.ts
   create src/main/webapp/app/core/interceptor/error-handler.interceptor.ts
   create src/main/webapp/app/config/language.constants.ts
   create src/main/webapp/app/core/interceptor/notification.interceptor.ts
   create src/main/webapp/app/config/translation.config.ts
   create src/main/webapp/app/core/interceptor/auth-expired.interceptor.ts
   create src/main/webapp/app/core/interceptor/index.ts
   create src/main/webapp/app/core/request/request-util.ts
   create src/main/webapp/app/core/request/request.model.ts
   create src/main/webapp/app/core/interceptor/auth.interceptor.ts
   create src/main/webapp/app/entities/user/user.service.ts
   create src/main/webapp/app/entities/user/user.service.spec.ts
   create src/main/webapp/app/entities/user/user.model.ts
   create src/main/webapp/app/shared/shared.module.ts
   create src/main/webapp/app/shared/shared-libs.module.ts
   create src/main/webapp/app/shared/date/duration.pipe.ts
   create src/main/webapp/app/shared/date/format-medium-date.pipe.ts
   create src/main/webapp/app/shared/date/format-medium-datetime.pipe.ts
   create src/main/webapp/app/shared/sort/sort.directive.ts
   create src/main/webapp/app/shared/sort/sort-by.directive.ts
   create src/main/webapp/app/shared/pagination/item-count.component.ts
   create src/main/webapp/app/shared/alert/alert.component.ts
   create src/main/webapp/app/shared/alert/alert.component.html
   create src/main/webapp/app/shared/alert/alert-error.component.ts
   create src/main/webapp/app/shared/alert/alert-error.component.html
   create src/main/webapp/app/shared/alert/alert-error.model.ts
   create src/main/webapp/app/shared/language/translation.module.ts
   create src/main/webapp/app/admin/configuration/configuration.component.spec.ts
   create src/main/webapp/app/shared/language/find-language-from-key.pipe.ts
   create src/main/webapp/app/admin/configuration/configuration.service.spec.ts
   create src/main/webapp/app/shared/language/translate.directive.ts
   create src/main/webapp/app/admin/health/modal/health-modal.component.spec.ts
   create src/main/webapp/app/core/auth/state-storage.service.ts
   create src/main/webapp/app/admin/health/health.component.spec.ts
   create src/main/webapp/app/shared/auth/has-any-authority.directive.ts
   create src/main/webapp/app/admin/health/health.service.spec.ts
   create src/main/webapp/app/core/auth/account.model.ts
   create src/main/webapp/app/admin/logs/logs.component.spec.ts
   create src/main/webapp/app/core/auth/account.service.ts
   create src/main/webapp/app/admin/logs/logs.service.spec.ts
   create src/main/webapp/app/core/auth/account.service.spec.ts
   create src/main/webapp/app/admin/metrics/metrics.component.spec.ts
   create src/main/webapp/app/core/auth/user-route-access.service.ts
   create src/main/webapp/app/admin/metrics/metrics.service.spec.ts
   create src/main/webapp/app/core/auth/auth-jwt.service.ts
   create src/main/webapp/app/shared/auth/has-any-authority.directive.spec.ts
   create src/main/webapp/app/core/auth/auth-jwt.service.spec.ts
   create src/main/webapp/app/core/util/event-manager.service.spec.ts
   create src/main/webapp/app/core/util/data-util.service.spec.ts
   create src/main/webapp/app/core/util/parse-links.service.spec.ts
   create src/main/webapp/app/core/util/alert.service.spec.ts
   create src/main/webapp/app/home/home.component.spec.ts
   create src/main/webapp/app/layouts/main/main.component.spec.ts
   create src/main/webapp/app/layouts/navbar/navbar.component.spec.ts
   create src/main/webapp/app/layouts/profiles/page-ribbon.component.spec.ts
   create src/main/webapp/app/shared/alert/alert.component.spec.ts
   create src/main/webapp/app/shared/alert/alert-error.component.spec.ts
   create src/main/webapp/app/shared/date/format-medium-date.pipe.spec.ts
   create src/main/webapp/app/shared/date/format-medium-datetime.pipe.spec.ts
   create src/main/webapp/app/shared/sort/sort.directive.spec.ts
   create src/main/webapp/app/shared/sort/sort-by.directive.spec.ts
   create src/main/webapp/app/shared/pagination/item-count.component.spec.ts
   create src/main/webapp/app/shared/language/translate.directive.spec.ts
   create src/main/webapp/app/account/activate/activate.component.spec.ts
   create src/main/webapp/app/account/activate/activate.service.spec.ts
   create src/main/webapp/app/account/password/password.component.spec.ts
   create src/main/webapp/app/account/password/password.service.spec.ts
   create src/main/webapp/app/account/password/password-strength-bar/password-strength-bar.component.spec.ts
   create src/main/webapp/app/account/password-reset/init/password-reset-init.component.spec.ts
   create src/main/webapp/app/account/password-reset/init/password-reset-init.service.spec.ts
   create src/main/webapp/app/account/password-reset/finish/password-reset-finish.component.spec.ts
   create src/main/webapp/app/account/password-reset/finish/password-reset-finish.service.spec.ts
   create src/main/webapp/app/account/register/register.component.spec.ts
   create src/main/webapp/app/account/register/register.service.spec.ts
   create src/main/webapp/app/account/settings/settings.component.spec.ts
   create src/main/webapp/app/login/login.component.spec.ts
   create src/main/webapp/app/admin/user-management/list/user-management.component.spec.ts
   create src/main/webapp/app/admin/user-management/detail/user-management-detail.component.spec.ts
   create src/main/webapp/app/admin/user-management/update/user-management-update.component.spec.ts
   create src/main/webapp/app/admin/user-management/delete/user-management-delete-dialog.component.spec.ts
   create src/main/webapp/app/admin/user-management/service/user-management.service.spec.ts
   create src/main/webapp/content/images/jhipster_family_member_0.svg
   create src/main/webapp/content/images/jhipster_family_member_0_head-192.png
   create src/main/webapp/content/images/jhipster_family_member_0_head-256.png
   create src/main/webapp/content/images/jhipster_family_member_0_head-384.png
   create src/main/webapp/content/images/jhipster_family_member_0_head-512.png
   create src/main/webapp/content/images/jhipster_family_member_1.svg
   create src/main/webapp/content/images/jhipster_family_member_1_head-192.png
   create src/main/webapp/content/images/jhipster_family_member_1_head-256.png
   create src/main/webapp/content/images/jhipster_family_member_1_head-384.png
   create src/main/webapp/content/images/jhipster_family_member_1_head-512.png
   create src/main/webapp/content/images/jhipster_family_member_2.svg
   create src/main/webapp/content/images/jhipster_family_member_2_head-192.png
   create src/main/webapp/content/images/jhipster_family_member_2_head-256.png
   create src/main/webapp/content/images/jhipster_family_member_2_head-384.png
   create src/main/webapp/content/images/jhipster_family_member_2_head-512.png
   create src/main/webapp/content/images/jhipster_family_member_3.svg
   create src/main/webapp/content/images/jhipster_family_member_3_head-192.png
   create src/main/webapp/content/images/jhipster_family_member_3_head-256.png
   create src/main/webapp/content/images/jhipster_family_member_3_head-384.png
   create src/main/webapp/content/images/jhipster_family_member_3_head-512.png
   create src/main/webapp/content/images/logo-jhipster.png
   create src/main/webapp/content/images/logo-pyhipster.png
   create src/main/webapp/favicon.ico
   create src/main/webapp/swagger-ui/dist/images/throbber.gif
   create .eslintignore
   create src/main/webapp/manifest.webapp
   create src/main/webapp/WEB-INF/web.xml
   create src/main/webapp/content/css/loading.css
   create src/main/webapp/robots.txt
   create src/main/webapp/404.html
   create src/main/webapp/index.html
   create src/main/webapp/swagger-ui/index.html
   create src/main/webapp/i18n/es/error.json
   create src/main/webapp/i18n/es/password.json
   create src/main/webapp/i18n/es/user-management.json
   create src/main/webapp/i18n/es/configuration.json
   create src/main/webapp/i18n/es/logs.json
   create src/main/webapp/i18n/es/register.json
   create src/main/webapp/i18n/es/metrics.json
   create src/main/webapp/i18n/es/activate.json
   create src/main/webapp/i18n/es/login.json
   create src/main/webapp/i18n/es/global.json
   create src/main/webapp/i18n/es/sessions.json
   create src/main/webapp/i18n/es/reset.json
   create src/main/webapp/i18n/es/health.json
   create src/main/webapp/i18n/es/settings.json
   create src/main/webapp/i18n/es/home.json
   create src/main/webapp/i18n/en/error.json
   create src/main/webapp/i18n/en/settings.json
   create src/main/webapp/i18n/en/login.json
   create src/main/webapp/i18n/en/user-management.json
   create src/main/webapp/i18n/en/home.json
   create src/main/webapp/i18n/en/configuration.json
   create src/main/webapp/i18n/en/logs.json
   create src/main/webapp/i18n/en/password.json
   create src/main/webapp/i18n/en/metrics.json
   create src/main/webapp/i18n/en/register.json
   create src/main/webapp/i18n/en/activate.json
   create src/main/webapp/i18n/en/global.json
   create src/main/webapp/i18n/en/sessions.json
   create src/main/webapp/i18n/en/reset.json
   create src/main/webapp/i18n/en/health.json
   create src/main/webapp/i18n/nl/error.json
   create src/main/webapp/i18n/nl/login.json
   create src/main/webapp/i18n/nl/home.json
   create src/main/webapp/i18n/nl/password.json
   create src/main/webapp/i18n/nl/register.json
   create src/main/webapp/i18n/nl/sessions.json
   create src/main/webapp/i18n/nl/settings.json
   create src/main/webapp/i18n/nl/user-management.json
   create src/main/webapp/i18n/nl/configuration.json
   create src/main/webapp/i18n/nl/logs.json
   create src/main/webapp/i18n/nl/metrics.json
   create src/main/webapp/i18n/nl/activate.json
   create src/main/webapp/i18n/nl/global.json
   create src/main/webapp/i18n/nl/reset.json
   create src/main/webapp/i18n/nl/health.json
   create src/main/resources/i18n/messages_es.properties
   create src/test/resources/i18n/messages_es.properties
   create src/main/resources/i18n/messages_en.properties
   create src/test/resources/i18n/messages_en.properties
   create src/main/resources/i18n/messages_nl.properties
   create src/test/resources/i18n/messages_nl.properties
   create src/main/python/rest/RegionResource.py
   create src/main/python/schema/RegionSchema.py
   create src/main/webapp/app/entities/region/region.model.ts
   create src/main/webapp/app/entities/region/list/region.component.html
   create src/main/webapp/app/entities/region/region.module.ts
   create src/main/webapp/app/entities/region/detail/region-detail.component.html
   create src/main/webapp/app/entities/region/list/region.component.ts
   create src/main/webapp/app/entities/region/detail/region-detail.component.ts
   create src/main/webapp/app/entities/region/route/region-routing.module.ts
   create src/main/webapp/app/entities/region/route/region-routing-resolve.service.ts
   create src/main/webapp/app/entities/region/detail/region-detail.component.spec.ts
   create src/main/webapp/app/entities/region/list/region.component.spec.ts
   create src/main/webapp/app/entities/region/route/region-routing-resolve.service.spec.ts
   create src/main/webapp/app/entities/region/service/region.service.ts
   create src/main/webapp/app/entities/region/service/region.service.spec.ts
   create src/main/webapp/app/entities/region/update/region-update.component.html
   create src/main/webapp/app/entities/region/delete/region-delete-dialog.component.html
   create src/main/webapp/app/entities/region/delete/region-delete-dialog.component.spec.ts
   create src/main/webapp/i18n/es/region.json
   create src/main/webapp/app/entities/region/update/region-update.component.ts
   create src/main/webapp/i18n/en/region.json
   create src/main/webapp/app/entities/region/delete/region-delete-dialog.component.ts
   create src/main/webapp/i18n/nl/region.json
   create src/main/webapp/app/entities/region/update/region-update.component.spec.ts
   create src/main/python/rest/CountryResource.py
   create src/main/python/schema/CountrySchema.py
   create src/main/webapp/app/entities/country/country.model.ts
   create src/main/webapp/app/entities/country/list/country.component.html
   create src/main/webapp/app/entities/country/detail/country-detail.component.html
   create src/main/webapp/app/entities/country/country.module.ts
   create src/main/webapp/app/entities/country/route/country-routing.module.ts
   create src/main/webapp/app/entities/country/detail/country-detail.component.spec.ts
   create src/main/webapp/app/entities/country/list/country.component.spec.ts
   create src/main/webapp/app/entities/country/route/country-routing-resolve.service.ts
   create src/main/webapp/app/entities/country/list/country.component.ts
   create src/main/webapp/app/entities/country/route/country-routing-resolve.service.spec.ts
   create src/main/webapp/app/entities/country/detail/country-detail.component.ts
   create src/main/webapp/app/entities/country/service/country.service.ts
   create src/main/webapp/app/entities/country/update/country-update.component.html
   create src/main/webapp/i18n/es/country.json
   create src/main/webapp/app/entities/country/delete/country-delete-dialog.component.html
   create src/main/webapp/i18n/en/country.json
   create src/main/webapp/app/entities/country/update/country-update.component.ts
   create src/main/webapp/i18n/nl/country.json
   create src/main/webapp/app/entities/country/delete/country-delete-dialog.component.ts
   create src/main/python/rest/LocationResource.py
   create src/main/webapp/app/entities/country/service/country.service.spec.ts
   create src/main/python/schema/LocationSchema.py
   create src/main/webapp/app/entities/country/update/country-update.component.spec.ts
   create src/main/webapp/app/entities/country/delete/country-delete-dialog.component.spec.ts
   create src/main/webapp/app/entities/location/location.model.ts
   create src/main/webapp/app/entities/location/list/location.component.html
   create src/main/webapp/app/entities/location/detail/location-detail.component.html
   create src/main/webapp/app/entities/location/location.module.ts
   create src/main/webapp/app/entities/location/detail/location-detail.component.spec.ts
   create src/main/webapp/app/entities/location/route/location-routing.module.ts
   create src/main/webapp/app/entities/location/list/location.component.spec.ts
   create src/main/webapp/app/entities/location/route/location-routing-resolve.service.ts
   create src/main/webapp/app/entities/location/route/location-routing-resolve.service.spec.ts
   create src/main/webapp/app/entities/location/list/location.component.ts
   create src/main/webapp/app/entities/location/detail/location-detail.component.ts
   create src/main/webapp/i18n/es/location.json
   create src/main/webapp/app/entities/location/service/location.service.ts
   create src/main/webapp/app/entities/location/update/location-update.component.html
   create src/main/webapp/i18n/en/location.json
   create src/main/webapp/app/entities/location/delete/location-delete-dialog.component.html
   create src/main/webapp/i18n/nl/location.json
   create src/main/webapp/app/entities/location/update/location-update.component.ts
   create src/main/python/rest/DepartmentResource.py
   create src/main/webapp/app/entities/location/delete/location-delete-dialog.component.ts
   create src/main/python/schema/DepartmentSchema.py
   create src/main/webapp/app/entities/location/service/location.service.spec.ts
   create src/main/webapp/app/entities/location/update/location-update.component.spec.ts
   create src/main/webapp/app/entities/location/delete/location-delete-dialog.component.spec.ts
   create src/main/webapp/app/entities/department/department.model.ts
   create src/main/webapp/app/entities/department/list/department.component.html
   create src/main/webapp/app/entities/department/detail/department-detail.component.html
   create src/main/webapp/app/entities/department/department.module.ts
   create src/main/webapp/app/entities/department/route/department-routing.module.ts
   create src/main/webapp/app/entities/department/route/department-routing-resolve.service.ts
   create src/main/webapp/app/entities/department/detail/department-detail.component.spec.ts
   create src/main/webapp/app/entities/department/list/department.component.ts
   create src/main/webapp/app/entities/department/list/department.component.spec.ts
   create src/main/webapp/app/entities/department/detail/department-detail.component.ts
   create src/main/webapp/app/entities/department/route/department-routing-resolve.service.spec.ts
   create src/main/webapp/app/entities/department/service/department.service.ts
   create src/main/webapp/app/entities/department/service/department.service.spec.ts
   create src/main/webapp/app/entities/department/update/department-update.component.html
   create src/main/webapp/app/entities/department/update/department-update.component.spec.ts
   create src/main/webapp/app/entities/department/delete/department-delete-dialog.component.html
   create src/main/webapp/app/entities/department/update/department-update.component.ts
   create src/main/webapp/i18n/es/department.json
   create src/main/webapp/i18n/en/department.json
   create src/main/webapp/i18n/nl/department.json
   create src/main/webapp/app/entities/department/delete/department-delete-dialog.component.ts
   create src/main/python/rest/TaskResource.py
   create src/main/webapp/app/entities/department/delete/department-delete-dialog.component.spec.ts
   create src/main/python/schema/TaskSchema.py
   create src/main/webapp/app/entities/task/task.model.ts
   create src/main/webapp/app/entities/task/list/task.component.html
   create src/main/webapp/app/entities/task/task.module.ts
   create src/main/webapp/app/entities/task/detail/task-detail.component.html
   create src/main/webapp/app/entities/task/list/task.component.ts
   create src/main/webapp/app/entities/task/route/task-routing.module.ts
   create src/main/webapp/app/entities/task/detail/task-detail.component.ts
   create src/main/webapp/app/entities/task/route/task-routing-resolve.service.ts
   create src/main/webapp/app/entities/task/service/task.service.ts
   create src/main/webapp/app/entities/task/update/task-update.component.html
   create src/main/webapp/app/entities/task/detail/task-detail.component.spec.ts
   create src/main/webapp/app/entities/task/list/task.component.spec.ts
   create src/main/webapp/app/entities/task/route/task-routing-resolve.service.spec.ts
   create src/main/webapp/app/entities/task/service/task.service.spec.ts
   create src/main/webapp/app/entities/task/update/task-update.component.spec.ts
   create src/main/webapp/app/entities/task/delete/task-delete-dialog.component.html
   create src/main/webapp/app/entities/task/delete/task-delete-dialog.component.spec.ts
   create src/main/webapp/i18n/es/task.json
   create src/main/webapp/app/entities/task/update/task-update.component.ts
   create src/main/webapp/i18n/en/task.json
   create src/main/webapp/i18n/nl/task.json
   create src/main/webapp/app/entities/task/delete/task-delete-dialog.component.ts
   create src/main/python/rest/EmployeeResource.py
   create src/main/python/schema/EmployeeSchema.py
   create src/main/webapp/app/entities/employee/employee.model.ts
   create src/main/webapp/app/entities/employee/list/employee.component.html
   create src/main/webapp/app/entities/employee/list/employee.component.ts
   create src/main/webapp/app/entities/employee/detail/employee-detail.component.html
   create src/main/webapp/app/entities/employee/detail/employee-detail.component.ts
   create src/main/webapp/app/entities/employee/employee.module.ts
   create src/main/webapp/app/entities/employee/route/employee-routing.module.ts
   create src/main/webapp/app/entities/employee/route/employee-routing-resolve.service.ts
   create src/main/webapp/app/entities/employee/service/employee.service.ts
   create src/main/webapp/app/entities/employee/update/employee-update.component.html
   create src/main/webapp/app/entities/employee/detail/employee-detail.component.spec.ts
   create src/main/webapp/app/entities/employee/list/employee.component.spec.ts
   create src/main/webapp/app/entities/employee/delete/employee-delete-dialog.component.html
   create src/main/webapp/app/entities/employee/route/employee-routing-resolve.service.spec.ts
   create src/main/webapp/app/entities/employee/update/employee-update.component.ts
   create src/main/webapp/app/entities/employee/service/employee.service.spec.ts
   create src/main/webapp/app/entities/employee/update/employee-update.component.spec.ts
   create src/main/webapp/app/entities/employee/delete/employee-delete-dialog.component.spec.ts
   create src/main/webapp/i18n/es/employee.json
   create src/main/webapp/i18n/en/employee.json
   create src/main/webapp/app/entities/employee/delete/employee-delete-dialog.component.ts
   create src/main/webapp/i18n/nl/employee.json
   create src/main/python/rest/JobResource.py
   create src/main/python/schema/JobSchema.py
   create src/main/webapp/app/entities/job/job.model.ts
   create src/main/webapp/app/entities/job/list/job.component.html
   create src/main/webapp/app/entities/job/detail/job-detail.component.html
   create src/main/webapp/app/entities/job/job.module.ts
   create src/main/webapp/app/entities/job/route/job-routing.module.ts
   create src/main/webapp/app/entities/job/route/job-routing-resolve.service.ts
   create src/main/webapp/app/entities/job/list/job.component.ts
   create src/main/webapp/app/entities/job/detail/job-detail.component.spec.ts
   create src/main/webapp/app/entities/job/detail/job-detail.component.ts
   create src/main/webapp/app/entities/job/list/job.component.spec.ts
   create src/main/webapp/app/entities/job/service/job.service.ts
   create src/main/webapp/app/entities/job/route/job-routing-resolve.service.spec.ts
   create src/main/webapp/app/entities/job/service/job.service.spec.ts
   create src/main/webapp/app/entities/job/update/job-update.component.html
   create src/main/webapp/app/entities/job/update/job-update.component.spec.ts
   create src/main/webapp/app/entities/job/delete/job-delete-dialog.component.html
   create src/main/webapp/app/entities/job/delete/job-delete-dialog.component.spec.ts
   create src/main/webapp/i18n/es/job.json
   create src/main/webapp/app/entities/job/update/job-update.component.ts
   create src/main/webapp/i18n/en/job.json
   create src/main/webapp/i18n/nl/job.json
   create src/main/webapp/app/entities/job/delete/job-delete-dialog.component.ts
   create src/main/python/rest/JobHistoryResource.py
   create src/main/python/schema/JobHistorySchema.py
   create src/main/python/domain/enumeration/Language.py
   create src/main/webapp/app/entities/enumerations/language.model.ts
   create src/main/webapp/app/entities/job-history/job-history.model.ts
   create src/main/webapp/app/entities/job-history/job-history.module.ts
   create src/main/webapp/app/entities/job-history/list/job-history.component.html
   create src/main/webapp/app/entities/job-history/list/job-history.component.ts
   create src/main/webapp/app/entities/job-history/detail/job-history-detail.component.html
   create src/main/webapp/app/entities/job-history/route/job-history-routing.module.ts
   create src/main/webapp/app/entities/job-history/route/job-history-routing-resolve.service.ts
   create src/main/webapp/app/entities/job-history/detail/job-history-detail.component.ts
   create src/main/webapp/app/entities/job-history/detail/job-history-detail.component.spec.ts
   create src/main/webapp/app/entities/job-history/service/job-history.service.ts
   create src/main/webapp/app/entities/job-history/list/job-history.component.spec.ts
   create src/main/webapp/app/entities/job-history/route/job-history-routing-resolve.service.spec.ts
   create src/main/webapp/app/entities/job-history/update/job-history-update.component.html
   create src/main/webapp/app/entities/job-history/service/job-history.service.spec.ts
   create src/main/webapp/app/entities/job-history/delete/job-history-delete-dialog.component.html
   create src/main/webapp/app/entities/job-history/update/job-history-update.component.spec.ts
   create src/main/webapp/app/entities/job-history/delete/job-history-delete-dialog.component.spec.ts
   create src/main/webapp/app/entities/job-history/update/job-history-update.component.ts
   create src/main/webapp/i18n/es/language.json
   create src/main/webapp/i18n/en/language.json
   create src/main/webapp/i18n/nl/language.json
   create src/main/webapp/i18n/es/jobHistory.json
   create src/main/webapp/app/entities/job-history/delete/job-history-delete-dialog.component.ts
   create src/main/webapp/i18n/en/jobHistory.json
   create src/main/webapp/i18n/nl/jobHistory.json
   create src/main/resources/config/liquibase/changelog/20240222115108_added_entity_Region.xml
   create src/main/resources/config/liquibase/fake-data/region.csv
   create src/main/resources/config/liquibase/changelog/20240222115208_added_entity_Country.xml
   create src/main/resources/config/liquibase/changelog/20240222115208_added_entity_constraints_Country.xml
   create src/main/resources/config/liquibase/fake-data/country.csv
   create src/main/resources/config/liquibase/changelog/20240222115308_added_entity_Location.xml
   create src/main/resources/config/liquibase/changelog/20240222115308_added_entity_constraints_Location.xml
   create src/main/resources/config/liquibase/fake-data/location.csv
   create src/main/resources/config/liquibase/changelog/20240222115408_added_entity_Department.xml
   create src/main/resources/config/liquibase/changelog/20240222115408_added_entity_constraints_Department.xml
   create src/main/resources/config/liquibase/fake-data/department.csv
   create src/main/resources/config/liquibase/changelog/20240222115508_added_entity_Task.xml
   create src/main/resources/config/liquibase/fake-data/task.csv
   create src/main/resources/config/liquibase/changelog/20240222115608_added_entity_Employee.xml
   create src/main/resources/config/liquibase/changelog/20240222115608_added_entity_constraints_Employee.xml
   create src/main/resources/config/liquibase/fake-data/employee.csv
   create src/main/resources/config/liquibase/changelog/20240222115708_added_entity_Job.xml
   create src/main/resources/config/liquibase/changelog/20240222115708_added_entity_constraints_Job.xml
   create src/main/resources/config/liquibase/fake-data/job.csv
   create src/main/resources/config/liquibase/changelog/20240222115808_added_entity_JobHistory.xml
   create src/main/resources/config/liquibase/changelog/20240222115808_added_entity_constraints_JobHistory.xml
   create src/main/resources/config/liquibase/fake-data/job_history.csv
   create README.md
   create src/main/python/domain/Region.py
   create src/main/python/domain/Country.py
   create src/main/python/domain/Location.py
   create src/main/python/domain/Department.py
   create src/main/python/domain/Task.py
   create src/main/python/domain/Employee.py
   create src/main/python/domain/Job.py
   create src/main/python/domain/JobHistory.py
    force .yo-rc.json
     info Installing Python modules
Creating virtualenv delivery in /projects/pyhipster-devspace/app/.venv
Updating dependencies
Resolving dependencies...

Package operations: 64 installs, 0 updates, 0 removals

  • Installing attrs (23.2.0)
  • Installing rpds-py (0.18.0)
  • Installing markupsafe (2.1.5)
  • Installing mdurl (0.1.2)
  • Installing referencing (0.33.0)
  • Installing click (8.1.7)
  • Installing exceptiongroup (1.2.0)
  • Installing iniconfig (2.0.0)
  • Installing itsdangerous (2.1.2)
  • Installing jinja2 (3.1.3)
  • Installing jsonschema-specifications (2023.12.1)
  • Installing markdown-it-py (3.0.0)
  • Installing greenlet (3.0.3)
  • Installing packaging (23.2)
  • Installing pbr (6.0.0)
  • Installing pluggy (1.4.0)
  • Installing pygments (2.17.2)
  • Installing six (1.16.0)
  • Installing tomli (2.0.1)
  • Installing werkzeug (2.1.2)
  • Installing aniso8601 (9.0.1)
  • Installing blinker (1.7.0)
  • Installing certifi (2024.2.2)
  • Installing colorama (0.4.6)
  • Installing coverage (7.4.2)
  • Installing idna (3.6)
  • Installing flask (2.1.2)
  • Installing marshmallow (3.18.0)
  • Installing mypy-extensions (1.0.0)
  • Installing jsonschema (4.21.1)
  • Installing numpy (1.26.4)
  • Installing charset-normalizer (3.3.2)
  • Installing pathspec (0.12.1)
  • Installing platformdirs (4.2.0)
  • Installing psutil (5.9.8)
  • Installing pyjwt (2.8.0)
  • Installing pytest (7.4.0)
  • Installing python-dateutil (2.8.2)
  • Installing pytz (2024.1)
  • Installing pyyaml (6.0.1)
  • Installing rich (13.7.0)
  • Installing sqlalchemy (1.4.40)
  • Installing stevedore (5.1.0)
  • Installing typing-extensions (4.3.0)
  • Installing urllib3 (2.2.1)
  • Installing wtforms (3.1.2)
  • Installing bandit (1.7.7)
  • Installing bcrypt (4.1.2)
  • Installing black (23.12.1)
  • Installing flask-jwt-extended (4.4.4)
  • Installing flask-mail (0.9.1)
  • Installing flask-restx (0.5.1)
  • Installing flask-sqlalchemy (2.5.1)
  • Installing flask-wtf (1.0.1)
  • Installing flask-marshmallow (0.14.0)
  • Installing flask-testing (0.8.1)
  • Installing pandas (1.3.5)
  • Installing marshmallow-sqlalchemy (0.28.1)
  • Installing psycopg2-binary (2.9.9)
  • Installing pytest-cov (4.1.0)
  • Installing pytest-flask (1.2.0)
  • Installing requests (2.31.0)
  • Installing ruff (0.0.284)
  • Installing taskipy (1.12.2)

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
