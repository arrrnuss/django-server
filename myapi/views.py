from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import (
    # AuthGroupSerializer,
    # # AuthGroupPermissionsSerializer,
    # AuthPermissionSerializer,
    # AuthUserSerializer,
    # # AuthUserGroupsSerializer,
    # # AuthUserUserPermissionsSerializer,
    # BaseleavedaysSerializer,
    CompanysSerializer,
    # DepartmentsSerializer,
    # DjangoAdminLogSerializer,
    # DjangoContentTypeSerializer,
    # DjangoMigrationsSerializer,
    # DjangoSessionSerializer,
    # HolidaysSerializer,
    # MyapiCompanysSerializer,
    # MyapiUsersSerializer,
    # PositionsSerializer,
    # ReportLeavesSerializer,
    # RequestInfosSerializer,
    # RequestLeavesSerializer,
    # # SequelizemetaSerializer,
    # SquadmembersSerializer,
    # SquadsSerializer,
    # TokensSerializer,
    UsersSerializer,
)

from .models import (
    # AuthGroup,
    # AuthGroupPermissions,
    # AuthPermission,
    # AuthUser,
    # AuthUserGroups,
    # AuthUserUserPermissions,
    # Baseleavedays,
    Companys,
    # Departments,
    # DjangoAdminLog,
    # DjangoContentType,
    # DjangoMigrations,
    # DjangoSession,
    # Holidays,
    # MyapiCompanys,
    # MyapiUsers,
    # Positions,
    # ReportLeaves,
    # RequestInfos,
    # RequestLeaves,
    # Sequelizemeta,
    # Squadmembers,
    # Squads,
    # Tokens,
    Users,
)


# class AuthGroupViewSet(viewsets.ModelViewSet):
#     queryset = AuthGroup.objects.all()
#     serializer_class = AuthGroupSerializer


# class AuthGroupPermissionsViewSet(viewsets.ModelViewSet):
#     queryset = AuthGroupPermissions.objects.all()
#     serializer_class = AuthGroupPermissionsSerializer


# class AuthPermissionViewSet(viewsets.ModelViewSet):
#     queryset = AuthPermission.objects.all()
#     serializer_class = AuthPermissionSerializer


# class AuthUserViewSet(viewsets.ModelViewSet):
#     queryset = AuthUser.objects.all()
#     serializer_class = AuthUserSerializer


# class AuthUserGroupsViewSet(viewsets.ModelViewSet):
#     queryset = AuthUserGroups.objects.all()
#     serializer_class = AuthUserGroupsSerializer


# class AuthUserUserPermissionsViewSet(viewsets.ModelViewSet):
#     queryset = AuthUserUserPermissions.objects.all()
#     serializer_class = AuthUserUserPermissionsSerializer


# class BaseleavedaysViewSet(viewsets.ModelViewSet):
#     queryset = Baseleavedays.objects.all()
#     serializer_class = BaseleavedaysSerializer


class CompanysViewSet(viewsets.ModelViewSet):
    queryset = Companys.objects.all()
    serializer_class = CompanysSerializer


# class DepartmentsViewSet(viewsets.ModelViewSet):
#     queryset = Departments.objects.all()
#     serializer_class = DepartmentsSerializer


# class DjangoAdminLogViewSet(viewsets.ModelViewSet):
#     queryset = DjangoAdminLog.objects.all()
#     serializer_class = DjangoAdminLogSerializer


# class DjangoContentTypeViewSet(viewsets.ModelViewSet):
#     queryset = DjangoContentType.objects.all()
#     serializer_class = DjangoContentTypeSerializer


# class DjangoMigrationsViewSet(viewsets.ModelViewSet):
#     queryset = DjangoMigrations.objects.all()
#     serializer_class = DjangoMigrationsSerializer


# class DjangoSessionViewSet(viewsets.ModelViewSet):
#     queryset = DjangoSession.objects.all()
#     serializer_class = DjangoSessionSerializer


# class HolidaysViewSet(viewsets.ModelViewSet):
#     queryset = Holidays.objects.all()
#     serializer_class = HolidaysSerializer


# class MyapiCompanysViewSet(viewsets.ModelViewSet):
#     queryset = MyapiCompanys.objects.all()
#     serializer_class = MyapiCompanysSerializer


# class MyapiUsersViewSet(viewsets.ModelViewSet):
#     queryset = MyapiUsers.objects.all()
#     serializer_class = MyapiUsersSerializer


# class PositionsViewSet(viewsets.ModelViewSet):
#     queryset = Positions.objects.all()
#     serializer_class = PositionsSerializer


# class ReportLeavesViewSet(viewsets.ModelViewSet):
#     queryset = ReportLeaves.objects.all()
#     serializer_class = ReportLeavesSerializer


# class RequestInfosViewSet(viewsets.ModelViewSet):
#     queryset = RequestInfos.objects.all()
#     serializer_class = RequestInfosSerializer


# class RequestLeavesViewSet(viewsets.ModelViewSet):
#     queryset = RequestLeaves.objects.all()
#     serializer_class = RequestLeavesSerializer


# class SequelizemetaViewSet(viewsets.ModelViewSet):
#     queryset = Sequelizemeta.objects.all()
#     serializer_class = SequelizemetaSerializer


# class SquadmembersViewSet(viewsets.ModelViewSet):
#     queryset = Squadmembers.objects.all()
#     serializer_class = SquadmembersSerializer


# class SquadsViewSet(viewsets.ModelViewSet):
#     queryset = Squads.objects.all()
#     serializer_class = SquadsSerializer


# class TokensViewSet(viewsets.ModelViewSet):
#     queryset = Tokens.objects.all()
#     serializer_class = TokensSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


@api_view(['POST'])
def add_company(request):
    if request.method == 'POST':
        serializer = CompanysSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

# @api_view(['GET', 'PUT'])
# def detail_user(request, pk):
#     try:
#         user = Users.objects.get(pk=pk)
#     except Users.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = UsersSerializer(user)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         # User is able to modify only his own data
#         if not (request.user and request.user.id == user.id): 
#             return HttpResponseForbidden("You can't edit this profile")
        
#         serializer = UsersSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
