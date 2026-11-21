from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userid', 'email', 'password', 'name', 'phone', 'cityid']
        read_only_fields = ['userid']
        extra_kwargs = {
            'password': {'write_only': True},
            'phone': {'required': False},
        }


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.IntegerField()
    password = serializers.CharField(max_length=128)
