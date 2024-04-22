from django.urls import path
from .views import UserRegistrationView, CustomUserLoginAPI, ManageUserView

urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name='signup'),
    path('login/', CustomUserLoginAPI.as_view(), name='token'),
    path('me/', ManageUserView.as_view(), name='me'),
]
