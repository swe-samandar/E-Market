from django.urls import path
from .views import SignupView, logout_view, ProfileView, ProfileUpdateView

app_name = 'users'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('update/', ProfileUpdateView.as_view(), name='update'),

]
