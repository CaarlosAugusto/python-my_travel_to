from django.conf.urls import url
from mytravelto_app import views

#TEMPLATE URLS!
app_name = 'mytravelto_app'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
