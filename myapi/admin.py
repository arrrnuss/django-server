from django.contrib import admin
# from .models import AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions
# from .models import Baseleavedays, Companys, Departments, DjangoAdminLog, DjangoContentType, DjangoMigrations
# from .models import DjangoSession, Holidays, MyapiCompanys, MyapiUsers, Positions, ReportLeaves, RequestInfos
# from .models import RequestLeaves, Sequelizemeta, Squadmembers, Squads, Tokens, Users

# List of models to register
models_to_register = [
    # AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions,
    # Baseleavedays, Companys, Departments, DjangoAdminLog, DjangoContentType, DjangoMigrations,
    # DjangoSession, Holidays, MyapiCompanys, MyapiUsers, Positions, ReportLeaves, RequestInfos,
    # RequestLeaves, Sequelizemeta, Squadmembers, Squads, Tokens, Users
]

# Register all models
for model in models_to_register:
    admin.site.register(model)