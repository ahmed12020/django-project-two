from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import Profile
from .forms import CommentForm, SignForm
from datetime import datetime, timedelta
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
# Create your views here.

def sign(request):
    if request.method == 'POST':
        forms = SignForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile')
    else:
        forms = SignForm()
    return render(request, 'profile/sign.html', {'forms':forms})




class Login(LoginView):
    template_name = 'registration/login.html'
    success_url = '/accounts/profile'


def setcookie(request):
    response = render(request, 'profile/setcookie.html')
    response.set_cookie('name','ahmed', expires=datetime.utcnow()+timedelta(days=10))
    return response

def getcookie(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('name', 'Default Name....')
    return render(request, 'profile/getcookie.html', {'name':name})

def delcookie(request):
    response = render(request, 'profile/delcookie.html')
    response.delete_cookie('name')
    return response

def setsession(request):
    request.session['name'] = 'alaa'
    return render(request, 'profile/setsession.html')


def getsession(request):
    # name = request.session['name']
    name = request.session.get('name', default='ahmed')
    return render(request, 'profile/getsession.html', {'name':name})


def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    return render(request, 'profile/delsession.html')




def comments(request, id):
    profile = get_object_or_404(Profile, id=id)
    btn = None
    if request.method == 'POST':
        forms = CommentForm(request.POST)
        if forms.is_valid():
            btn = forms.save(commit=False)
            btn.profile = profile
            btn.save()
            return HttpResponseRedirect('/accounts/profiledetails/' + str(profile.id))
    else:
        forms = CommentForm()
    return render(request, 'profile/page.html', {'forms':forms})



def profile(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'profile/home.html', context)


def profile_details(request, id):
    details = Profile.objects.get(id=id)
    is_liked = False
    if details.likes.filter(id=request.user.id).exists():
        is_liked = True

    is_fav = False
    if details.fav.filter(id=request.user.id).exists():
        is_fav = True

    comments = details.comments.all()
    lbl = None
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            lbl = form.save(commit=False)
            lbl.details = details
            lbl.save()
            form = CommentForm()
    else:
        form = CommentForm()
    context = {'details':details, 'is_liked':is_liked, 'is_fav':is_fav, 'comments':comments, 'form':form}
    return render(request, 'profile/profile_details.html', context)



def likes_button(request):
    profiles = get_object_or_404(Profile, id=request.POST.get('details_id'))
    is_liked = False
    if profiles.likes.filter(id=request.user.id).exists():
        profiles.likes.remove(request.user)
        is_liked = False
    else:
        profiles.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect('/accounts/profiledetails/'+ str(profiles.id))


def faves(request, id):
    profile = get_object_or_404(Profile, id=id)
    if profile.fav.filter(id=request.user.id).exists():
        profile.fav.remove(request.user)
    else:
        profile.fav.add(request.user)
    return HttpResponseRedirect('/accounts/profiledetails/' + str(profile.id))

def all_fav(request):
    favs = Profile.objects.filter(fav=request.user)
    context = {'favs':favs}
    return render(request, 'profile/fav.html', context)




