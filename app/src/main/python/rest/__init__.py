from .PublicUserResource import public_user_list_ns
from .AuthorityResource import authority_list_ns
from .UserJWTController import jwt_authentication_ns
from .AccountResource import account_register_ns, account_authenticate_ns, account_ns, \
    account_activate_ns, passwd_reset_init_ns, passwd_reset_finish_ns, change_passwd_ns
from .UserResource import user_list_ns
from .LogoutResource import logout_ns
from .AppManagment import app_management_ns
from .ProductoResource import productos_list_ns
from .ProductoCategoriaResource import producto_categorias_list_ns
from .ClienteResource import clientes_list_ns
from .CarritoResource import carritos_list_ns
from .ProductoOrdenResource import producto_ordens_list_ns
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
    api.add_namespace(productos_list_ns)
    api.add_namespace(producto_categorias_list_ns)
    api.add_namespace(clientes_list_ns)
    api.add_namespace(carritos_list_ns)
    api.add_namespace(producto_ordens_list_ns)
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
    productos_list_ns.add_resource(ProductoResource.ProductoResourceList, "")
    productos_list_ns.add_resource(ProductoResource.ProductoResourceListCount, "/count")
    productos_list_ns.add_resource(ProductoResource.ProductoResource, "/<int:id>")
    producto_categorias_list_ns.add_resource(ProductoCategoriaResource.ProductoCategoriaResourceList, "")
    producto_categorias_list_ns.add_resource(ProductoCategoriaResource.ProductoCategoriaResourceListCount, "/count")
    producto_categorias_list_ns.add_resource(ProductoCategoriaResource.ProductoCategoriaResource, "/<int:id>")
    clientes_list_ns.add_resource(ClienteResource.ClienteResourceList, "")
    clientes_list_ns.add_resource(ClienteResource.ClienteResourceListCount, "/count")
    clientes_list_ns.add_resource(ClienteResource.ClienteResource, "/<int:id>")
    carritos_list_ns.add_resource(CarritoResource.CarritoResourceList, "")
    carritos_list_ns.add_resource(CarritoResource.CarritoResourceListCount, "/count")
    carritos_list_ns.add_resource(CarritoResource.CarritoResource, "/<int:id>")
    producto_ordens_list_ns.add_resource(ProductoOrdenResource.ProductoOrdenResourceList, "")
    producto_ordens_list_ns.add_resource(ProductoOrdenResource.ProductoOrdenResourceListCount, "/count")
    producto_ordens_list_ns.add_resource(ProductoOrdenResource.ProductoOrdenResource, "/<int:id>")
    # pyhipster-needle-rest-api-list-add-resource-list-count

    return api



