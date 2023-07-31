from django.db.transaction import atomic
from rest_framework import serializers
from users import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'is_active', 'is_staff', 'is_superuser',
                  'last_login', 'date_joined', ]
        read_only_fields = ['id', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined', ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        attrs = super().validate(attrs)
        return attrs

    @atomic()
    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    @atomic()
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        if 'password' in validated_data.keys():
            instance.set_password(validated_data['password'])
            instance.save()
        return instance
