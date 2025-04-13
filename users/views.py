from django.contrib.auth import logout, login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, ProfileUpdateForm
from django.views import View
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from conversation.models import ConversationRoom


class SignupView(View):
    def get(self, request):
        return render(request, 'registration/signup.html', {'form': SignupForm()})

    def post(self, request):
        if request.method == 'POST':
            form = SignupForm(data=request.POST)

            if form.is_valid():
                user = form.save()
                login(request, user)
                print('login works, Uhhhh!!!')
                messages.success(request, 'Muvaffaqiyatli royxatdan otdingiz')
                return redirect('main:index')

        else:
            form = SignupForm()
        return render(request, 'registration/signup.html', {'form': form})



def logout_view( request):
    logout(request)
    return redirect('main:index')


class ProfileView(View):
    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        #notifications = ConversationRoom.objects.filter(user2=user)
        notifications_ = ConversationRoom.objects.all()
        print(type(notifications_))
        notifications = [item for item in notifications_ if item.user2 == request.user ]


        return render(request, 'registration/profile.html', {'customuser': user,
                                                             'notifications': notifications})


class ProfileUpdateView(View, LoginRequiredMixin):
    login_url = 'login'
    def get(self, request):
        form = ProfileUpdateForm(instance=request.user)
        return render(request, 'registration/profile_update.html', {'form': form})

    def post(self, request):
        #if request.method == 'POST':
        form = ProfileUpdateForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
                form.save()
                return redirect('users:profile', request.user.pk)

        #else: form = ProfileUpdateForm(instance=request.user)
        return render(request, 'registration/signup.html', {'form': form})