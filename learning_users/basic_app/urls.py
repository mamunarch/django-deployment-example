from django.conf.urls import url
from basic_app import views

# for relative url
app_name = 'basic_app'

urlpatterns = [
    url(r'^registe/', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_logi'),
]
