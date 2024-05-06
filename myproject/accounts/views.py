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

# class CustomUserLoginAPI(APIView):
#     def get(self, request):
#         form = LoginForm()
#         return render(request, 'login.html', {'form': form})

#     def post(self, request):
#         print("Call from front-end")
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             serializer = CustomLoginSerializer(data=form.cleaned_data)
#             if serializer.is_valid():
#                 user = serializer.validated_data['user']
#                 response_data = {
#                     "success": True,
#                     "email": user.email,
#                     "username": user.username,
#                     **(CustomUserSerializer(instance=user).data),
#                 }
#                 return Response(response_data, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return render(request, 'login.html', {'form': form})


# class UserRegistrationView(APIView):
#     def get(self, request):
#         user_form = UserForm()
#         driver_form = AVDriverForm(prefix='driver')
#         staff_form = AVStaffForm(prefix='staff')
#         return render(request, 'registration_form.html', {
#             'user_form': user_form,
#             'driver_form': driver_form,
#             'staff_form': staff_form
#         })

#     def post(self, request):
#         user_form = UserForm(request.POST, prefix='user')
#         if user_form.is_valid():
#             user = user_form.save()
#             if user.user_type == 'driver':
#                 driver_form = AVDriverForm(request.POST, prefix='driver')
#                 if driver_form.is_valid():
#                     driver = driver_form.save(commit=False)
#                     driver.user = user
#                     driver.save()
#                     return redirect('success_url')
#             elif user.user_type == 'staff':
#                 staff_form = AVStaffForm(request.POST, prefix='staff')
#                 if staff_form.is_valid():
#                     staff = staff_form.save(commit=False)
#                     staff.user = user
#                     staff.save()
#                     return redirect('success_url')

#         return render(request, 'registration_form.html', {
#             'user_form': user_form,
#             'driver_form': AVDriverForm(prefix='driver'),
#             'staff_form': AVStaffForm(prefix='staff')
#         })


        
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

