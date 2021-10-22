from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, id, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not id:
            raise ValueError('El usuario debe tener un numero de identificación')
        user = self.model(id=id)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            id=id,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuarios(AbstractBaseUser, PermissionsMixin):
    id = models.IntegerField(primary_key=True)
    password = models.CharField('Password', max_length=255)
    rol = models.CharField('Rol', max_length=45)
    nombre = models.CharField('Nombre', max_length=15)
    apellidos = models.CharField('Apellidos', max_length=15)
    email = models.EmailField('Email', max_length=100)
    estado = models.CharField('Estado', max_length=45)
    telefono_viajero = models.IntegerField('Telefono')

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'id'
