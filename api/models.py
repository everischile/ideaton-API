# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    commune = models.CharField(max_length=50, blank=True)
    age = models.PositiveIntegerField(default=0, blank=True)
    is_student = models.BooleanField(default=False)
    career = models.CharField(max_length=60, blank=True)
    university = models.CharField(max_length=60, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name


class Category(models.Model):
    cat_name = models.TextField()

    def __unicode__(self):
        return self.cat_name


class Idea(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField(max_length=400)
    url_video = models.URLField(max_length=500, blank=False)
    num_vote = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    main_image = models.ImageField(upload_to='imagenes_principales/',
                                    default='', blank=False)

    def __unicode__(self):
        return self.title


class Vote(models.Model):
    user = models.ForeignKey(User)
    idea = models.ForeignKey(Idea)

    class Meta:
        unique_together = (('user', 'idea'), )

    def __unicode__(self):
        return u'{} votó {}'.format(
            self.user.username, self.idea.titulo)


class Commentary(models.Model):
    user = models.ForeignKey(User)
    idea = models.ForeignKey(Idea)
    commentary = models.TextField(max_length=500)

    def __unicode__(self):
        return u'{} Comentó {}'.format(
            self.user.username, self.idea.titulo, self.commentary)


class Image(models.Model):
    idea = models.ForeignKey(Idea)
    image = models.ImageField(upload_to='imagenes_ideas/',
                               default='', blank=True)

    def __unicode__(self):
        return u'{} Tiene  {}'.format(
            self.idea.title, self.image)

