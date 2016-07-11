from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user_id = models.PositiveIntegerField(verbose_name = 'связка с ID из users')
    type_profile = models.CharField(verbose_name='тип профиля', max_length=32)
    link = models.URLField(verbose_name='ссылка на личный сайт', max_length=90)
    about_me = models.TextField(verbose_name = 'коротко о себе')
    avatar = models.CharField(verbose_name='путь до картинки', max_length=32)


class UserAlboms(models.Model):
    id_user_profile = models.ForeignKey(UserProfile, verbose_name = 'связка с ID из users_profile')
    albom_name = models.CharField(verbose_name='название альбома', max_length=32)
    albom_catefory = models.CharField(verbose_name='категория альбома', max_length=32)
    # albom_date = models.DateField(verbose_name = 'дата создания')


class AlbomPhotos(models.Model):
    id_albom = models.ForeignKey(UserProfile, verbose_name = 'связка с ID из UsersAlbom')
    # photo_date = models.DateField(verbose_name='дата создания')
    photo_name = models.CharField(verbose_name='название фото', max_length=32)
    photo_pol = models.PositiveIntegerField(verbose_name = 'голоса за фото')


