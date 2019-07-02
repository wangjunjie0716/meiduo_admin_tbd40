from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(min_length=5,max_length=20,error_messages={
        'min_length': '用户名是5到20位数字、字母或下划线',
        'max_length': '用户名是5到20位数字、字母或下划线',
    },required=True)
    email = serializers.EmailField()
    mobile = serializers.CharField(required=True)
    password = serializers.CharField(read_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return  user

