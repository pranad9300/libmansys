from django.urls import path,include
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    # path('', TemplateView.as_view(template_name='social_app/login.html')),
    path('sign_up', views.sign_up, name="sign_up"),
    path('login/',views.login,name="login"),
    path('createuser',views.createuser,name="createuser"),
    path('handle_login',views.handle_login,name="handle_login"),
    path('index',views.index,name="index"),
    path('logout',views.logout,name="logout"),
    path('createprofile',views.createprofile,name="createprofile")
]