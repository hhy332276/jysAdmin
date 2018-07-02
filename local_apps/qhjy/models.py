from __future__ import unicode_literals

from django.db import models


class QhAdmin(models.Model):
    user_name = models.CharField(unique=True, max_length=255)
    user_pwd = models.CharField(max_length=32)
    access_token = models.CharField(max_length=255)
    last_login_time = models.IntegerField()
    last_login_addr = models.CharField(max_length=255)
    client_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qh_admin'


class QhBetting(models.Model):
    user_id = models.IntegerField()
    tw_qh_coin = models.IntegerField()
    nper_id = models.IntegerField()
    type = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=6)
    add_time = models.IntegerField()
    is_true = models.IntegerField()
    poundage = models.DecimalField(max_digits=18, decimal_places=10)
    rate = models.DecimalField(max_digits=7, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'qh_betting'


class QhBettingFalse(models.Model):
    user_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=18, decimal_places=8)
    type = models.IntegerField()
    coin_id = models.IntegerField()
    nper_id = models.IntegerField()
    rate = models.DecimalField(max_digits=18, decimal_places=8)
    add_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'qh_betting_false'


class QhConfig(models.Model):
    is_open = models.IntegerField()
    next_open_time = models.CharField(max_length=20)
    rate = models.DecimalField(max_digits=8, decimal_places=5)
    max_betting_price = models.DecimalField(max_digits=15, decimal_places=7)
    min_betting_price = models.DecimalField(max_digits=15, decimal_places=7)
    max_flat_deviation = models.DecimalField(max_digits=18, decimal_places=8, blank=True, null=True)
    min_flat_deviation = models.DecimalField(max_digits=18, decimal_places=8, blank=True, null=True)
    btc_error = models.DecimalField(max_digits=18, decimal_places=8, blank=True, null=True)
    eth_error = models.DecimalField(max_digits=18, decimal_places=8, blank=True, null=True)
    open_success = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'qh_config'


class QhNper(models.Model):
    nper = models.IntegerField()
    open_time = models.IntegerField()
    add_time = models.IntegerField()
    coin_id = models.IntegerField()
    result = models.IntegerField()
    is_current = models.IntegerField()
    up_rate = models.DecimalField(max_digits=28, decimal_places=18, blank=True, null=True)
    down_rate = models.DecimalField(max_digits=28, decimal_places=18, blank=True, null=True)
    flat_rate = models.DecimalField(max_digits=28, decimal_places=18, blank=True, null=True)
    result_rate = models.DecimalField(max_digits=28, decimal_places=18, blank=True, null=True)
    stop_time = models.IntegerField()
    end_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'qh_nper'


class QhPvuv(models.Model):
    ip = models.CharField(max_length=30)
    click = models.IntegerField()
    type = models.CharField(max_length=10)
    time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'qh_pvuv'


class QhQueue(models.Model):
    open_time = models.CharField(max_length=255)
    stop_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'qh_queue'


class QhResult(models.Model):
    nper_id = models.IntegerField()
    coin_id = models.IntegerField()
    exchange_name = models.CharField(max_length=255)
    open_time_price = models.DecimalField(max_digits=15, decimal_places=8)
    end_time_price = models.DecimalField(max_digits=15, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'qh_result'


class QhResultPeople(models.Model):
    nper_id = models.IntegerField()
    coin_id = models.IntegerField()
    exchange_name = models.CharField(max_length=255)
    open_time_price = models.DecimalField(max_digits=15, decimal_places=8)
    end_time_price = models.DecimalField(max_digits=15, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'qh_result_people'


class QhRyb(models.Model):
    message = models.CharField(max_length=255)
    add_time = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'qh_ryb'


class QhTv(models.Model):
    coinid = models.IntegerField(db_column='coinId', blank=True, null=True)  # Field name made lowercase.
    exchangename = models.IntegerField(db_column='exchangeName', blank=True, null=True)  # Field name made lowercase.
    price = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    createtime = models.CharField(db_column='createTime', max_length=64, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='endTime', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qh_tv'


class Qijia(models.Model):
    url = models.CharField(max_length=64, blank=True, null=True)
    cointype = models.IntegerField(db_column='coinType', blank=True, null=True)  # Field name made lowercase.
    name = models.IntegerField(blank=True, null=True)
    price = models.CharField(max_length=32, blank=True, null=True)
    inserttime = models.IntegerField(db_column='insertTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qijia'