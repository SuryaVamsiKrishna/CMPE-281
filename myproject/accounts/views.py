from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AVDriverSerializer, AVStaffSerializer, UserSerializer, CustomLoginSerializer, CustomUserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics, authentication, permissions, viewsets
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework import parsers
from .forms import LoginForm
from .forms import UserForm, AVDriverForm, AVStaffForm

class UserRegistrationView(APIView):
    parser_classes = [parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser]

    def post(self, request, *args, **kwargs):
        user_data = request.data.get('user')
        user_type = user_data.get('user_type')
        print("Inide this.... hello")
        if user_type == 'driver':
            print("driver")
            serializer = AVDriverSerializer(data=request.data)
        else:
            print(user_type)
            print(user_type == 'driver')
            serializer = AVStaffSerializer(data=request.data)
        print("Inide this.... hello 12345")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomUserLoginAPI(APIView):
    SerializerClass = CustomLoginSerializer

    def post(self, request):
        serializer = self.SerializerClass(data=request.data)
        serializer.is_valid(raise_exception=True)

        response_data = {
            "success": True,
            "email": serializer.validated_data["user"].email,
            "username": serializer.validated_data["user"].username,
            **(CustomUserSerializer(instance=serializer.validated_data["user"]).data),
        }
        return Response(response_data, status=status.HTTP_200_OK)

        
class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user


from rest_framework import status, views
from rest_framework.response import Response
from .models import User, AVDriver, AVStaff

class GetUserDetailsByUsername(views.APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            user_data = {
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "user_type": user.user_type,
                    "password": user.password,
                }
            }

            if user.user_type == User.AV_DRIVER:
                driver = AVDriver.objects.get(user=user)
                user_data['license_number'] = driver.license_number
                user_data['vehicle_color'] = driver.vehicle_color
                user_data['model_number'] = driver.model_number
                user_data['sensor_info'] = driver.sensor_info
                # user_data.update(driver_data)

            return Response(user_data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

from rest_framework import status, views
from rest_framework.response import Response
from .models import User, AVDriver, AVStaff

class EditProfile(views.APIView):
    def put(self, request):
        user_data = request.data.get("user", {})
        username = user_data.get("username", "")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update user information
        user.email = user_data.get("email", user.email)
        user.password = user_data.get("password", user.password)
        user.save()

        user_type = user_data.get("user_type", "")
        if user_type == User.AV_DRIVER:
            # Update AVDriver information
            driver_data = request.data
            try:
                driver = AVDriver.objects.get(user=user)
            except AVDriver.DoesNotExist:
                return Response({"error": "AVDriver not found"}, status=status.HTTP_404_NOT_FOUND)
            
            driver.license_number = driver_data.get("license_number", driver.license_number)
            driver.vehicle_color = driver_data.get("vehicle_color", driver.vehicle_color)
            driver.model_number = driver_data.get("model_number", driver.model_number)
            driver.sensor_info = driver_data.get("sensor_info", driver.sensor_info)
            driver.save()
        elif user_type == User.AV_STAFF:
            # Update AVStaff information
            staff_data = request.data
            try:
                staff = AVStaff.objects.get(user=user)
            except AVStaff.DoesNotExist:
                return Response({"error": "AVStaff not found"}, status=status.HTTP_404_NOT_FOUND)
            # Update AVStaff information here similarly to AVDriver

        return Response({"message": "User profile updated successfully"}, status=status.HTTP_200_OK)


