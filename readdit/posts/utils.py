from django.db.models import Q
from .models import Votes
from django.db.models.expressions import OuterRef
from django.db.models import Sum


def getVoteState(request, type):

    voteState = Votes.objects.filter(Q(postid=OuterRef(
        'pk')) if type == 'post' else Q(postid=OuterRef(
            'pk')), authorid=request.user.id).values('score')
    voteTotal = Votes.objects.filter(Q(postid=OuterRef(
        'pk')) if type == 'post' else Q(postid=OuterRef(
            'pk'))).values('score').annotate(voteTotal=Sum('score')).values(
        'voteTotal'
    )
    return {
        "voteTotal": voteTotal,
        "voteState": voteState
    }
