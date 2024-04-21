from django.shortcuts import render

# Create your views here.
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AVDriverSerializer, AVStaffSerializer, UserSerializer, AuthTokenSerializer 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics, authentication, permissions, viewsets
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework import parsers


class UserRegistrationView(APIView):
    parser_classes = [parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser]

    # def get(self, request, *args, **kwargs):
    #     # Decide which serializer to use
    #     user_type = request.query_params.get('user_type')
    #     if user_type == 'driver':
    #         serializer = AVDriverSerializer()
    #     else:
    #         serializer = AVStaffSerializer()
    #     # Display the HTML form for the serializer
    #     serializer = UserSerializer
    #     return Response({'serializerData': serializer.data})

    def post(self, request, *args, **kwargs):
        user_type = request.data.get('user_type')
        print("Inide this.... hello")
        if user_type == 'driver':
            serializer = AVDriverSerializer(data=request.data)
        else:
            serializer = AVStaffSerializer(data=request.data)
        print("Inide this.... hello 12345")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user

