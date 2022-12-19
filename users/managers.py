from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, username, password, email, role=None, name=None,  **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not username:
            raise ValueError(('The Username must be set'))
        user = self.model(username=username, email=email, name=name,
                          role=role,  **extra_fields)
        print(user)
        user.set_password(password)
        print(user.password)
        user.save()
        return user

    def create_superuser(self, username, password, email, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, email, 'admin', **extra_fields)
