import random

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import (
    ForgotPasswordSerializer,
    RegisterSerializer,
    ResetPasswordSerializer,
)


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def forgot_password(request):
    serializer = ForgotPasswordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data['email']

    user = User.objects.filter(email=email).first()
    if user is None:
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    user.code = random.randint(100000, 999999)
    user.save(update_fields=['code'])
    # TODO: remove code from the response once it is sent by email.
    return Response({'email': user.email, 'code': user.code})


@api_view(['POST'])
def reset_password(request):
    serializer = ResetPasswordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    user = User.objects.filter(email=data['email']).first()
    if user is None or user.code == 0 or user.code != data['code']:
        return Response({'detail': 'Invalid code'}, status=status.HTTP_400_BAD_REQUEST)

    user.password = data['password']
    user.code = 0
    user.save(update_fields=['password', 'code'])
    return Response({'detail': 'Password reset successful'})
