from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManage(BaseUserManager): #clase que tiene las operaciones para crear un nuevo usuario y tambien un superadminusuario
    def create_user(self, first_name, last_name, username, email, password=None,):
        if not email:
            raise ValueError('el usuario debe tener email')
        
        if not username:
            raise ValueError('el usuario debe tener un username')
        
        user = self.model(                         #creando usuario
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,

        )

        user.set_password(password) #password
        user.save(using=self._db) #insertar el valor en la BD
        return user


    def create_superuser(self, first_name, last_name, email, username, password):#crear super usuario
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,       
        )    

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser): #crear modelo de la clase account
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    #campos atributos de django
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' #para que el usuario inicie sesion son su email y no con su username como esta configurado en django
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] #indicarle que campos son requeridos para el nuevo usuario


    objects = MyAccountManage()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
