import requests
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token

from accounts.serializers import (
    BaseUserSerializer,
    AdminSerializer,
    PasswordResetSerializer,
    RequestPasswordResetSerializer,
    VerifyCodeSerializer,
    UserLoginSerializer,
)
from accounts.utils import send_password_reset_email


User = get_user_model()

"""
Auth
"""


class TokenView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            user = authenticate(email=email, password=password)

            if user:
                if user.is_active:
                    token, created = Token.objects.get_or_create(user=user)
                    user_details = {
                        "id": user.id,
                        "email": user.email,
                        "is_superuser": user.is_superuser,
                        "is_active": user.is_active,
                        "is_staff": user.is_staff,
                        "is_verified": user.is_verified,
                        "is_admin": user.is_guest,
                        "token": token.key,
                    }
                    return Response(user_details, status=status.HTTP_200_OK)
                else:
                    return Response(
                        {"detail": ("User account is disabled.")},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {"detail": ("Unable to log in with provided credentials.")},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
Create views
"""


class AdminCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = AdminSerializer


"""
User detail views
"""


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BaseUserSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


"""
Account verification
"""


class VerifyEmailView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = VerifyCodeSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data.get("user")
            verification = serializer.validated_data.get("verification")

            # Verify the account
            user.is_verified = True
            user.save()

            # Mark code as used
            verification.used = True
            verification.save()

            return Response(
                {"message": "Account verified successfully!"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
Forgot password and password reset
"""


class RequestPasswordResetView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RequestPasswordResetSerializer(data=request.data)

        if serializer.is_valid():
            verification = serializer.save()

            send_password_reset_email(verification.user, verification.code)

            return Response(
                {"message": "Password reset email sent successfully!"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Password reset successful!"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
