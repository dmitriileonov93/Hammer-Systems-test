from rest_framework import serializers

from .models import VerifyCode


class VerifyCodeSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=False)
    phone = serializers.CharField(required=True)

    class Meta:
        model = VerifyCode
        fields = ('phone', 'code')
