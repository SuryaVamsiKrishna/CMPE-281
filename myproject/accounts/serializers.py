from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import AVDriver, AVStaff

User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password', 'user_type')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user_type = validated_data.pop('user_type')
#         user = User.objects.create_user(**validated_data)
#         user.user_type = user_type
#         user.save()
#         if user_type == User.AV_DRIVER:
#             AVDriver.objects.create(user=user, **validated_data)
#         elif user_type == User.AV_STAFF:
#             AVStaff.objects.create(user=user)
#         return user

# class AVDriverSerializer(serializers.ModelSerializer):
#     user = UserSerializer(required=True)

#     class Meta:
#         model = AVDriver
#         fields = ('user', 'license_number', 'vehicle_color', 'model_number', 'sensor_info')
    
#     def validate(self, data):
#         """
#         Perform custom validation on the serializer data.
#         """
#         # Check if username is unique
#         if 'username' in data:
#             existing_user = User.objects.filter(username=data['username']).exists()
#             if existing_user:
#                 raise serializers.ValidationError("Username already exists")

#         # Additional custom validation logic can go here

#         return data

#     def create(self, validated_data):
#         user_data = validated_data.pop('user')
#         user = UserSerializer.create(UserSerializer(), validated_data=user_data)
#         user.is_av_driver = True
#         user.save()
#         av_driver = AVDriver.objects.create(user=user, **validated_data)
#         return av_driver

# class AVStaffSerializer(serializers.ModelSerializer):
#     user = UserSerializer(required=True)

#     class Meta:
#         model = AVStaff
#         fields = ('user',)

#     def create(self, validated_data):
#         user_data = validated_data.pop('user')
#         user = UserSerializer.create(UserSerializer(), validated_data=user_data)
#         user.is_av_staff = True
#         user.save()
#         av_staff = AVStaff.objects.create(user=user)
#         return av_staff



class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'user_type']

class AVDriverSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = AVDriver
        fields = ['user', 'license_number', 'vehicle_color', 'model_number', 'sensor_info']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        print("Inide this....")
        user = User.objects.create(**user_data)
        av_driver = AVDriver.objects.create(user=user, **validated_data)
        return av_driver

class AVStaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = AVStaff
        fields = ['user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        av_staff = AVStaff.objects.create(user=user, **validated_data)
        return av_staff
