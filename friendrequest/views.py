from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from friendrequest.forms import UserCreateForm

from .models import User, Friend_Request


# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"])
            login(request, new_user)
            return HttpResponse('loggeDIN')
        else:
            print(request.POST, form.errors)
            context = {
                'form': form,
                'error': form.errors
            } 
            return render(request, 'signup.html', context)
    else:
        form = UserCreateForm()
        return render(request, 'signup.html', {'form': form})



def loginview(request):
    if request.method == 'POST':
        user = authenticate(request, 
            username = request.POST['username'],
            password = request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponse('LOGGED_IN')
        else:
            return HttpResponse('LOGIN UNSUCCESSFUL')

    else:
        return render(request, 'login.html')
        
# Send FRIEND REQUST
@login_required
def send_friend_request(request, userID):
    from_user = request.user
    to_user = User.objects.get(id=userID)
    friend_request, created = Friend_Request.objects.get_or_create(
        from_user=from_user, to_user=to_user)
    if created:
        return HttpResponse('request sent successfully')
    else:
        return HttpResponse('request was already sent')

# Accept FRIEND REQUEST
def accept_friend_request(request, requestID):
    friend_request = Friend_Request.objects.get(request=requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.from_user)
        friend_request.delete()

        return HttpResponse('friend request accepted')
    else:
        HttpResponse('friend request not accepted')
