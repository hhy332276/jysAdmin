from __future__ import unicode_literals

from django.db import models


class BfAdmin(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=16)
    nickname = models.CharField(max_length=50)
    moble = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    last_login_time = models.IntegerField()
    last_login_ip = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_admin'


class BfAdver(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    look = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_adver'


class BfArticle(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    adminid = models.IntegerField()
    type = models.CharField(max_length=100)
    hits = models.IntegerField()
    footer = models.IntegerField()
    index = models.IntegerField()
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    img = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'bf_article'


class BfArticleType(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    remark = models.CharField(max_length=50)
    index = models.CharField(max_length=50)
    footer = models.CharField(max_length=50)
    shang = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_article_type'


class BfAuthExtend(models.Model):
    group_id = models.IntegerField()
    extend_id = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_auth_extend'
        unique_together = (('group_id', 'extend_id', 'type'),)


class BfAuthGroup(models.Model):
    module = models.CharField(max_length=20)
    type = models.IntegerField()
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=80)
    status = models.IntegerField()
    rules = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'bf_auth_group'


class BfAuthGroupAccess(models.Model):
    uid = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_auth_group_access'
        unique_together = (('uid', 'group_id'),)


class BfAuthRule(models.Model):
    module = models.CharField(max_length=20)
    type = models.IntegerField()
    name = models.CharField(max_length=80)
    title = models.CharField(max_length=20)
    status = models.IntegerField()
    condition = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'bf_auth_rule'


class BfCandyLog(models.Model):
    adminid = models.IntegerField()
    adminname = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=20, decimal_places=6)
    addtime = models.IntegerField()
    realnum = models.DecimalField(max_digits=20, decimal_places=6)
    person = models.IntegerField()
    coinname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'bf_candy_log'


class BfCandyReward(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=20, decimal_places=6)
    addtime = models.IntegerField()
    coinname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'bf_candy_reward'


class BfCoin(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    img = models.CharField(max_length=100)
    sort = models.IntegerField()
    fee_bili = models.CharField(max_length=50)
    endtime = models.IntegerField()
    addtime = models.IntegerField()
    status = models.IntegerField()
    fee_meitian = models.CharField(max_length=200)
    dj_zj = models.CharField(max_length=200)
    dj_dk = models.CharField(max_length=200)
    dj_yh = models.CharField(max_length=200)
    dj_mm = models.CharField(max_length=200)
    zr_zs = models.CharField(max_length=50)
    zr_jz = models.CharField(max_length=50)
    zr_dz = models.CharField(max_length=50)
    zr_sm = models.CharField(max_length=50)
    zc_sm = models.CharField(max_length=50)
    zc_fee = models.DecimalField(max_digits=12, decimal_places=5)
    zc_user = models.CharField(max_length=50)
    zc_min = models.DecimalField(max_digits=20, decimal_places=5)
    zc_max = models.DecimalField(max_digits=20, decimal_places=5)
    zc_jz = models.CharField(max_length=50)
    zc_zd = models.CharField(max_length=50)
    js_yw = models.CharField(max_length=50)
    js_sm = models.TextField(blank=True, null=True)
    js_qb = models.CharField(max_length=50)
    js_ym = models.CharField(max_length=50)
    js_gw = models.CharField(max_length=50)
    js_lt = models.CharField(max_length=50)
    js_wk = models.CharField(max_length=50)
    cs_yf = models.CharField(max_length=50)
    cs_sf = models.CharField(max_length=50)
    cs_fb = models.CharField(max_length=50)
    cs_qk = models.CharField(max_length=50)
    cs_zl = models.CharField(max_length=50)
    cs_cl = models.CharField(max_length=50)
    cs_zm = models.DecimalField(max_digits=20, decimal_places=6)
    cs_nd = models.CharField(max_length=50)
    cs_jl = models.CharField(max_length=50)
    cs_ts = models.CharField(max_length=50)
    cs_bz = models.CharField(max_length=50)
    tp_zs = models.CharField(max_length=50)
    tp_js = models.CharField(max_length=50)
    tp_yy = models.CharField(max_length=50)
    tp_qj = models.CharField(max_length=50)
    sh_zd = models.IntegerField()
    dj_zj_mytx = models.CharField(max_length=200, blank=True, null=True)
    dj_dk_mytx = models.CharField(max_length=200, blank=True, null=True)
    dj_yh_mytx = models.CharField(max_length=200, blank=True, null=True)
    dj_mm_mytx = models.CharField(max_length=200, blank=True, null=True)
    zc_fee_bili = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ranking = models.IntegerField(blank=True, null=True)
    js_qk = models.CharField(max_length=50)
    js_bp = models.CharField(max_length=50)
    js_zcp = models.CharField(max_length=11)
    js_en = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bf_coin'


class BfCoinJson(models.Model):
    name = models.CharField(max_length=100)
    data = models.CharField(max_length=500)
    type = models.CharField(max_length=100)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_coin_json'


class BfConfig(models.Model):
    footer_logo = models.CharField(max_length=200)
    huafei_zidong = models.CharField(max_length=200)
    kefu = models.CharField(max_length=200)
    huafei_openid = models.CharField(max_length=200)
    huafei_appkey = models.CharField(max_length=200)
    index_lejimum = models.CharField(max_length=200)
    login_verify = models.CharField(max_length=200)
    fee_meitian = models.CharField(max_length=200)
    top_name = models.CharField(max_length=200)
    web_name = models.CharField(max_length=200)
    web_title = models.CharField(max_length=200)
    web_logo = models.CharField(max_length=200)
    web_llogo_small = models.CharField(max_length=200)
    web_keywords = models.CharField(max_length=200, blank=True, null=True)
    web_description = models.CharField(max_length=200, blank=True, null=True)
    web_close = models.CharField(max_length=255, blank=True, null=True)
    web_close_cause = models.CharField(max_length=255, blank=True, null=True)
    web_icp = models.CharField(max_length=255, blank=True, null=True)
    web_cnzz = models.CharField(max_length=255, blank=True, null=True)
    web_ren = models.CharField(max_length=255, blank=True, null=True)
    web_reg = models.TextField(blank=True, null=True)
    market_mr = models.CharField(max_length=255, blank=True, null=True)
    xnb_mr = models.CharField(max_length=255, blank=True, null=True)
    rmb_mr = models.CharField(max_length=255, blank=True, null=True)
    web_waring = models.CharField(max_length=255, blank=True, null=True)
    moble_type = models.CharField(max_length=255, blank=True, null=True)
    moble_url = models.CharField(max_length=255, blank=True, null=True)
    moble_user = models.CharField(max_length=255, blank=True, null=True)
    moble_pwd = models.CharField(max_length=255, blank=True, null=True)
    contact_moble = models.CharField(max_length=255, blank=True, null=True)
    contact_weibo = models.TextField(blank=True, null=True)
    contact_tqq = models.TextField(blank=True, null=True)
    contact_qq = models.TextField(blank=True, null=True)
    contact_qqun = models.TextField(blank=True, null=True)
    contact_weixin = models.TextField(blank=True, null=True)
    contact_weixin_img = models.TextField(blank=True, null=True)
    contact_email = models.TextField(blank=True, null=True)
    contact_alipay = models.TextField(blank=True, null=True)
    contact_alipay_img = models.TextField(blank=True, null=True)
    contact_bank = models.TextField(blank=True, null=True)
    user_truename = models.TextField(blank=True, null=True)
    user_moble = models.TextField(blank=True, null=True)
    user_alipay = models.TextField(blank=True, null=True)
    user_bank = models.TextField(blank=True, null=True)
    user_text_truename = models.TextField(blank=True, null=True)
    user_text_moble = models.TextField(blank=True, null=True)
    user_text_alipay = models.TextField(blank=True, null=True)
    user_text_bank = models.TextField(blank=True, null=True)
    user_text_log = models.TextField(blank=True, null=True)
    user_text_password = models.TextField(blank=True, null=True)
    user_text_paypassword = models.TextField(blank=True, null=True)
    mytx_min = models.TextField(blank=True, null=True)
    mytx_max = models.TextField(blank=True, null=True)
    mytx_bei = models.TextField(blank=True, null=True)
    mytx_coin = models.TextField(blank=True, null=True)
    mytx_fee_min = models.FloatField(blank=True, null=True)
    mytx_fee = models.TextField(blank=True, null=True)
    trade_min = models.TextField(blank=True, null=True)
    trade_max = models.TextField(blank=True, null=True)
    trade_limit = models.TextField(blank=True, null=True)
    trade_text_log = models.TextField(blank=True, null=True)
    issue_ci = models.TextField(blank=True, null=True)
    issue_jian = models.TextField(blank=True, null=True)
    issue_min = models.TextField(blank=True, null=True)
    issue_max = models.TextField(blank=True, null=True)
    money_min = models.TextField(blank=True, null=True)
    money_max = models.TextField(blank=True, null=True)
    money_bei = models.TextField(blank=True, null=True)
    money_text_index = models.TextField(blank=True, null=True)
    money_text_log = models.TextField(blank=True, null=True)
    money_text_type = models.TextField(blank=True, null=True)
    invit_type = models.TextField(blank=True, null=True)
    invit_fee1 = models.TextField(blank=True, null=True)
    invit_fee2 = models.TextField(blank=True, null=True)
    invit_fee3 = models.TextField(blank=True, null=True)
    invit_text_txt = models.TextField(blank=True, null=True)
    invit_text_log = models.TextField(blank=True, null=True)
    index_notice_1 = models.TextField(blank=True, null=True)
    index_notice_11 = models.TextField(blank=True, null=True)
    index_notice_2 = models.TextField(blank=True, null=True)
    index_notice_22 = models.TextField(blank=True, null=True)
    index_notice_3 = models.TextField(blank=True, null=True)
    index_notice_33 = models.TextField(blank=True, null=True)
    index_notice_4 = models.TextField(blank=True, null=True)
    index_notice_44 = models.TextField(blank=True, null=True)
    text_footer = models.TextField(blank=True, null=True)
    shop_text_index = models.TextField(blank=True, null=True)
    shop_text_log = models.TextField(blank=True, null=True)
    shop_text_addr = models.TextField(blank=True, null=True)
    shop_text_view = models.TextField(blank=True, null=True)
    huafei_text_index = models.DecimalField(max_digits=10, decimal_places=4)
    huafei_text_log = models.TextField(blank=True, null=True)
    addtime = models.IntegerField()
    status = models.IntegerField()
    shop_coin = models.CharField(max_length=200)
    shop_logo = models.CharField(max_length=200)
    shop_login = models.CharField(max_length=200)
    index_html = models.CharField(max_length=50)
    trade_hangqing = models.CharField(max_length=50)
    trade_moshi = models.CharField(max_length=50)
    mytx_day_max = models.DecimalField(max_digits=13, decimal_places=0)
    en_web_reg = models.TextField(blank=True, null=True)
    tui_jy_jl = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True)
    before_cpc = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    rank_num = models.IntegerField(blank=True, null=True)
    ethaddress = models.CharField(max_length=100, blank=True, null=True)
    ethpassword = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bf_config'


class BfDaohang(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    entitle = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bf_daohang'


class BfEthHash(models.Model):
    ethhash = models.CharField(unique=True, max_length=100)
    address = models.CharField(max_length=100)
    addtime = models.IntegerField()
    isdeal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bf_eth_hash'


class BfEthTransfer(models.Model):
    zc_addr = models.CharField(max_length=100)
    zr_addr = models.CharField(max_length=100)
    zc_amount = models.DecimalField(max_digits=20, decimal_places=8)
    addtime = models.IntegerField()
    zchash = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'bf_eth_transfer'


class BfFeedback(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    addtime = models.IntegerField()
    endtime = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=50)
    attachone = models.CharField(max_length=200, blank=True, null=True)
    attachtwo = models.CharField(max_length=200, blank=True, null=True)
    userid = models.IntegerField()
    username = models.CharField(max_length=50)
    isread = models.IntegerField()
    txid = models.CharField(max_length=100, blank=True, null=True)
    freshtime = models.IntegerField(blank=True, null=True)
    userstatus = models.IntegerField(blank=True, null=True)
    adminstatus = models.IntegerField(blank=True, null=True)
    recordno = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'bf_feedback'


class BfFinance(models.Model):
    userid = models.IntegerField()
    coinname = models.CharField(max_length=50)
    num_a = models.DecimalField(max_digits=20, decimal_places=8)
    num_b = models.DecimalField(max_digits=20, decimal_places=8)
    num = models.DecimalField(max_digits=20, decimal_places=8)
    fee = models.DecimalField(max_digits=20, decimal_places=8)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    nameid = models.IntegerField()
    remark = models.CharField(max_length=50)
    mum_a = models.DecimalField(max_digits=20, decimal_places=8)
    mum_b = models.DecimalField(max_digits=20, decimal_places=8)
    mum = models.DecimalField(max_digits=20, decimal_places=8)
    move = models.CharField(max_length=50)
    addtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_finance'


class BfFinanceLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    adminname = models.CharField(max_length=50, blank=True, null=True)
    addtime = models.IntegerField()
    plusminus = models.IntegerField()
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    description = models.CharField(max_length=100, blank=True, null=True)
    optype = models.IntegerField()
    cointype = models.IntegerField()
    old_amount = models.DecimalField(max_digits=20, decimal_places=8)
    new_amount = models.DecimalField(max_digits=20, decimal_places=8)
    userid = models.IntegerField()
    adminid = models.IntegerField()
    addip = models.CharField(max_length=100)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_finance_log'


class BfFooter(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    remark = models.CharField(max_length=50)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_footer'


class BfGrade(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True)
    fee = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    need_cpc = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bf_grade'


class BfGradeLog(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    gid = models.IntegerField(blank=True, null=True)
    mouth = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    addtime = models.IntegerField(blank=True, null=True)
    endtime = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    style = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bf_grade_log'


class BfIncentive(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=20, decimal_places=6)
    addtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_incentive'


class BfIncentiveLog(models.Model):
    adminid = models.IntegerField()
    admin = models.CharField(max_length=200)
    amount = models.IntegerField()
    addtime = models.IntegerField()
    realnum = models.DecimalField(max_digits=20, decimal_places=6)
    person = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_incentive_log'


class BfInvit(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.IntegerField()
    invit = models.IntegerField()
    name = models.IntegerField()
    type = models.IntegerField()
    num = models.DecimalField(max_digits=20, decimal_places=8)
    mum = models.DecimalField(max_digits=20, decimal_places=8)
    fee = models.DecimalField(max_digits=20, decimal_places=8)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    buysell = models.IntegerField()
    orderno = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bf_invit'


class BfLink(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    mytx = models.CharField(max_length=100)
    remark = models.CharField(max_length=50)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    look_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_link'


class BfMarket(models.Model):
    name = models.CharField(max_length=50)
    round = models.CharField(max_length=255)
    fee_buy = models.CharField(max_length=255)
    fee_sell = models.CharField(max_length=255)
    buy_min = models.CharField(max_length=255)
    buy_max = models.CharField(max_length=255)
    sell_min = models.CharField(max_length=255)
    sell_max = models.CharField(max_length=255)
    trade_min = models.CharField(max_length=255)
    trade_max = models.CharField(max_length=255)
    invit_buy = models.CharField(max_length=50)
    invit_sell = models.CharField(max_length=50)
    invit_1 = models.CharField(max_length=50)
    invit_2 = models.CharField(max_length=50)
    invit_3 = models.CharField(max_length=50)
    zhang = models.CharField(max_length=255)
    die = models.CharField(max_length=255)
    hou_price = models.CharField(max_length=255)
    tendency = models.TextField(blank=True, null=True)
    trade = models.IntegerField()
    new_price = models.DecimalField(max_digits=20, decimal_places=8)
    buy_price = models.DecimalField(max_digits=20, decimal_places=8)
    sell_price = models.DecimalField(max_digits=20, decimal_places=8)
    min_price = models.DecimalField(max_digits=20, decimal_places=8)
    max_price = models.DecimalField(max_digits=20, decimal_places=8)
    volume = models.DecimalField(max_digits=20, decimal_places=8)
    change = models.DecimalField(max_digits=20, decimal_places=8)
    api_min = models.DecimalField(max_digits=20, decimal_places=8)
    api_max = models.DecimalField(max_digits=20, decimal_places=8)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    start_time = models.IntegerField(blank=True, null=True)
    stop_time = models.IntegerField(blank=True, null=True)
    start_minute = models.IntegerField(blank=True, null=True)
    stop_minute = models.IntegerField(blank=True, null=True)
    agree6 = models.IntegerField(blank=True, null=True)
    agree7 = models.IntegerField(blank=True, null=True)
    trade_num_min = models.CharField(max_length=30)
    is_zhu = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_market'


class BfMarketJson(models.Model):
    name = models.CharField(max_length=100)
    data = models.CharField(max_length=500)
    type = models.CharField(max_length=100)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_market_json'


class BfMenu(models.Model):
    title = models.CharField(max_length=50)
    pid = models.IntegerField()
    sort = models.IntegerField()
    url = models.CharField(max_length=255)
    hide = models.IntegerField()
    tip = models.CharField(max_length=255)
    group = models.CharField(max_length=50, blank=True, null=True)
    is_dev = models.IntegerField()
    ico_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'bf_menu'


class BfMycz(models.Model):
    userid = models.IntegerField()
    num = models.DecimalField(max_digits=11, decimal_places=2)
    mum = models.DecimalField(max_digits=11, decimal_places=2)
    type = models.CharField(max_length=50)
    tradeno = models.CharField(max_length=50)
    remark = models.CharField(max_length=250)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    alipay_truename = models.CharField(max_length=20, blank=True, null=True)
    alipay_account = models.CharField(max_length=35, blank=True, null=True)
    ewmname = models.CharField(max_length=50)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    bank = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bf_mycz'


class BfMyczInvit(models.Model):
    userid = models.IntegerField()
    invitid = models.IntegerField()
    num = models.DecimalField(max_digits=20, decimal_places=2)
    fee = models.DecimalField(max_digits=20, decimal_places=8)
    coinname = models.CharField(max_length=50)
    mum = models.DecimalField(max_digits=20, decimal_places=8)
    remark = models.CharField(max_length=250)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_mycz_invit'


class BfMyczType(models.Model):
    max = models.CharField(max_length=200)
    min = models.CharField(max_length=200)
    kaihu = models.CharField(max_length=200)
    truename = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    img = models.CharField(max_length=50)
    extra = models.CharField(max_length=50)
    remark = models.CharField(max_length=50)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'bf_mycz_type'


class BfMytx(models.Model):
    userid = models.IntegerField()
    num = models.IntegerField()
    fee = models.DecimalField(max_digits=20, decimal_places=2)
    mum = models.DecimalField(max_digits=20, decimal_places=2)
    truename = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    bank = models.CharField(max_length=250)
    bankprov = models.CharField(max_length=50)
    bankcity = models.CharField(max_length=50)
    bankaddr = models.CharField(max_length=50)
    bankcard = models.CharField(max_length=200)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_mytx'


class BfMyzc(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=200)
    coinname = models.CharField(max_length=200)
    txid = models.CharField(max_length=200)
    num = models.DecimalField(max_digits=20, decimal_places=8)
    fee = models.DecimalField(max_digits=20, decimal_places=8)
    mum = models.DecimalField(max_digits=20, decimal_places=8)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    to_user = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_myzc'


class BfMyzcFee(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=200)
    coinname = models.CharField(max_length=200)
    txid = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    fee = models.DecimalField(max_digits=20, decimal_places=8)
    num = models.DecimalField(max_digits=20, decimal_places=8)
    mum = models.DecimalField(max_digits=20, decimal_places=8)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_myzc_fee'


class BfMyzr(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=200)
    coinname = models.CharField(max_length=200)
    txid = models.CharField(max_length=200)
    num = models.DecimalField(max_digits=20, decimal_places=8)
    mum = models.DecimalField(max_digits=20, decimal_places=8)
    fee = models.DecimalField(max_digits=20, decimal_places=8)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    from_user = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_myzr'


class BfMyzrJson(models.Model):
    id = models.BigAutoField(primary_key=True)
    addtime = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    coinname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'bf_myzr_json'


class BfRegPrize(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=55)
    addtime = models.IntegerField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    childuid = models.IntegerField()
    childuname = models.CharField(max_length=55)
    coinid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_reg_prize'


class BfTrade(models.Model):
    userid = models.IntegerField()
    market = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    num = models.DecimalField(max_digits=20, decimal_places=8)
    deal = models.DecimalField(max_digits=20, decimal_places=8)
    mum = models.DecimalField(max_digits=20, decimal_places=8)
    fee = models.DecimalField(max_digits=20, decimal_places=8)
    type = models.IntegerField()
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    feerate_buy = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    feerate_sell = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bf_trade'


class BfTradeJson(models.Model):
    market = models.CharField(max_length=100)
    data = models.CharField(max_length=500)
    type = models.CharField(max_length=100)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_trade_json'


class BfTradeJsonCopy(models.Model):
    market = models.CharField(max_length=100)
    data = models.CharField(max_length=500)
    type = models.CharField(max_length=100)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_trade_json_copy'


class BfTradeLog(models.Model):
    userid = models.IntegerField()
    peerid = models.IntegerField()
    market = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    num = models.DecimalField(max_digits=20, decimal_places=8)
    mum = models.DecimalField(max_digits=20, decimal_places=8)
    fee_buy = models.DecimalField(max_digits=20, decimal_places=8)
    fee_sell = models.DecimalField(max_digits=20, decimal_places=8)
    type = models.IntegerField()
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_trade_log'


class BfTradePrize(models.Model):
    cpc = models.FloatField()
    trade_sum = models.DecimalField(max_digits=20, decimal_places=6)
    addtime = models.IntegerField()
    userid = models.IntegerField()
    username = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'bf_trade_prize'


class BfTradeSum(models.Model):
    addtime = models.IntegerField()
    amount = models.DecimalField(max_digits=20, decimal_places=1)
    prizesum = models.DecimalField(max_digits=20, decimal_places=6)
    history_prize = models.DecimalField(max_digits=20, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'bf_trade_sum'


class BfUser(models.Model):
    username = models.CharField(unique=True, max_length=50)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    mobiletime = models.IntegerField()
    password = models.CharField(max_length=32)
    tpwdsetting = models.CharField(max_length=32)
    paypassword = models.CharField(max_length=50, blank=True, null=True)
    invit_1 = models.CharField(max_length=50)
    invit_2 = models.CharField(max_length=50)
    invit_3 = models.CharField(max_length=50)
    truename = models.CharField(max_length=32, blank=True, null=True)
    idcard = models.CharField(max_length=32, blank=True, null=True)
    logins = models.IntegerField()
    ga = models.CharField(max_length=50, blank=True, null=True)
    addip = models.CharField(max_length=50)
    addr = models.CharField(max_length=50)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    email = models.CharField(max_length=50, blank=True, null=True)
    alipay = models.CharField(max_length=50, blank=True, null=True)
    invit = models.CharField(max_length=50, blank=True, null=True)
    token = models.CharField(max_length=50, blank=True, null=True)
    mibao_question = models.CharField(max_length=200, blank=True, null=True)
    mibao_answer = models.CharField(max_length=200, blank=True, null=True)
    zhengjian = models.CharField(max_length=20, blank=True, null=True)
    idcard_zheng = models.CharField(max_length=200, blank=True, null=True)
    idcard_fan = models.CharField(max_length=200, blank=True, null=True)
    findpwd_mibao = models.IntegerField(blank=True, null=True)
    findpaypwd_mibao = models.IntegerField(blank=True, null=True)
    is_agree = models.IntegerField(blank=True, null=True)
    idcard_shouchi = models.CharField(max_length=200, blank=True, null=True)
    ethpassword = models.CharField(max_length=50, blank=True, null=True)
    etcpassword = models.CharField(max_length=50, blank=True, null=True)
    pwd_err = models.IntegerField()
    buy_sum = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    sell_sum = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    cpcprize_sum = models.IntegerField(blank=True, null=True)
    trade_sum = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    gjcode = models.IntegerField()
    enname = models.CharField(max_length=50, blank=True, null=True)
    headimg = models.CharField(max_length=255, blank=True, null=True)
    goodnum = models.IntegerField()
    goodcomm = models.IntegerField()
    jianjie = models.CharField(max_length=255, blank=True, null=True)
    history = models.DecimalField(max_digits=20, decimal_places=8)
    sftime_sum = models.IntegerField()
    first_trade_time = models.IntegerField()
    transact = models.IntegerField()
    xinren = models.TextField(blank=True, null=True)
    pingbi = models.TextField(blank=True, null=True)
    ixinren = models.TextField(blank=True, null=True)
    ipingbi = models.TextField(blank=True, null=True)
    trade_id = models.TextField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    cpcpassword = models.CharField(max_length=100, blank=True, null=True)
    marketid = models.CharField(max_length=55, blank=True, null=True)
    socket_token = models.CharField(max_length=32, blank=True, null=True)
    login_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bf_user'


class BfUserBank(models.Model):
    userid = models.IntegerField()
    name = models.CharField(max_length=200)
    bank = models.CharField(max_length=200)
    bankprov = models.CharField(max_length=200)
    bankcity = models.CharField(max_length=200)
    bankaddr = models.CharField(max_length=200)
    bankcard = models.CharField(max_length=200)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_user_bank'


class BfUserBankType(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    mytx = models.CharField(max_length=200)
    remark = models.CharField(max_length=50)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_user_bank_type'


class BfUserCoin(models.Model):
    userid = models.IntegerField()
    btc = models.DecimalField(max_digits=20, decimal_places=8)
    btcd = models.DecimalField(max_digits=20, decimal_places=8)
    btcb = models.CharField(max_length=200)
    ltc = models.DecimalField(max_digits=20, decimal_places=8)
    ltcd = models.DecimalField(max_digits=20, decimal_places=8)
    ltcb = models.CharField(max_length=200)
    eth = models.DecimalField(max_digits=20, decimal_places=8)
    ethd = models.DecimalField(max_digits=20, decimal_places=8)
    ethb = models.CharField(max_length=200)
    cusd = models.DecimalField(max_digits=20, decimal_places=8)
    cusdd = models.DecimalField(max_digits=20, decimal_places=8)
    usdt = models.DecimalField(max_digits=20, decimal_places=8)
    usdtd = models.DecimalField(max_digits=20, decimal_places=8)
    usdtb = models.CharField(max_length=200)
    bch = models.DecimalField(max_digits=20, decimal_places=8)
    bchd = models.DecimalField(max_digits=20, decimal_places=8)
    bchb = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'bf_user_coin'


class BfUserLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.IntegerField()
    type = models.CharField(max_length=30)
    remark = models.CharField(max_length=50)
    addip = models.CharField(max_length=20)
    addr = models.CharField(max_length=100)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    session_key = models.CharField(max_length=100, blank=True, null=True)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_user_log'


class BfUserLogCopy(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.IntegerField()
    type = models.CharField(max_length=30)
    remark = models.CharField(max_length=50)
    addip = models.CharField(max_length=20)
    addr = models.CharField(max_length=100)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    session_key = models.CharField(max_length=100, blank=True, null=True)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_user_log_copy'


class BfUserQianbao(models.Model):
    userid = models.IntegerField()
    coinname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    addr = models.CharField(max_length=200)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_user_qianbao'


class BfUsercoinClear(models.Model):
    userid = models.IntegerField()
    num = models.DecimalField(max_digits=12, decimal_places=4)
    ctime = models.IntegerField()
    coin = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'bf_usercoin_clear'


class BfVote(models.Model):
    userid = models.IntegerField()
    name = models.CharField(max_length=50)
    type = models.IntegerField()
    sort = models.IntegerField()
    addtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bf_vote'


class BfVoteType(models.Model):
    name = models.CharField(unique=True, max_length=100)
    title = models.CharField(max_length=100)
    status = models.IntegerField()
    zancheng = models.IntegerField()
    fandui = models.IntegerField()
    canyu = models.IntegerField()
    website = models.CharField(max_length=255, blank=True, null=True)
    zsptcoin = models.IntegerField()
    cpccost = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    sort = models.IntegerField()
    userid = models.IntegerField()
    rjreason = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bf_vote_type'


class BfZcbatchError(models.Model):
    zcid = models.IntegerField()
    addtime = models.IntegerField()
    beizhu = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bf_zcbatch_error'


class Transactions(models.Model):
    transaction_hash = models.CharField(unique=True, max_length=100, blank=True, null=True)
    block_hash = models.CharField(max_length=100, blank=True, null=True)
    from_field = models.CharField(db_column='from', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=100, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    gas = models.IntegerField(blank=True, null=True)
    gas_price = models.IntegerField(blank=True, null=True)
    nonce = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'


class TwAdBuy(models.Model):
    id = models.BigAutoField(primary_key=True)
    ad_no = models.CharField(unique=True, max_length=15)
    userid = models.IntegerField()
    location = models.IntegerField()
    currency = models.IntegerField()
    margin = models.DecimalField(max_digits=4, decimal_places=2)
    min_limit = models.DecimalField(max_digits=12, decimal_places=2)
    max_limit = models.DecimalField(max_digits=12, decimal_places=2)
    pay_method = models.CharField(max_length=25)
    message = models.CharField(max_length=500)
    due_time = models.IntegerField()
    safe_option = models.IntegerField()
    trust_only = models.IntegerField()
    open_time = models.CharField(max_length=100)
    add_time = models.IntegerField()
    state = models.IntegerField()
    finished_time = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    coin = models.IntegerField()
    fee = models.DecimalField(max_digits=13, decimal_places=2)
    skaccount = models.CharField(max_length=255, blank=True, null=True)
    deal_bnum = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_ad_buy'


class TwAdSell(models.Model):
    id = models.BigAutoField(primary_key=True)
    ad_no = models.CharField(unique=True, max_length=15)
    userid = models.IntegerField()
    location = models.IntegerField()
    currency = models.IntegerField()
    margin = models.DecimalField(max_digits=4, decimal_places=2)
    min_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    min_limit = models.DecimalField(max_digits=12, decimal_places=2)
    max_limit = models.DecimalField(max_digits=12, decimal_places=2)
    pay_method = models.CharField(max_length=25)
    message = models.CharField(max_length=500)
    safe_option = models.IntegerField()
    trust_only = models.IntegerField()
    open_time = models.CharField(max_length=100)
    add_time = models.IntegerField()
    state = models.IntegerField()
    finished_time = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    coin = models.IntegerField()
    fee = models.DecimalField(max_digits=13, decimal_places=2)
    skaccount = models.CharField(max_length=255, blank=True, null=True)
    deal_bnum = models.DecimalField(max_digits=13, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tw_ad_sell'


class TwAdmin(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=16)
    nickname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    last_login_time = models.IntegerField()
    last_login_ip = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_admin'


class TwAdver(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    look = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_adver'


class TwAreaCode(models.Model):
    name_zh = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    shortname = models.CharField(max_length=255)
    areacode = models.IntegerField()
    desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_area_code'


class TwArticle(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    adminid = models.IntegerField()
    type = models.CharField(max_length=100)
    hits = models.IntegerField()
    footer = models.IntegerField()
    index = models.IntegerField()
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    img = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tw_article'


class TwArticleType(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    remark = models.CharField(max_length=50)
    index = models.CharField(max_length=50)
    footer = models.CharField(max_length=50)
    shang = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_article_type'


class TwAuthExtend(models.Model):
    group_id = models.IntegerField()
    extend_id = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_auth_extend'
        unique_together = (('group_id', 'extend_id', 'type'),)


class TwAuthGroup(models.Model):
    module = models.CharField(max_length=20)
    type = models.IntegerField()
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=80)
    status = models.IntegerField()
    rules = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'tw_auth_group'


class TwAuthGroupAccess(models.Model):
    uid = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_auth_group_access'
        unique_together = (('uid', 'group_id'),)


class TwAuthRule(models.Model):
    module = models.CharField(max_length=20)
    type = models.IntegerField()
    name = models.CharField(max_length=80)
    title = models.CharField(max_length=20)
    status = models.IntegerField()
    condition = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'tw_auth_rule'


class TwBch(models.Model):
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=30, decimal_places=8)
    updatetime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_bch'


class TwBtc(models.Model):
    name = models.CharField(max_length=20)
    name_yw = models.CharField(max_length=20)
    short_name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=30, decimal_places=8)
    updatetime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_btc'


class TwBtcLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=55)
    userid = models.IntegerField()
    ctime = models.IntegerField()
    type = models.IntegerField()
    plusminus = models.IntegerField()
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    desc = models.CharField(max_length=255, blank=True, null=True)
    operator = models.IntegerField()
    ctype = models.IntegerField()
    action = models.SmallIntegerField()
    addip = models.CharField(max_length=50, blank=True, null=True)
    showname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tw_btc_log'


class TwConfig(models.Model):
    footer_logo = models.CharField(max_length=200)
    huafei_zidong = models.CharField(max_length=200)
    kefu = models.CharField(max_length=200)
    huafei_openid = models.CharField(max_length=200)
    huafei_appkey = models.CharField(max_length=200)
    index_lejimum = models.CharField(max_length=200)
    login_verify = models.CharField(max_length=200)
    fee_meitian = models.CharField(max_length=200)
    top_name = models.CharField(max_length=200)
    web_name = models.CharField(max_length=200)
    web_title = models.CharField(max_length=200)
    web_logo = models.CharField(max_length=200)
    web_llogo_small = models.CharField(max_length=200)
    web_keywords = models.CharField(max_length=200, blank=True, null=True)
    web_description = models.CharField(max_length=200, blank=True, null=True)
    web_close = models.CharField(max_length=255, blank=True, null=True)
    web_close_cause = models.CharField(max_length=255, blank=True, null=True)
    web_icp = models.CharField(max_length=255, blank=True, null=True)
    web_cnzz = models.CharField(max_length=255, blank=True, null=True)
    web_ren = models.CharField(max_length=255, blank=True, null=True)
    web_reg = models.TextField(blank=True, null=True)
    market_mr = models.CharField(max_length=255, blank=True, null=True)
    xnb_mr = models.CharField(max_length=255, blank=True, null=True)
    rmb_mr = models.CharField(max_length=255, blank=True, null=True)
    web_waring = models.CharField(max_length=255, blank=True, null=True)
    moble_type = models.CharField(max_length=255, blank=True, null=True)
    moble_url = models.CharField(max_length=255, blank=True, null=True)
    moble_user = models.CharField(max_length=255, blank=True, null=True)
    moble_pwd = models.CharField(max_length=255, blank=True, null=True)
    contact_moble = models.CharField(max_length=255, blank=True, null=True)
    contact_weibo = models.TextField(blank=True, null=True)
    contact_tqq = models.TextField(blank=True, null=True)
    contact_qq = models.TextField(blank=True, null=True)
    contact_qqun = models.TextField(blank=True, null=True)
    contact_weixin = models.TextField(blank=True, null=True)
    contact_weixin_img = models.TextField(blank=True, null=True)
    contact_email = models.TextField(blank=True, null=True)
    contact_alipay = models.TextField(blank=True, null=True)
    contact_alipay_img = models.TextField(blank=True, null=True)
    contact_bank = models.TextField(blank=True, null=True)
    user_truename = models.TextField(blank=True, null=True)
    user_moble = models.TextField(blank=True, null=True)
    user_alipay = models.TextField(blank=True, null=True)
    user_bank = models.TextField(blank=True, null=True)
    user_text_truename = models.TextField(blank=True, null=True)
    user_text_moble = models.TextField(blank=True, null=True)
    user_text_alipay = models.TextField(blank=True, null=True)
    user_text_bank = models.TextField(blank=True, null=True)
    user_text_log = models.TextField(blank=True, null=True)
    user_text_password = models.TextField(blank=True, null=True)
    user_text_paypassword = models.TextField(blank=True, null=True)
    mytx_min = models.TextField(blank=True, null=True)
    mytx_max = models.TextField(blank=True, null=True)
    mytx_bei = models.TextField(blank=True, null=True)
    mytx_coin = models.TextField(blank=True, null=True)
    mytx_fee_min = models.FloatField(blank=True, null=True)
    mytx_fee = models.TextField(blank=True, null=True)
    trade_min = models.TextField(blank=True, null=True)
    trade_max = models.TextField(blank=True, null=True)
    trade_limit = models.TextField(blank=True, null=True)
    trade_text_log = models.TextField(blank=True, null=True)
    issue_ci = models.TextField(blank=True, null=True)
    issue_jian = models.TextField(blank=True, null=True)
    issue_min = models.TextField(blank=True, null=True)
    issue_max = models.TextField(blank=True, null=True)
    money_min = models.TextField(blank=True, null=True)
    money_max = models.TextField(blank=True, null=True)
    money_bei = models.TextField(blank=True, null=True)
    money_text_index = models.TextField(blank=True, null=True)
    money_text_log = models.TextField(blank=True, null=True)
    money_text_type = models.TextField(blank=True, null=True)
    invit_type = models.TextField(blank=True, null=True)
    invit_fee1 = models.TextField(blank=True, null=True)
    invit_fee2 = models.TextField(blank=True, null=True)
    invit_fee3 = models.TextField(blank=True, null=True)
    invit_text_txt = models.TextField(blank=True, null=True)
    invit_text_log = models.TextField(blank=True, null=True)
    index_notice_1 = models.TextField(blank=True, null=True)
    index_notice_11 = models.TextField(blank=True, null=True)
    index_notice_2 = models.TextField(blank=True, null=True)
    index_notice_22 = models.TextField(blank=True, null=True)
    index_notice_3 = models.TextField(blank=True, null=True)
    index_notice_33 = models.TextField(blank=True, null=True)
    index_notice_4 = models.TextField(blank=True, null=True)
    index_notice_44 = models.TextField(blank=True, null=True)
    text_footer = models.TextField(blank=True, null=True)
    shop_text_index = models.TextField(blank=True, null=True)
    shop_text_log = models.TextField(blank=True, null=True)
    shop_text_addr = models.TextField(blank=True, null=True)
    shop_text_view = models.TextField(blank=True, null=True)
    huafei_text_index = models.IntegerField(blank=True, null=True)
    huafei_text_log = models.TextField(blank=True, null=True)
    addtime = models.IntegerField()
    status = models.IntegerField()
    shop_coin = models.CharField(max_length=200)
    shop_logo = models.CharField(max_length=200)
    shop_login = models.CharField(max_length=200)
    index_html = models.CharField(max_length=50)
    trade_hangqing = models.CharField(max_length=50)
    trade_moshi = models.CharField(max_length=50)
    mytx_day_max = models.DecimalField(max_digits=13, decimal_places=0)
    en_web_reg = models.TextField(blank=True, null=True)
    tui_jy_jl = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True)
    before_cpc = models.BigIntegerField()
    fee_bili = models.DecimalField(max_digits=4, decimal_places=2)
    least_btc = models.DecimalField(max_digits=4, decimal_places=2)
    sfk_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_config'


class TwCusd(models.Model):
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=30, decimal_places=8)
    updatetime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_cusd'


class TwCusdLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=55)
    userid = models.IntegerField()
    ctime = models.IntegerField()
    type = models.IntegerField()
    plusminus = models.IntegerField()
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    desc = models.CharField(max_length=255, blank=True, null=True)
    operator = models.IntegerField()
    ctype = models.IntegerField()
    action = models.SmallIntegerField()
    addip = models.CharField(max_length=50, blank=True, null=True)
    showname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tw_cusd_log'


class TwDaohang(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_daohang'


class TwEth(models.Model):
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=30, decimal_places=8)
    updatetime = models.IntegerField()
    name_yw = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_eth'


class TwEthHash(models.Model):
    ethhash = models.CharField(unique=True, max_length=100)
    address = models.CharField(max_length=100)
    addtime = models.IntegerField()
    isdeal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_eth_hash'


class TwEthLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=55)
    userid = models.IntegerField()
    ctime = models.IntegerField()
    type = models.IntegerField()
    plusminus = models.IntegerField()
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    desc = models.CharField(max_length=255, blank=True, null=True)
    operator = models.IntegerField()
    ctype = models.IntegerField()
    action = models.SmallIntegerField()
    addip = models.CharField(max_length=50, blank=True, null=True)
    showname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tw_eth_log'


class TwEthTransfer(models.Model):
    zc_addr = models.CharField(max_length=100)
    zr_addr = models.CharField(max_length=100)
    zc_amount = models.DecimalField(max_digits=20, decimal_places=8)
    addtime = models.IntegerField()
    zchash = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tw_eth_transfer'


class TwEthzr(models.Model):
    id = models.BigAutoField(primary_key=True)
    fromaddress = models.CharField(max_length=255)
    toaddress = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    addtime = models.IntegerField()
    orderno = models.BigIntegerField()
    finished = models.IntegerField()
    otherid = models.BigIntegerField()
    transaction_hash = models.CharField(max_length=255)
    block_hash = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tw_ethzr'
        unique_together = (('toaddress', 'transaction_hash', 'fromaddress'),)


class TwFeedback(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    addtime = models.IntegerField()
    endtime = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=50)
    attachone = models.CharField(max_length=200, blank=True, null=True)
    attachtwo = models.CharField(max_length=200, blank=True, null=True)
    userid = models.IntegerField()
    username = models.CharField(max_length=50)
    isread = models.IntegerField()
    txid = models.CharField(max_length=100, blank=True, null=True)
    freshtime = models.IntegerField(blank=True, null=True)
    userstatus = models.IntegerField(blank=True, null=True)
    adminstatus = models.IntegerField(blank=True, null=True)
    recordno = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tw_feedback'


class TwFeedbackReply(models.Model):
    fid = models.IntegerField()
    userid = models.IntegerField()
    username = models.CharField(max_length=50)
    addtime = models.IntegerField()
    content = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tw_feedback_reply'


class TwFooter(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    remark = models.CharField(max_length=50)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_footer'


class TwLink(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    mytx = models.CharField(max_length=100)
    remark = models.CharField(max_length=50)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    look_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_link'


class TwLocation(models.Model):
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=10)
    enname = models.CharField(max_length=55, blank=True, null=True)
    name_yw = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_location'


class TwLtc(models.Model):
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=30, decimal_places=8)
    updatetime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_ltc'


class TwLtcLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=55)
    userid = models.IntegerField()
    ctime = models.IntegerField()
    type = models.IntegerField()
    plusminus = models.IntegerField()
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    desc = models.CharField(max_length=255, blank=True, null=True)
    operator = models.IntegerField()
    ctype = models.IntegerField()
    action = models.SmallIntegerField()
    addip = models.CharField(max_length=50, blank=True, null=True)
    showname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tw_ltc_log'


class TwMenu(models.Model):
    title = models.CharField(max_length=50)
    pid = models.IntegerField()
    sort = models.IntegerField()
    url = models.CharField(max_length=255)
    hide = models.IntegerField()
    tip = models.CharField(max_length=255)
    group = models.CharField(max_length=50, blank=True, null=True)
    is_dev = models.IntegerField()
    ico_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tw_menu'


class TwMycz(models.Model):
    userid = models.IntegerField()
    num = models.DecimalField(max_digits=11, decimal_places=2)
    mum = models.DecimalField(max_digits=11, decimal_places=2)
    type = models.CharField(max_length=50)
    tradeno = models.CharField(max_length=50)
    remark = models.CharField(max_length=250)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    alipay_truename = models.CharField(max_length=20, blank=True, null=True)
    alipay_account = models.CharField(max_length=35, blank=True, null=True)
    ewmname = models.CharField(max_length=50)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    bank = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_mycz'


class TwMyczInvit(models.Model):
    userid = models.IntegerField()
    invitid = models.IntegerField()
    num = models.DecimalField(max_digits=20, decimal_places=2)
    fee = models.DecimalField(max_digits=20, decimal_places=8)
    coinname = models.CharField(max_length=50)
    mum = models.DecimalField(max_digits=20, decimal_places=8)
    remark = models.CharField(max_length=250)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_mycz_invit'


class TwMyczType(models.Model):
    max = models.CharField(max_length=200)
    min = models.CharField(max_length=200)
    kaihu = models.CharField(max_length=200)
    truename = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    img = models.CharField(max_length=50)
    extra = models.CharField(max_length=50)
    remark = models.CharField(max_length=50)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tw_mycz_type'


class TwMytx(models.Model):
    userid = models.IntegerField()
    num = models.IntegerField()
    fee = models.DecimalField(max_digits=20, decimal_places=2)
    mum = models.DecimalField(max_digits=20, decimal_places=2)
    truename = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    bank = models.CharField(max_length=250)
    bankprov = models.CharField(max_length=50)
    bankcity = models.CharField(max_length=50)
    bankaddr = models.CharField(max_length=50)
    bankcard = models.CharField(max_length=200)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_mytx'


class TwMyzc(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=200)
    coinname = models.CharField(max_length=200)
    txid = models.CharField(max_length=200)
    num = models.DecimalField(max_digits=20, decimal_places=8)
    fee = models.DecimalField(max_digits=20, decimal_places=8)
    mum = models.DecimalField(max_digits=20, decimal_places=8)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    to_user = models.IntegerField()
    cointype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_myzc'


class TwMyzcEth(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=200)
    coinname = models.CharField(max_length=200)
    txid = models.CharField(max_length=200)
    num = models.DecimalField(max_digits=20, decimal_places=8)
    fee = models.DecimalField(max_digits=20, decimal_places=8)
    mum = models.DecimalField(max_digits=20, decimal_places=8)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    to_user = models.IntegerField()
    cointype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_myzc_eth'


class TwMyzcFee(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=200)
    coinname = models.CharField(max_length=200)
    txid = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    fee = models.DecimalField(max_digits=20, decimal_places=8)
    num = models.DecimalField(max_digits=20, decimal_places=8)
    mum = models.DecimalField(max_digits=20, decimal_places=8)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_myzc_fee'


class TwMyzr(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=200)
    coinname = models.CharField(max_length=200)
    txid = models.CharField(max_length=200)
    num = models.DecimalField(max_digits=20, decimal_places=8)
    mum = models.DecimalField(max_digits=20, decimal_places=8)
    fee = models.DecimalField(max_digits=20, decimal_places=8)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    from_user = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_myzr'


class TwMyzrJson(models.Model):
    id = models.BigAutoField(primary_key=True)
    addtime = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    coinname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tw_myzr_json'


class TwOrderBuy(models.Model):
    buy_id = models.IntegerField()
    buy_bid = models.IntegerField()
    sell_id = models.IntegerField()
    sell_sid = models.IntegerField()
    deal_amount = models.DecimalField(max_digits=13, decimal_places=2)
    deal_price = models.DecimalField(max_digits=13, decimal_places=2)
    deal_ctype = models.IntegerField()
    deal_num = models.DecimalField(max_digits=20, decimal_places=8)
    ctime = models.IntegerField()
    dktime = models.IntegerField()
    ltime = models.IntegerField()
    status = models.IntegerField()
    desc = models.CharField(max_length=100, blank=True, null=True)
    finished_time = models.IntegerField(blank=True, null=True)
    order_no = models.CharField(unique=True, max_length=55)
    cancle_op = models.IntegerField()
    buy_pj = models.IntegerField(blank=True, null=True)
    sell_pj = models.IntegerField(blank=True, null=True)
    su_type = models.IntegerField()
    su_reason = models.TextField(blank=True, null=True)
    sutp = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField()
    deal_coin = models.IntegerField()
    fee = models.DecimalField(max_digits=20, decimal_places=8)
    skaccount = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    adminhandle = models.IntegerField()
    lmessage = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_order_buy'


class TwOrderSell(models.Model):
    id = models.BigAutoField(primary_key=True)
    buy_id = models.IntegerField()
    buy_bid = models.IntegerField()
    sell_id = models.IntegerField()
    sell_sid = models.IntegerField()
    deal_amount = models.DecimalField(max_digits=20, decimal_places=2)
    deal_price = models.DecimalField(max_digits=13, decimal_places=2)
    deal_ctype = models.IntegerField()
    deal_num = models.DecimalField(max_digits=20, decimal_places=8)
    ctime = models.IntegerField()
    dktime = models.IntegerField()
    ltime = models.IntegerField()
    status = models.IntegerField()
    desc = models.CharField(max_length=100, blank=True, null=True)
    finished_time = models.IntegerField(blank=True, null=True)
    order_no = models.CharField(unique=True, max_length=55)
    buy_pj = models.IntegerField(blank=True, null=True)
    sell_pj = models.IntegerField(blank=True, null=True)
    su_type = models.IntegerField()
    su_reason = models.TextField(blank=True, null=True)
    cancle_op = models.IntegerField()
    sutp = models.CharField(max_length=155, blank=True, null=True)
    type = models.IntegerField()
    deal_coin = models.IntegerField()
    fee = models.DecimalField(max_digits=20, decimal_places=8)
    skaccount = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    adminhandle = models.IntegerField()
    lmessage = models.CharField(max_length=255, blank=True, null=True)
    fee1 = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_order_sell'


class TwOrderTemp(models.Model):
    id = models.BigAutoField(primary_key=True)
    ordertype = models.IntegerField()
    buy_id = models.IntegerField()
    buy_bid = models.IntegerField()
    sell_id = models.IntegerField()
    sell_sid = models.IntegerField()
    ctime = models.IntegerField()
    advtype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_order_temp'


class TwPayMethod(models.Model):
    name = models.CharField(max_length=20)
    enname = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_pay_method'


class TwRegion(models.Model):
    rgname = models.CharField(max_length=100)
    addtime = models.IntegerField()
    dluser = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_region'


class TwTradeLog(models.Model):
    userid = models.IntegerField()
    peerid = models.IntegerField()
    market = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    num = models.DecimalField(max_digits=20, decimal_places=8)
    mum = models.DecimalField(max_digits=20, decimal_places=8)
    fee_buy = models.DecimalField(max_digits=20, decimal_places=8)
    fee_sell = models.DecimalField(max_digits=20, decimal_places=8)
    type = models.IntegerField()
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_trade_log'


class TwTradePrize(models.Model):
    cpc = models.DecimalField(max_digits=20, decimal_places=6)
    trade_sum = models.DecimalField(max_digits=20, decimal_places=1)
    addtime = models.IntegerField()
    userid = models.IntegerField()
    username = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tw_trade_prize'


class TwUsdt(models.Model):
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=30, decimal_places=8)
    updatetime = models.IntegerField()
    name_yw = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_usdt'


class TwUsdtLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=55)
    userid = models.IntegerField()
    ctime = models.IntegerField()
    type = models.IntegerField()
    plusminus = models.IntegerField()
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    desc = models.CharField(max_length=255, blank=True, null=True)
    operator = models.IntegerField()
    ctype = models.IntegerField()
    action = models.SmallIntegerField()
    addip = models.CharField(max_length=50, blank=True, null=True)
    showname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tw_usdt_log'


class TwUserLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.IntegerField()
    type = models.CharField(max_length=30)
    remark = models.CharField(max_length=50)
    addip = models.CharField(max_length=20)
    addr = models.CharField(max_length=100)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    session_key = models.CharField(max_length=100, blank=True, null=True)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_user_log'


class TwUserLogCopy(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.IntegerField()
    type = models.CharField(max_length=30)
    remark = models.CharField(max_length=50)
    addip = models.CharField(max_length=20)
    addr = models.CharField(max_length=100)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    session_key = models.CharField(max_length=100, blank=True, null=True)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_user_log_copy'


class TwUserQianbao(models.Model):
    userid = models.IntegerField()
    coinname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    addr = models.CharField(max_length=200)
    sort = models.IntegerField()
    addtime = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tw_user_qianbao'


class TwZcbatchError(models.Model):
    zcid = models.IntegerField()
    addtime = models.IntegerField()
    beizhu = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_zcbatch_error'


class UserInformation(models.Model):
    user_id = models.IntegerField()
    is_access_index_once = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_information'