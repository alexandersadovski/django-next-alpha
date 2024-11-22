from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from next.matches.models import Match


@login_required
def list_matches(request):
    matches = Match.objects.filter(user1=request.user) | Match.objects.filter(user2=request.user)
    return render(request, 'dashboard/matches.html', context={'matches': matches})
