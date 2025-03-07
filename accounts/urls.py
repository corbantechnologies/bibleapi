from django.urls import path

from accounts.views import (
    AdminCreateView,
    TokenView,
    UserDetailView,
    RequestPasswordResetView,
    PasswordResetView,
    VerifyEmailView,
)

app_name = "accounts"

urlpatterns = [
    path("login/", TokenView.as_view(), name="login"),
    path("signup/admin/", AdminCreateView.as_view(), name="admin-signup"),
    path("verify-account/", VerifyEmailView.as_view(), name="verify-email"),
    path("<str:id>", UserDetailView.as_view(), name="user-detail"),
    path("password/reset/", RequestPasswordResetView.as_view(), name="password-reset"),
    path("password/new/", PasswordResetView.as_view(), name="password-reset"),
]
