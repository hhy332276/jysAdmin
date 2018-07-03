import time

from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from jys.models import BfUser, BfUserCoin
from qhjy.models import QhBetting
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def index(requests):
#     return render(requests,'users/index.html')

def timeCover(t):
    t1= time.localtime(t)
    t2 = time.strftime('%Y-%m-%d %H:%M:%S', t1)
    return t2

@login_required
def index(request,num):
    t = time.localtime(time.time())
    t = int(time.mktime(time.strptime(time.strftime('%Y-%m-%d 00:00:00', t), '%Y-%m-%d %H:%M:%S')))
    # 新增用户
    if num == "1":
        object_list = BfUser.objects.filter(addtime__gt=t)
    # 活跃用户
    elif num == "2":
        user_ids = QhBetting.objects.using('db2').values('user_id').distinct().filter(add_time__gt=t)
        # print(user_id.values())
        mlst = []
        print(user_ids)
        for i in user_ids:
            mlst.append(i['user_id'])
        object_list = BfUser.objects.filter(id__in=mlst)
    # 在线用户
    elif num == "3":
        object_list = BfUser.objects.using('db1').filter(login_time__gt=t)
    # 所有用户
    else:
        object_list = BfUser.objects.all()

    limit = 10
    p = Paginator(object_list, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    # print('我是page------------',page)
    # print('我是id------------',primary_domain_id)
    if page:
        pass
    else:
        page = 1
    try:
        a_a = p.page(page)  # 获取某页对应的记录
        page1 = p.page(page)
        user_list = page1.object_list
    except PageNotAnInteger:  # 如果页码不是个整数
        a_a = p.page(1)  # 取第一页的记录
        # page1 = p.page(1)
        # user_list = page1.object_list
    except EmptyPage:  # 如果页码太大，没有相应的记录
        a_a = p.page(p.num_pages)
        # page1 = p.page(p.num_pages)
        # user_list = page1.object_list
        # 取最后一页的记录
    print(user_list)
    # if BfUser.objects.filter(item_info__icontains='qinshilin'):
    #     search_contents = BfUser.objects.filter(item_info__icontains='qinshilin')
    #     print(search_contents)
    return render(request, 'users/index.html',
                  { 'user_list': user_list, 'second_list_obj': a_a, 'p': p})

def search(request):
    print('hello')
    q = request.GET.get('id')
    print(q)
    error_msg = ''
    if not q:
        error_msg = '请输入关键字'
        return render(request, 'users/index.html', {'error_msg': error_msg})
    # post_list = BfUser.objects.filter(Q(id=q) | Q(username__icontains=q))
    post_list = BfUser.objects.filter(Q(id=q) | Q(username__icontains=q))
    print(post_list)
    return render(request, 'users/index.html', {'error_msg': error_msg,
                                                'user_list': post_list})



    # return render(request,'users/index.html',{'page':page,'userList':userList})


def test(request):
    return render(request,'users/test.html',{'t':int(time.time())})




