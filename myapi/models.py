# This is an auto-generated Django model module.

# You'll have to do the following manually to clean this up:

#   * Rearrange models' order

#   * Make sure each model has one field with primary_key=True

#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior

#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table

# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models





class AuthGroup(models.Model):

    name = models.CharField(unique=True, max_length=150)



    class Meta:

        managed = False

        db_table = 'auth_group'





class AuthGroupPermissions(models.Model):

    id = models.BigAutoField(primary_key=True)

    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)



    class Meta:

        managed = False

        db_table = 'auth_group_permissions'

        unique_together = (('group', 'permission'),)





class AuthPermission(models.Model):

    name = models.CharField(max_length=255)

    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)

    codename = models.CharField(max_length=100)



    class Meta:

        managed = False

        db_table = 'auth_permission'

        unique_together = (('content_type', 'codename'),)





class AuthUser(models.Model):

    password = models.CharField(max_length=128)

    last_login = models.DateTimeField(blank=True, null=True)

    is_superuser = models.IntegerField()

    username = models.CharField(unique=True, max_length=150)

    first_name = models.CharField(max_length=150)

    last_name = models.CharField(max_length=150)

    email = models.CharField(max_length=254)

    is_staff = models.IntegerField()

    is_active = models.IntegerField()

    date_joined = models.DateTimeField()



    class Meta:

        managed = False

        db_table = 'auth_user'





class AuthUserGroups(models.Model):

    id = models.BigAutoField(primary_key=True)

    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)



    class Meta:

        managed = False

        db_table = 'auth_user_groups'

        unique_together = (('user', 'group'),)





class AuthUserUserPermissions(models.Model):

    id = models.BigAutoField(primary_key=True)

    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)



    class Meta:

        managed = False

        db_table = 'auth_user_user_permissions'

        unique_together = (('user', 'permission'),)





class Baseleavedays(models.Model):

    keyid = models.CharField(db_column='KeyID', primary_key=True, max_length=36, db_collation='utf8mb4_bin')  # Field name made lowercase.

    leavename = models.CharField(db_column='leaveName', unique=True, max_length=255)  # Field name made lowercase.

    baseday = models.IntegerField()

    upleaveday = models.IntegerField()

    wantfile = models.CharField(db_column='wantFile', max_length=255)  # Field name made lowercase.

    basedayfile = models.IntegerField(db_column='basedayFile')  # Field name made lowercase.

    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'baseleavedays'





class Companys(models.Model):

    keyid = models.CharField(db_column='KeyID', primary_key=True, max_length=36, db_collation='utf8mb4_bin')  # Field name made lowercase.

    company = models.CharField(unique=True, max_length=255, blank=True, null=True)

    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'companys'





class Departments(models.Model):

    keyid = models.CharField(db_column='KeyID', primary_key=True, max_length=36, db_collation='utf8mb4_bin')  # Field name made lowercase.

    companyid = models.ForeignKey(Companys, models.DO_NOTHING, db_column='companyId')  # Field name made lowercase.

    department = models.CharField(max_length=255, blank=True, null=True)

    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'departments'





class DjangoAdminLog(models.Model):

    action_time = models.DateTimeField()

    object_id = models.TextField(blank=True, null=True)

    object_repr = models.CharField(max_length=200)

    action_flag = models.PositiveSmallIntegerField()

    change_message = models.TextField()

    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)

    user = models.ForeignKey(AuthUser, models.DO_NOTHING)



    class Meta:

        managed = False

        db_table = 'django_admin_log'





class DjangoContentType(models.Model):

    app_label = models.CharField(max_length=100)

    model = models.CharField(max_length=100)



    class Meta:

        managed = False

        db_table = 'django_content_type'

        unique_together = (('app_label', 'model'),)





class DjangoMigrations(models.Model):

    id = models.BigAutoField(primary_key=True)

    app = models.CharField(max_length=255)

    name = models.CharField(max_length=255)

    applied = models.DateTimeField()



    class Meta:

        managed = False

        db_table = 'django_migrations'





class DjangoSession(models.Model):

    session_key = models.CharField(primary_key=True, max_length=40)

    session_data = models.TextField()

    expire_date = models.DateTimeField()



    class Meta:

        managed = False

        db_table = 'django_session'





class Holidays(models.Model):

    keyid = models.CharField(db_column='KeyID', primary_key=True, max_length=36, db_collation='utf8mb4_bin')  # Field name made lowercase.

    nameofholiday = models.CharField(unique=True, max_length=255, blank=True, null=True)

    dateofholiday = models.DateTimeField(blank=True, null=True)

    enddateofholiday = models.DateTimeField(blank=True, null=True)

    remark = models.CharField(max_length=255, blank=True, null=True)

    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'holidays'





class MyapiCompanys(models.Model):

    id = models.BigAutoField(primary_key=True)

    company = models.CharField(max_length=100)



    class Meta:

        managed = False

        db_table = 'myapi_companys'





class MyapiUsers(models.Model):

    id = models.BigAutoField(primary_key=True)

    fistname = models.CharField(db_column='fistName', max_length=100)  # Field name made lowercase.

    lastname = models.CharField(db_column='lastName', max_length=60)  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'myapi_users'





class Positions(models.Model):

    keyid = models.CharField(db_column='KeyID', primary_key=True, max_length=36, db_collation='utf8mb4_bin')  # Field name made lowercase.

    departmentid = models.ForeignKey(Departments, models.DO_NOTHING, db_column='departmentId')  # Field name made lowercase.

    position = models.CharField(max_length=255, blank=True, null=True)

    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    companyid = models.CharField(db_column='companyId', max_length=36, db_collation='utf8mb4_bin')  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'positions'





class ReportLeaves(models.Model):

    keyid = models.CharField(db_column='KeyID', primary_key=True, max_length=36, db_collation='utf8mb4_bin')  # Field name made lowercase.

    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    lastname = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    role = models.CharField(max_length=255, blank=True, null=True)

    squadname = models.CharField(max_length=255, blank=True, null=True)

    company = models.CharField(max_length=255, blank=True, null=True)

    department = models.CharField(max_length=255, blank=True, null=True)

    leavetype = models.CharField(max_length=255, blank=True, null=True)

    medicalcertificate = models.CharField(max_length=255, blank=True, null=True)

    reason = models.CharField(max_length=255, blank=True, null=True)

    startdate = models.DateTimeField(blank=True, null=True)

    enddate = models.DateTimeField(blank=True, null=True)

    useleaveday = models.IntegerField(blank=True, null=True)

    phonenumber = models.CharField(db_column='phoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.

    email = models.CharField(max_length=255, blank=True, null=True)

    statusfromtl = models.CharField(max_length=255, blank=True, null=True)

    statusofleave = models.CharField(max_length=255, blank=True, null=True)

    remark = models.CharField(max_length=255, blank=True, null=True)

    remarkfromtl = models.CharField(max_length=255, blank=True, null=True)

    remarkfromhr = models.CharField(max_length=255, blank=True, null=True)

    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.

    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'report_leaves'





class RequestInfos(models.Model):

    requestid = models.CharField(primary_key=True, max_length=36, db_collation='utf8mb4_bin')

    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    lastname = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    department = models.CharField(max_length=255, blank=True, null=True)

    company = models.CharField(max_length=255, blank=True, null=True)

    position = models.CharField(max_length=255, blank=True, null=True)

    age = models.CharField(max_length=255, blank=True, null=True)

    birthday = models.DateTimeField(blank=True, null=True)

    phonenumber = models.CharField(db_column='phoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.

    address = models.CharField(max_length=255, blank=True, null=True)

    email = models.CharField(max_length=255, blank=True, null=True)

    status = models.CharField(max_length=255, blank=True, null=True)

    remark = models.CharField(max_length=255, blank=True, null=True)

    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.

    firstnameold = models.CharField(db_column='firstNameOld', max_length=255, blank=True, null=True)  # Field name made lowercase.

    lastnameold = models.CharField(db_column='lastNameOld', max_length=255, blank=True, null=True)  # Field name made lowercase.

    departmentold = models.CharField(db_column='departmentOld', max_length=255, blank=True, null=True)  # Field name made lowercase.

    companyold = models.CharField(db_column='companyOld', max_length=255, blank=True, null=True)  # Field name made lowercase.

    positionold = models.CharField(db_column='positionOld', max_length=255, blank=True, null=True)  # Field name made lowercase.

    ageold = models.CharField(db_column='ageOld', max_length=255, blank=True, null=True)  # Field name made lowercase.

    birthdayold = models.DateTimeField(db_column='birthdayOld', blank=True, null=True)  # Field name made lowercase.

    phonenumberold = models.CharField(db_column='phoneNumberOld', max_length=255, blank=True, null=True)  # Field name made lowercase.

    addressold = models.CharField(db_column='addressOld', max_length=255, blank=True, null=True)  # Field name made lowercase.

    emailold = models.CharField(db_column='emailOld', max_length=255, blank=True, null=True)  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'request_infos'





class RequestLeaves(models.Model):

    keyid = models.CharField(db_column='KeyID', primary_key=True, max_length=36, db_collation='utf8mb4_bin')  # Field name made lowercase.

    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    lastname = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    role = models.CharField(max_length=255, blank=True, null=True)

    squadname = models.CharField(max_length=255, blank=True, null=True)

    company = models.CharField(max_length=255, blank=True, null=True)

    leavetype = models.CharField(max_length=255, blank=True, null=True)

    medicalcertificate = models.CharField(max_length=255, blank=True, null=True)

    reason = models.CharField(max_length=255, blank=True, null=True)

    startdate = models.DateTimeField(blank=True, null=True)

    enddate = models.DateTimeField(blank=True, null=True)

    phonenumber = models.CharField(db_column='phoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.

    email = models.CharField(max_length=255, blank=True, null=True)

    statusfromtl = models.CharField(max_length=255, blank=True, null=True)

    statusofleave = models.CharField(max_length=255, blank=True, null=True)

    remark = models.CharField(max_length=255, blank=True, null=True)

    remarkfromtl = models.CharField(max_length=255, blank=True, null=True)

    remarkfromhr = models.CharField(max_length=255, blank=True, null=True)

    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.

    useleaveday = models.IntegerField(blank=True, null=True)

    department = models.CharField(max_length=255, blank=True, null=True)



    class Meta:

        managed = False

        db_table = 'request_leaves'





class Sequelizemeta(models.Model):

    name = models.CharField(primary_key=True, max_length=255)



    class Meta:

        managed = False

        db_table = 'sequelizemeta'





class Squadmembers(models.Model):

    keyid = models.CharField(db_column='KeyID', primary_key=True, max_length=36, db_collation='utf8mb4_bin')  # Field name made lowercase.

    role = models.CharField(max_length=255, blank=True, null=True)

    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.

    squadid = models.ForeignKey('Squads', models.DO_NOTHING, db_column='squadID', blank=True, null=True)  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'squadmembers'





class Squads(models.Model):

    squadid = models.CharField(db_column='squadID', primary_key=True, max_length=36, db_collation='utf8mb4_bin')  # Field name made lowercase.

    squadname = models.CharField(max_length=255, blank=True, null=True)

    departmentid = models.CharField(db_column='departmentID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    companyid = models.CharField(db_column='companyID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'squads'





class Tokens(models.Model):

    tokenid = models.CharField(primary_key=True, max_length=36, db_collation='utf8mb4_bin')

    username = models.CharField(max_length=255, blank=True, null=True)

    accesstoken = models.CharField(db_column='accessToken', max_length=255, blank=True, null=True)  # Field name made lowercase.

    refreshtoken = models.CharField(db_column='refreshToken', max_length=255, blank=True, null=True)  # Field name made lowercase.

    accesstokenexpiry = models.DateTimeField(db_column='accessTokenExpiry', blank=True, null=True)  # Field name made lowercase.

    refreshexpiry = models.DateTimeField(db_column='refreshExpiry', blank=True, null=True)  # Field name made lowercase.

    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'tokens'





class Users(models.Model):

    keyid = models.CharField(db_column='KeyID', primary_key=True, max_length=36, db_collation='utf8mb4_bin')  # Field name made lowercase.

    firstname = models.CharField(db_column='firstName', max_length=255)  # Field name made lowercase.

    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.

    username = models.CharField(unique=True, max_length=255)

    password = models.CharField(max_length=255)

    departmentid = models.CharField(db_column='departmentID', max_length=36)  # Field name made lowercase.

    companyid = models.CharField(db_column='companyID', max_length=36)  # Field name made lowercase.

    positionid = models.CharField(db_column='positionID', max_length=36)  # Field name made lowercase.

    age = models.CharField(max_length=255)

    birthday = models.DateTimeField()

    startofworkday = models.DateTimeField(db_column='startOfWorkday')  # Field name made lowercase.

    phonenumber = models.CharField(db_column='phoneNumber', unique=True, max_length=255)  # Field name made lowercase.

    address = models.CharField(max_length=255)

    email = models.CharField(unique=True, max_length=255)

    role = models.CharField(max_length=255)

    status = models.CharField(max_length=255)

    imgprofile = models.CharField(db_column='imgProfile', max_length=255)  # Field name made lowercase.

    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'users'

