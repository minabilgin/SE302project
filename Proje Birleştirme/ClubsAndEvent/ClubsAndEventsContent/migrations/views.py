def club_details(request, pk):
    club = get_object_or_404(Clubs, pk=pk)
    events = Events.objects.filter(club_id=pk).all()
    comments = Comments.objects.filter(event__in=events)
    return render(request, "KulupDetay.html", {'club_det': club, 'club_event': events, 'comments': comments})


def page1(request):
    if request.method == "POST":
        logout(request)
        return redirect('anasayfa')
    each_club = Clubs.objects.order_by('club_name')
    return render(request, 'kulupler.html', {'each_club': each_club})