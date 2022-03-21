from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from .models import VerifyCode
from .serializers import VerifyCodeSerializer


class APIPhoneToCode(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APICodeToToken(ObtainAuthToken):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = VerifyCodeSerializer(data=request.data,
                                          context={'request': request})
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            code = serializer.validated_data['code']
            if VerifyCode.objects.filter(phone=phone, code=code).exists():
                user, user_created = User.objects.get_or_create(
                    phone_number=phone)
                token, token_created = Token.objects.get_or_create(user=user)
                VerifyCode.objects.get(phone=phone, code=code).delete()
                return Response({
                    'token': token.key,
                    'phone_number': str(user.phone_number),
                })
            return Response(
                {'message': 'Wrong code!'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
