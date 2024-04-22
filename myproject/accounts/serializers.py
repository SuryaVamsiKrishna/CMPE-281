from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import AVDriver, AVStaff
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed


INVALID_CRED_TXT = "Invalid Credentials"

User = get_user_model()

class CustomLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)


    def validate(self, attrs):
        try:
            user = None
            user = User.objects.get(username=self.initial_data.get("username"))
            print("Hi")
            print(user)
        except User.DoesNotExist:
            raise AuthenticationFailed(INVALID_CRED_TXT)

        attrs["user"] = user
        print("Authentication successfull")
        print(self.initial_data.get("password"))
        password = attrs.get("password")
        if not user.check_password(password):
            print(self.initial_data.get("password"))
            raise AuthenticationFailed(INVALID_CRED_TXT)
        return attrs
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'user_type', 'password']

class AVDriverSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = AVDriver
        fields = ['user', 'license_number', 'vehicle_color', 'model_number', 'sensor_info']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        print(user_data)
        print("Inide this....")
        user = User.objects.create(**user_data)
        print("user:",user)
        av_driver = AVDriver.objects.create(user=user, **validated_data)
        print("av_driver:",av_driver)
        return av_driver

class AVStaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = AVStaff
        fields = ['user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        print(user_data)
        user = User.objects.create(**user_data)
        print("user:",user)
        av_staff = AVStaff.objects.create(user=user, **validated_data)
        print("av_staff:",av_staff)
        return av_staff


class CustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    # role = serializers.ChoiceField(choices=User.ROLE_CHOICES)
    username = serializers.CharField(max_length=24, required=False)
    # phoneNumber = PhoneNumberField()