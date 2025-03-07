from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

from accounts.validators import (
    validate_password_digit,
    validate_password_uppercase,
    validate_password_lowercase,
    validate_password_symbol,
)
from verification.models import VerificationCode
from accounts.utils import send_verification_email

User = get_user_model()


class BaseUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        max_length=128,
        min_length=5,
        write_only=True,
        validators=[
            validate_password_digit,
            validate_password_uppercase,
            validate_password_symbol,
            validate_password_lowercase,
        ],
    )
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "is_active",
            "is_staff",
            "is_superuser",
            "is_admin",
            "created_at",
            "updated_at",
            "reference",
            "slug",
        )

    def create_user(self, validated_data, role_field):
        """
        Normal email and password signup
        """
        user = User.objects.create_user(**validated_data)
        setattr(user, role_field, True)
        user.is_active = True
        user.save()

        verification_code = VerificationCode.objects.create(
            user=user, purpose="email_verification"
        )
        send_verification_email(user, verification_code.code)

        return user


class AdminSerializer(BaseUserSerializer):
    def create(self, validated_data):
        user = self.create_user(validated_data, "is_admin")
        user.is_staff = True
        user.save()
        return user


"""
Account verification
"""


class VerifyCodeSerializer(serializers.Serializer):
    code = serializers.CharField()

    def validate(self, attrs):
        code = attrs.get("code")

        try:
            verification = VerificationCode.objects.get(
                code=code, purpose="email_verification", used=False
            )
        except VerificationCode.DoesNotExist:
            raise serializers.ValidationError("Invalid or expired verification code!")

        try:
            user = User.objects.get(email=verification.user.email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Account with this email does not exist!")

        try:
            verification = user.verification_codes.get(
                code=code, purpose="email_verification", used=False
            )
        except VerificationCode.DoesNotExist:
            raise serializers.ValidationError("Invalid or expired verification code!")

        if not verification.is_valid():
            raise serializers.ValidationError(
                "The code has expired or already been used!"
            )

        attrs["user"] = user
        attrs["verification"] = verification

        return attrs


"""
Forgot Password and Reset Password
"""


class RequestPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Account with this email does not exist!")
        return email

    def save(self):
        email = self.validated_data.get("email")
        user = User.objects.get(email=email)

        # create verification code
        verification = VerificationCode.objects.create(
            user=user, purpose="password_reset"
        )

        return verification


class PasswordResetSerializer(serializers.Serializer):
    code = serializers.CharField()
    password = serializers.CharField(
        max_length=128,
        min_length=5,
        write_only=True,
        validators=[
            validate_password_digit,
            validate_password_uppercase,
            validate_password_symbol,
            validate_password_lowercase,
        ],
    )

    def validate(self, attrs):
        code = attrs.get("code")

        try:
            verification = VerificationCode.objects.get(
                code=code, purpose="password_reset", used=False
            )
        except VerificationCode.DoesNotExist:
            raise serializers.ValidationError("Invalid or expired verification code!")

        if not verification.is_valid():
            raise serializers.ValidationError(
                "The code has expired or already been used!"
            )

        attrs["verification"] = verification
        attrs["user"] = verification.user
        return attrs

    def save(self):
        user = self.validated_data.get("user")
        verification = self.validated_data.get("verification")
        password = self.validated_data.get("password")

        # update password
        user.set_password(password)
        user.save()

        # mark code as used
        verification.used = True
        verification.save()

        return user


"""
Normal login
"""


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(required=True, write_only=True)
