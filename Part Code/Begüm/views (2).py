from django.shortcuts import render, get_object_or_404, redirect
from .models import Clubs, Comments, Events
from .forms import ClubForm, EventForm, CommentForm, UpdateEventForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


def anasayfa(request):
    each_club = Clubs.objects.order_by('club_name')
    clublist = Events.objects.order_by('event_day')
    q = request.GET.getlist("q", None)
    if q is not None and len(q) != 0:
        clublist = Events.objects.filter(club__club_name__in=q).all()
    return render(request, 'anasayfa.html', {'clublist': clublist, 'each_club': each_club})


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


def allcomments(request):
    commentslist = Comments.objects.order_by('status')
    return render(request, 'allcomments.html', {'commentslist': commentslist})


def user_logout(request):
    if request.method == "POST":
        logout(request)
    return redirect('anasayfa')


def allcomments_details(request, pk):
    obj = get_object_or_404(Comments, pk=pk)
    if request.method == "POST":
        comment = CommentForm(request.POST, instance=obj)
        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('allcomments')
    else:
        comment = CommentForm(instance=obj)
    return render(request, 'allcomments_detail.html', {'comment': comment})
