from django.db import models
from django.db.models.manager import Manager


class User(models.Model):
    name = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_block = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AdminManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)


# 관리자용
class Admin(User):
    objects = AdminManager()

    def __str__(self):
        return f'{self.name} (관리자)'

    @staticmethod
    def drop(self, user):
        user.delete()


class StaffManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)


# 일반유저용
class Staff(User):
    class Meta:
        proxy = True

    def __str__(self):
        return f'{self.name} (스태프)'

    @staticmethod
    def block(self, user):
        user.is_block = True
        user.save()
