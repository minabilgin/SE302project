from django.shortcuts import render, get_object_or_404, redirect
from .models import Clubs, Comments, Events
from .forms import ClubForm, EventForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


def anasayfa(request):
    if request.method == "POST":
        logout(request)
        return redirect('anasayfa')
    each_club = Clubs.objects.order_by('club_name')
    clublist = Events.objects.order_by('event_day')
    return render(request, 'anasayfa.html', {'clublist': clublist, 'each_club': each_club})


def page1(request):
    if request.method == "POST":
        logout(request)
        return redirect('anasayfa')
    each_club = Clubs.objects.order_by('club_name')
    return render(request, 'kulupler.html', {'each_club': each_club})


def page4(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('anasayfa')
    else:
        form = AuthenticationForm()
    return render(request, 'Login.html', {'form': form})


def page5(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('anasayfa')
    else:
        form = UserCreationForm()
    return render(request, 'Register.html', {'form': form})


@login_required(login_url='/Login')
@user_passes_test(lambda u: u.is_staff, login_url='/Login')
def page6(request):
    if request.method == "POST":
        logout(request)
        return redirect('anasayfa')
    return render(request, 'ModeratorPanel.html', {})


def club_details(request, pk):
    if request.method == "POST":
        logout(request)
        return redirect('anasayfa')
    club = get_object_or_404(Clubs, pk=pk)
    events = Events.objects.filter(club_id=pk).all()
    comments = Comments.objects.filter(event__in=events)
    return render(request, "KulupDetay.html", {'club_det': club, 'club_event': events, 'comments': comments})


@login_required(login_url='/Login')
def page3(request):
    if request.method == "POST":
        logout(request)
        return redirect('anasayfa')
    return render(request, 'Favori Kulüpler.html', {})


@login_required(login_url='/Login')
def adding_comment(request, pk):
    obj = get_object_or_404(Events, pk=pk)
    if request.method == "POST":
        comment = request.POST['comment']
        if comment is not None:
            user = request.user
            instance = Comments(user=user, event_id=pk, comment=comment)
            instance.save()
            return redirect('anasayfa')
    return render(request, 'add_comment.html', {'event': obj})
