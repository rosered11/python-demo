# Implement Model Auth in Python

## UserManager

Should will create class usermanager first,it use for manage user.

```python
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and save a new user"""
        user = self.models(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
```

the extra_fields use for add anothor fields,it don't have the fields in model.

```python
def create_user(self, email, password=None, **extra_fields):
```

## User Model

When need to custom model

```python
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that support using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
```

By default the model will default the username field

We will customize that to email field.

So we can use an email address

```python
USERNAME_FIELD = 'email'
```

And, then

Go to the file settings.py

Append this code

```python
AUTH_USER_MODEL = '{your-custom-user-model}'
```

And, then

You try to run migrations follow this command

`python manage.py makemigrations {your-module}`
