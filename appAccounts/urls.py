from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import EmailAuthenticationForm

urlpatterns = [
    # path('', views.dashboard, name='dashboard'),
    # path('lead/new/', views.lead_create, name='lead_create'),
    # path('lead/<int:pk>/', views.lead_detail, name='lead_detail'),
    # path('lead/<int:pk>/edit/', views.lead_update, name='lead_update'),
    # path('lead/<int:pk>/delete/', views.lead_delete, name='lead_delete'),
]

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(
        template_name='appAccounts/login.html',
        authentication_form=EmailAuthenticationForm
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='appAccounts/password_reset.html',
        email_template_name='appAccounts/password_reset_email.html',
        subject_template_name='appAccounts/password_reset_subject.txt',
        success_url='/password_reset_done/'
    ), name='password_reset'),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='appAccounts/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='appAccounts/password_reset_confirm.html',
        success_url='/reset/done/'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='appAccounts/password_reset_complete.html'
    ), name='password_reset_complete'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='appAccounts/password_change.html',
        success_url='/password_change_done/'
    ), name='password_change'),

    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='appAccounts/password_change_done.html'
    ), name='password_change_done'),
]