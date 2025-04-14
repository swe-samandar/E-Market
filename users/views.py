
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from .forms import UserRegistrationForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser, SavedProduct
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from products.models import Product, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from conversation.models import ConversationRoom
# Create your views here.

class SignUpView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'users/signup.html', {'form': form})
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Siz muvaffiqaytli ro'yxatdan o'tdingiz!")
            return redirect('users:login')
        return render(request, 'users/signup.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:index')
            else:
                form.add_error(None, "Noto'g'ri username yoki parol.")

        return render(request, 'users/login.html', {'form': form})
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main:index')
    

class ProfileView(View):
    def get(self, request, username):
        customuser = get_object_or_404(CustomUser, username=username)
        saveds = SavedProduct.objects.filter(user=customuser)
        products = Product.objects.filter(author=customuser)
        
        notificationss = ConversationRoom.objects.filter(user1=customuser)
        notifications_ = ConversationRoom.objects.all()
        notifications = [item for item in notifications_ if item.user2 == request.user]
        
        query = request.POST.get('q')
        if query:
            products = Product.objects.filter(title__icontains=query)
            return render(request, 'users/profile.html', {'customuser':customuser, 'products':products, 'notifications': notifications if notifications else notificationss})
        return render(request, 'users/profile.html', {'customuser':customuser, 'products':products, 'saveds':saveds, 'notifications': notifications if notifications else notificationss})


class ProfileUpdateView(View):
    def get(self, request):
        return render(request, 'users/profile_update.html', {'form':ProfileUpdateForm(instance=request.user)})

    def post(self, request):
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile', request.user)
        return render(request, 'users/profile_update.html', {'form':form})

        
class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('users:password-change-done')
    template_name = 'users/password_change_form.html'


class NewCommentView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        comment = Comment.objects.create(
            product = product,
            author = request.user,
            body = request.POST["comment"]
            )
        if comment:
            comment.save()
            messages.info(request, 'Successfully Sended!')
            return redirect('main:detail', product.title)
        return HttpResponse("Add comment")


class DeleteCommentView(LoginRequiredMixin, View):
    login_url = 'users:login'
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.author:
            comment.delete()
            messages.info(request, "Succesfully deleted!")
        return redirect(request.META.get("HTTP_REFERER"))


class AddRemovedSavedView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        saved_products = SavedProduct.objects.filter(user=request.user, product=product)
        if saved_products:
            saved_products.delete()
            # saved = False
            messages.info(request, 'Removed')  
        else:
            SavedProduct.objects.create(user=request.user, product=product)    
            # saved = True
            messages.info(request, 'Saved')
        return redirect(request.META.get("HTTP_REFERER"))


class SavedsView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request):
        saveds = SavedProduct.objects.filter(user=request.user)
        query = request.POST.get('q')
        if query:
            products = Product.objects.filter(title__icontains=query)
            saveds = SavedProduct.objects.filter(user=request.user, product__in=products)
        return render(request, 'users/saveds.html', {'saveds': saveds})


def password_change_done(request):
    return render(request, 'users/password_change_done.html')


@require_POST
@login_required
def ajax_toggle_follow(request):
    target_user = get_object_or_404(CustomUser, username=request.POST.get('username'))

    if target_user in request.user.following.all():
        request.user.following.remove(target_user)
        following = False
    else:
        request.user.following.add(target_user)
        following = True

    return JsonResponse({
        'following': following,
        'followers_count': target_user.followers.count()
    })


def get_followers(request, username):
    customuser = get_object_or_404(CustomUser, username=username)
    return render(request, 'users/followers.html', {'customuser':customuser})


def get_followings(request, username):
    customuser = get_object_or_404(CustomUser, username=username)
    return render(request, 'users/followings.html', {'customuser':customuser})


def get_all_users(request):
    users = CustomUser.objects.all()
    print(users)
    return render(request, 'users/all_users.html', {'users':users})

