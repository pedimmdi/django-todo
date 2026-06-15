from rest_framework import serializers
from accounts.models import Profile, User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name', 'image', 'bio']
        extra_kwargs = {
            'user': {'read_only': True}
        }
