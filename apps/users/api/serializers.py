from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.models import User
from django.contrib.auth.models import Group, Permission


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class GetPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class GetGroupSerializer(serializers.ModelSerializer):
    permissions = GetPermissionsSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    groups = GetGroupSerializer(many=True, read_only=True)
    user_permissions = GetPermissionsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    groups = GetGroupSerializer(many=True, read_only=True)
    user_permissions = GetPermissionsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user


class UserListSerializer(serializers.ModelSerializer):
    groups = GetGroupSerializer(many=True, read_only=True)
    user_permissions = GetPermissionsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class UserListSerializerTest(serializers.ModelSerializer):
    # fields = ('name',)
    def to_representation(self, instance):
        # print(instance)
        # data = super().to_representation(instance)
        class Meta:
            model = User
            # exclude = ('updated_at',)

        return {
            'id': instance['id'],
            'password': instance['password'],
            'last_login': instance['last_login'],
            'is_superuser': instance['is_superuser'],
            'username': instance['username'],
            'email': instance['email'],
            'name': instance['name'],
            'last_name': instance['last_name'],
            'image': instance['image'],
            'is_active': instance['is_active'],
            'is_staff': instance['is_staff'],
            'created_at': instance['created_at'],
            'updated_at': instance['updated_at'],
            'groups': instance['groups'],
            'user_permissions': instance['user_permissions'],
        }
