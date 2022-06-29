from .views import (
    loginPage,
    logoutUser,
    # register,
    updateUser
)
from django.urls import path
from django.conf import settings
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', loginPage, name=settings.LOGIN_URL_NAME),
    path('logout', logoutUser, name="logout-page"),
    # path('signup', register, name="sign-up-page"),
    path('update', updateUser, name="update-user-page"),
    # path('reset_password/',auth_views.PasswordResetView.as_view(template_name='users/reset_password.html'),name='password_reset'), # noqa
    # path('reset_password_done/',auth_views.PasswordResetDoneView.as_view(template_name='users/reset_password_done.html'),name='password_reset_done'), # noqa
    # path('reset_password_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/reset_password_confirm.html'),name='password_reset_confirm'), # noqa
    # path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/reset_password_complete.html'),name='password_reset_complete'), # noqa
]
