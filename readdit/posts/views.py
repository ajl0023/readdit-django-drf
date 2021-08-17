from django.db.models.aggregates import Sum
from rest_framework.authentication import TokenAuthentication
from rest_framework.serializers import Serializer
from posts.models import Comments, Votes
from posts.serializers import SinglePostSerializer
from posts.utils import getVoteState
from posts import views
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from posts.serializers import PostSerializer
from posts.models import Posts
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.expressions import Case, F, OuterRef, Subquery, Value, When, Window
from django.db.models.functions import Coalesce, DenseRank
import json


class PostList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def get(self, request, format=None):

        voteDict = getVoteState(request, 'post')

        posts = Posts.objects.annotate(voteTotal=Coalesce(voteDict.get("voteTotal"), 0), voteState=Coalesce(
            voteDict.get("voteState"), 0), className=Case(When(voteState__gt=0, then=Value('vote-state-active')), default=Value("")))

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class SinglePost(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = [TokenAuthentication]

    def get(self, request, id, format=None):
        post = Posts.objects.prefetch_related('comments')
        print(post.query)

        # voteDict = getVoteState(request, 'post')

        # post = Posts.objects.prefetch_related('comments').annotate(voteTotal=Coalesce(voteDict.get("voteTotal"), 0), voteState=Coalesce(
        #     voteDict.get("voteState"), 0)).get(id=id)

        # comments = post.comments.annotate(bucket=Window(expression=DenseRank(),
        #                                      order_by=F('depth').asc()), voteTotal=Coalesce(Votes.objects.filter(commentid=OuterRef('pk')).values('score').annotate(voteTotal=Sum('score')).values(
        #                                          'voteTotal'
        #                                      ), 0), voteState=Coalesce(Votes.objects.filter(commentid=OuterRef(
        #                                          'pk'), authorid=request.user.id).values('score'), 0))
        # print(comments[0].voteState)
        # print(post.comments.all()[0].voteState)
        # serializer = SinglePostSerializer(post)
        # print(serializer)
        # return Response(serializer.data)


class Vote(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request,  format=None):
        data = json.loads(request.body)

        voteType = data.get('type')
        model = Posts.objects.get(id=data.get(
            "postid")) if voteType == 'post' else Comments.objects.get(id=data.get("commentid"))
        user = request.user
        try:
            obj = Votes.objects.get(postid=model, authorid=user) if voteType == 'post' else Votes.objects.get(
                commentid=model, authorid=user)

            obj.score = Case(When(score=-1, then=Value(1)), When(score=1, then=Value(0)),
                             When(score=0, then=Value(1)), default=0) if data.get('score') == 1 else Case(When(score=-1, then=Value(0)), When(score=1, then=Value(-1)),
                                                                                                          When(score=0, then=Value(-1)), default=0)

            obj.save()
            obj.refresh_from_db()
            print(obj.score)
            voteTotal = Votes.objects.filter(postid=model).annotate(
                voteTotal=Sum('score')).values('voteTotal') if voteType == 'post' else Votes.objects.filter(commentid=model).annotate(
                voteTotal=Sum('score')).values('voteTotal')

            responseObj = {
                "voteTotal": voteTotal[0].get("voteTotal"),
                "voteState": obj.score
            }

            return Response(responseObj)
        except Votes.DoesNotExist:
            obj = Votes(postid=model, authorid=user,
                        score=1 if data.get('score') == 1 else -1) if voteType == 'post' else Votes(commentid=model, authorid=user,
                                                                                                    score=1 if data.get('score') == 1 else -1)

            obj.save()
            voteTotal = Votes.objects.filter(postid=model).annotate(
                voteTotal=Sum('score')).values('voteTotal') if voteType == 'post' else Votes.objects.filter(commentid=model).annotate(
                voteTotal=Sum('score')).values('voteTotal')

            return Response({"voteState": 1, "voteTotal": voteTotal[0].get("voteTotal"), })
