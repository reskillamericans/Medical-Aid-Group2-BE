from django.urls import path
from . import views
from aidApp import views as aid_app_views


app_name = 'users'

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/', views.render_login_page, name='user_login'),
    path('submit-form/', views.submit_register_form, name='register_user'),
    path('submit-login/', views.login_submit, name="login_user"),
    path('', aid_app_views.index, name="homepage"),
    path('index/', views.index, name='index'),
    path('about-us/', views.about_us, name='about-us'),
    path('faq/', views.faq, name="faq"),
    
    

]