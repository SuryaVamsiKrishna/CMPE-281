from django.urls import path
from .views import UserRegistrationView, CustomUserLoginAPI, ManageUserView, GetUserDetailsByUsername

urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name='signup'),
    path('login/', CustomUserLoginAPI.as_view(), name='token'),
    path('me/', ManageUserView.as_view(), name='me'),
    path('get-user-details/<str:username>/', GetUserDetailsByUsername.as_view(), name='get_user_details'),
]

