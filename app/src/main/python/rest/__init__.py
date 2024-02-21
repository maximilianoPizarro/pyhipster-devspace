from .PublicUserResource import public_user_list_ns
from .AuthorityResource import authority_list_ns
from .UserJWTController import jwt_authentication_ns
from .AccountResource import account_register_ns, account_authenticate_ns, account_ns, \
    account_activate_ns, passwd_reset_init_ns, passwd_reset_finish_ns, change_passwd_ns
from .UserResource import user_list_ns
from .LogoutResource import logout_ns
from .AppManagment import app_management_ns
from .RegionResource import regions_list_ns
from .CountryResource import countries_list_ns
from .LocationResource import locations_list_ns
from .DepartmentResource import departments_list_ns
from .TaskResource import tasks_list_ns
from .EmployeeResource import employees_list_ns
from .JobResource import jobs_list_ns
from .JobHistoryResource import job_histories_list_ns
# pyhipster-needle-rest-api-list-add-entry-import

def add_api_namespace(api):
    # Registering the namespaces
    api.add_namespace(public_user_list_ns)
    api.add_namespace(authority_list_ns)
    api.add_namespace(jwt_authentication_ns)
    api.add_namespace(logout_ns)
    api.add_namespace(account_register_ns)
    api.add_namespace(account_authenticate_ns)
    api.add_namespace(account_ns)
    api.add_namespace(account_activate_ns)
    api.add_namespace(passwd_reset_init_ns)
    api.add_namespace(passwd_reset_finish_ns)
    api.add_namespace(change_passwd_ns)
    api.add_namespace(user_list_ns)
    api.add_namespace(app_management_ns)
    api.add_namespace(regions_list_ns)
    api.add_namespace(countries_list_ns)
    api.add_namespace(locations_list_ns)
    api.add_namespace(departments_list_ns)
    api.add_namespace(tasks_list_ns)
    api.add_namespace(employees_list_ns)
    api.add_namespace(jobs_list_ns)
    api.add_namespace(job_histories_list_ns)
    # pyhipster-needle-rest-api-list-add-namespaces

    # Adding resources to added namespaces
    public_user_list_ns.add_resource(PublicUserResource.PublicUserResourceList, "")
    authority_list_ns.add_resource(AuthorityResource.AuthorityResourceList, "")
    jwt_authentication_ns.add_resource(UserJWTController.UserJWTResource, "")
    logout_ns.add_resource(LogoutResource.LogoutResource, "")
    account_register_ns.add_resource(AccountResource.ManagedUserAccountRegister, "")
    account_authenticate_ns.add_resource(AccountResource.AccountAuthenticate, "")
    account_ns.add_resource(AccountResource.AdminAccountDetails, "")
    account_activate_ns.add_resource(AccountResource.AccountActivate, "")
    passwd_reset_init_ns.add_resource(AccountResource.AccountPasswordResetInit, "")
    passwd_reset_finish_ns.add_resource(AccountResource.AccountPasswordResetFinish, "")
    change_passwd_ns.add_resource(AccountResource.AccountChangePassword, "")
    user_list_ns.add_resource(UserResource.UserResource, "/<string:login>")
    user_list_ns.add_resource(UserResource.UserResourceList, "")
    app_management_ns.add_resource(AppManagment.AppManagementInfoResource, "/info")
    app_management_ns.add_resource(AppManagment.AppManagementEnvironmentResource, "/env")
    app_management_ns.add_resource(AppManagment.AppManagementConfigurationResource, "/configprops")
    app_management_ns.add_resource(AppManagment.AppManagementOpenAPIResource, "/jhiopenapigroups")
    # pyhipster-needle-rest-api-list-add-resource
    # pyhipster-needle-rest-api-list-add-resource-list
    regions_list_ns.add_resource(RegionResource.RegionResourceList, "")
    regions_list_ns.add_resource(RegionResource.RegionResourceListCount, "/count")
    regions_list_ns.add_resource(RegionResource.RegionResource, "/<int:id>")
    countries_list_ns.add_resource(CountryResource.CountryResourceList, "")
    countries_list_ns.add_resource(CountryResource.CountryResourceListCount, "/count")
    countries_list_ns.add_resource(CountryResource.CountryResource, "/<int:id>")
    locations_list_ns.add_resource(LocationResource.LocationResourceList, "")
    locations_list_ns.add_resource(LocationResource.LocationResourceListCount, "/count")
    locations_list_ns.add_resource(LocationResource.LocationResource, "/<int:id>")
    departments_list_ns.add_resource(DepartmentResource.DepartmentResourceList, "")
    departments_list_ns.add_resource(DepartmentResource.DepartmentResourceListCount, "/count")
    departments_list_ns.add_resource(DepartmentResource.DepartmentResource, "/<int:id>")
    tasks_list_ns.add_resource(TaskResource.TaskResourceList, "")
    tasks_list_ns.add_resource(TaskResource.TaskResourceListCount, "/count")
    tasks_list_ns.add_resource(TaskResource.TaskResource, "/<int:id>")
    employees_list_ns.add_resource(EmployeeResource.EmployeeResourceList, "")
    employees_list_ns.add_resource(EmployeeResource.EmployeeResourceListCount, "/count")
    employees_list_ns.add_resource(EmployeeResource.EmployeeResource, "/<int:id>")
    jobs_list_ns.add_resource(JobResource.JobResourceList, "")
    jobs_list_ns.add_resource(JobResource.JobResourceListCount, "/count")
    jobs_list_ns.add_resource(JobResource.JobResource, "/<int:id>")
    job_histories_list_ns.add_resource(JobHistoryResource.JobHistoryResourceList, "")
    job_histories_list_ns.add_resource(JobHistoryResource.JobHistoryResourceListCount, "/count")
    job_histories_list_ns.add_resource(JobHistoryResource.JobHistoryResource, "/<int:id>")
    # pyhipster-needle-rest-api-list-add-resource-list-count

    return api



