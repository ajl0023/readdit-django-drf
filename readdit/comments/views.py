import json
from rest_framework import permissions

from rest_framework.views import APIView
from comments.forms import ReplyForm
from posts.models import Votes

from django.http.response import HttpResponse
from comments.forms import CommentForm
from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.renderers import TemplateHTMLRenderer


class NewComment(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):

        form = CommentForm(request.POST)
        print(form)
        replyForm = ReplyForm(request.POST)
        renderer_classes = [TemplateHTMLRenderer]
        print(form.is_valid())
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user

            comment = form.save()

            comment.voteState = 1
            comment.voteTotal = 1
            vote = Votes(authorid=request.user, commentid=comment, score=1)
            vote.save()
            print(comment.content)
            

            # return HttpResponseRedirect('/thanks/')
        else:
            return

        # form = NameForm()
    # return render(request, 'name.html', {'form': form})
