from __future__ import unicode_literals

from django.db import models


class BtcUser(models.Model):
    user_id = models.IntegerField(unique=True, blank=True, null=True)
    pubadd = models.CharField(unique=True, max_length=64, blank=True, null=True)
    privkey = models.CharField(max_length=64, blank=True, null=True)
    publickey = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'btc_user'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class EthUser(models.Model):
    user_id = models.IntegerField(unique=True, blank=True, null=True)
    pubadd = models.CharField(unique=True, max_length=64, blank=True, null=True)
    privkey = models.CharField(max_length=64, blank=True, null=True)
    publickey = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eth_user'
