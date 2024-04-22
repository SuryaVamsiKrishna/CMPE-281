from django.shortcuts import render

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

