from django.urls import path

from .views import (
    SignUpView,
    LoginView,
    LogoutView,
    ProfileView,
    ProfileUpdateView,
    PasswordChangeView,
    NewCommentView,
    DeleteCommentView,
    AddRemovedSavedView, 
    SavedsView,
    password_change_done,
    ajax_toggle_follow,
    get_followers,
    get_followings,
    get_all_users,
    )

app_name = 'users'

urlpatterns = [

    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<str:username>/profile/', ProfileView.as_view(), name='profile'),
    path('profile-edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('<int:product_id>/comment/', NewCommentView.as_view(), name='new-comment'),
    path('comment/delete/<int:comment_id>/', DeleteCommentView.as_view(), name='delete-comment'),
    path('saved/<int:product_id>', AddRemovedSavedView.as_view(), name='saved'),
    path('saveds/', SavedsView.as_view(), name='saveds'),
    path('password-change-done/', password_change_done, name='password-change-done'),
    path('ajax/toggle-follow/', ajax_toggle_follow, name='ajax-toggle-follow'),
    path('<str:username>/followers/', get_followers, name='followers'),
    path('<str:username>/followigs/', get_followings, name='followings'),
    path('all/', get_all_users, name='all-users'),

    


]

