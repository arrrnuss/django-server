# myapi/serializers.py
from rest_framework import serializers
from .models import (
    # AuthUser, AuthGroup, AuthPermission, DjangoContentType, DjangoSession,
    # DjangoAdminLog, DjangoMigrations, Baseleavedays,  Departments,
    # Holidays, MyapiCompanys, MyapiUsers, Positions, ReportLeaves, RequestInfos,
    # RequestLeaves, Squadmembers, Squads, Tokens, 
    Users ,Companys,
)

# class AuthUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AuthUser
#         fields = '__all__'

# class AuthGroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AuthGroup
#         fields = '__all__'

# class AuthPermissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AuthPermission
#         fields = '__all__'

# class DjangoContentTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DjangoContentType
#         fields = '__all__'

# class DjangoSessionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DjangoSession
#         fields = '__all__'

# class DjangoAdminLogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DjangoAdminLog
#         fields = '__all__'

# class DjangoMigrationsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DjangoMigrations
#         fields = '__all__'

# class BaseleavedaysSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Baseleavedays
#         fields = '__all__'

class CompanysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companys
        fields = '__all__'

# class DepartmentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Departments
#         fields = '__all__'

# class HolidaysSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Holidays
#         fields = '__all__'

# class MyapiCompanysSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyapiCompanys
#         fields = '__all__'

# class MyapiUsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyapiUsers
#         fields = '__all__'

# class PositionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Positions
#         fields = '__all__'

# class ReportLeavesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ReportLeaves
#         fields = '__all__'

# class RequestInfosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RequestInfos
#         fields = '__all__'

# class RequestLeavesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RequestLeaves
#         fields = '__all__'

# class SquadmembersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Squadmembers
#         fields = '__all__'

# class SquadsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Squads
#         fields = '__all__'

# class TokensSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tokens
#         fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
