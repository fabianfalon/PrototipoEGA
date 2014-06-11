# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from PIL import Image


# class UserManager(BaseUserManager):

# 	def _create_user(self, username, email, password, is_staff,
# 			is_superuser, **extra_fields):
# 		if not email:
# 			raise ValueError('el email debe ser obligado')
# 		email = self.normalize_email(email)
# 		user = self.model(username=username, email=email, is_active=True,
# 				is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
# 		user.set_password(password)
# 		user.save(using = self._db)
# 		return user

# 	def create_user(self, username, email, password=None, **extra_fields):
# 		return self._create_user(username, email, password, False, False,**extra_fields)

# 	def create_superuser(self, username, email, password, **extra_fields):
# 		return self._create_user(username, email, password, True, True, **extra_fields)



# class User(AbstractBaseUser,PermissionsMixin):

# 	username = models.CharField(max_length=50, unique=True)
# 	email = models.EmailField(max_length=50, unique=True)
# 	apellido_nombre = models.CharField(max_length=50)
# 	carrera = models.CharField(max_length=50)
# 	dni = models.CharField(max_length=10)
# 	ciudad_actual = models.CharField(max_length=500)
# 	domicilio_actual = models.CharField(max_length=500)
# 	fecha_nacimiento = models.DateField()
# 	cod_alumno = models.IntegerField(blank=True, null=True)
# 	tipo_usuario = models.IntegerField(blank=True, null=True)
# 	documentacion_completa = models.BooleanField(default=False)
# 	fecha = models.DateField(auto_now=True, auto_now_add=True)
# 	perfil = models.ImageField(upload_to='alumnos/', blank=True, null=True)
	

# 	objects = UserManager()

# 	is_active = models.BooleanField(default= True)
# 	is_staff = models.BooleanField(default= False)

# 	USERNAME_FIELD = 'username'
# 	REQUIRED_FIELDS = ['email']

# 	def get_short_name(self):
# 		return self.username

