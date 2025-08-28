from django.urls import path
from .views import (
    signup,
    UserLoginView,
    UserLogoutView,
    ProfileDetailView,
    profile_update,
    UserPasswordChangeView,
)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', profile_update, name='profile_edit'),
    path('password/change/', UserPasswordChangeView.as_view(), name='password_change'),
]

