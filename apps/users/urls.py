from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'index/(\d)/$', views.index,name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'test/$',views.test,name='test')
]