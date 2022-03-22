from rest_framework import serializers

from users.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    invited_users = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('phone_number', 'owner_invite_code', 'inviter_code', 'invited_users')

    def get_invited_users(self, obj):
        users = User.objects.filter(
            inviter_code=self.context['request'].user.owner_invite_code
        )
        result = []
        for user in users:
            result.append(str(user.phone_number))
        return set(result)
