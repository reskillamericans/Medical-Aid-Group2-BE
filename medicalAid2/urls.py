"""medicalAid2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from aidApp import views as aid_app_views
from users import views as v



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', aid_app_views.index, name="homepage"),
    path('about-us/', aid_app_views.about_us, name="about-us"),
    path('faq/', aid_app_views.faq, name="faq"),
    path('login/', aid_app_views.login, name="login"),
    path('sign-up/', aid_app_views.sign_up, name="sign-up"),
    path('feedback/', aid_app_views.feedback, name ="feedback"),
    path('feedbacksent/', aid_app_views.feedbacksent, name="feedbacksent"),
    path('feedbackform/', aid_app_views.feedbackform, name="feedbackform"),
    path('aid/', include('aidApp.urls')),
    path('users/', include('users.urls')),
    path('submit-form/', v.submit_register_form, name="register_user"),
    path('submit-login/', v.login_submit, name="login_user"),
    path('login/', v.render_login_page, name="user_login"),
]
