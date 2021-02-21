from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
path('login/', auth_views.LoginView.as_view(template_name='html/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('signup/', views.createaccount, name='signup'),
path('profile/', views.profile, name='profile'),
path('change-password/', auth_views.PasswordChangeView.as_view(template_name='html/change_pass.html'), name='password_change'),
path('change-password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='html/done.html'), name='password_change_done')
]