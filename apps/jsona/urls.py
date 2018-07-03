from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'user_overview/$', views.user_overview,name='user_overview'),
    url(r'user_data/$', views.user_data, name='user_data'),
]