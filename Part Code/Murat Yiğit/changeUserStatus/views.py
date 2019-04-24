from django.shortcuts import render, get_object_or_404, redirect
from .models import Clubs, Comments, Events, User
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


def changeUserStatusDetail(request):
    if request.method == 'POST':
        id = request.POST['val']
        obj = get_object_or_404(User, pk = id)
        newIsStaffValue = not obj.is_staff
        obj.is_staff = newIsStaffValue
        obj.save()
    redirect('changeUserStatus')


def changeUserStatus(request):
    allUserObjects = User.objects.all()
    if request.method == 'POST':
        changeUserStatusDetail(request)
    return render(request, 'changeUserStatus.html', {'auth_user': allUserObjects})


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
    return render(request, 'ModeratorPanel.html', {})


def club_details(request, pk):
    club = get_object_or_404(Clubs, pk=pk)
    events = Events.objects.filter(club_id=pk).all()
    comments = Comments.objects.filter(event__in=events)
    return render(request, "KulupDetay.html", {'club_det': club, 'club_event': events, 'comments': comments})


@login_required(login_url='/Login')
@user_passes_test(lambda u: u.is_staff, login_url='/Login')
def page7(request):
    each_club = Clubs.objects.order_by('club_name')
    return render(request, 'edit_club.html', {'each_club': each_club})


@login_required(login_url='/Login')
@user_passes_test(lambda u: u.is_staff, login_url='/Login')
def page8(request):
    return render(request, 'edit_club_detail.html')


@login_required(login_url='/Login')
@user_passes_test(lambda u: u.is_staff, login_url='/Login')
def page9(request):
    clublist = Events.objects.order_by('event_day')
    return render(request, 'edit_event.html', {'clublist': clublist})


@login_required(login_url='/Login')
@user_passes_test(lambda u: u.is_staff, login_url='/Login')
def addclub(request):
    if request.method == "POST" or None:
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            new_club1 = form.save(commit=False)
            new_club1.author = request.user
            new_club1.save()
            return redirect('ModeratorPanel')
    else:
        form = ClubForm()
    return render(request, 'new_club.html', {'form': form})


@login_required(login_url='/Login')
@user_passes_test(lambda u: u.is_staff, login_url='/Login')
def addevent(request):
    if request.method == "POST" or None:
        form1 = EventForm(request.POST)
        if form1.is_valid():
            new_event = form1.save(commit=False)
            new_event.author = request.user
            new_event.save()
            return redirect('ModeratorPanel')
    else:
        form1 = EventForm()
    return render(request, 'new_event.html', {'form1': form1})


@login_required(login_url='/Login')
@user_passes_test(lambda u: u.is_staff, login_url='/Login')
def editclub(request, pk):
    obj = get_object_or_404(Clubs, pk=pk)
    if request.method == "POST":
        club = ClubForm(request.POST, instance=obj)
        if club.is_valid():
            club = club.save(commit=False)
            club.author = request.user
            club.save()
            return redirect('ModeratorPanel')
    else:
        club = ClubForm(instance=obj)
    return render(request, 'edit_club_detail.html', {'club': club, 'club_obj': obj})


@login_required(login_url="/Login")
def change_club_status(request):
    if request.method == "POST":
        status = request.POST.get("status", None)
        pk = request.POST.get("pk", None)
        if status and pk:
            obj = get_object_or_404(Clubs, pk=pk)
            obj.status = status
            obj.save()

    return redirect('ModeratorPanel')


@login_required(login_url='/Login')
@user_passes_test(lambda u: u.is_staff, login_url='/Login')
def editevent(request, pk):
    obj = get_object_or_404(Events, pk=pk)
    if request.method == "POST":
        form = UpdateEventForm(request.POST, instance=obj)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('ModeratorPanel')
    else:
        form = UpdateEventForm(instance=obj)
    return render(request, 'edit_event_detail.html', {'event': form})


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
