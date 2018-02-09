from django.db import models
from django.db.models import Manager


class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#커스텀 매니저
class NewManager(Manager):
    def get_query(self):
        print('NewMAnager get_queryset')
        return super().get_queryset()

#커스텀 매니저를 직접 자기 속성으로 갖는 MyPerson1
class MyPerson1(Person):
    class Meta:
        proxy = True

#커스텀 매니저를 속성으로 갖는 ABC Model
class ExtraManagerModel(models.Model):
    secondary = NewManager()

#커스텀 매니저를 갖는 ABC 모델을 상속받은 MyPErson2
#간접적으로 secondary라는 Manager를 갖게
class MyPerson2(Person):
    class Meta:
        proxy = True
