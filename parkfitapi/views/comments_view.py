from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from parkfitapi.models import Comments, Classes


class CommentView(ViewSet):
  def list(self, request):
     
        comments = Comments.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  
  def retrieve(self, request, pk):
        comment = Comments.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

  def create(self, request):
        userId = request.data['user']
        user = User.objects.get(id=userId)
        post = Classes.objects.get(pk=request.data['post'])

        comments = Comments.objects.create(
            review=request.data['review'],
            user=user,
            post=post
            
        )

        serializer = CommentSerializer(comments)
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'last_name', 'first_name')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Comments
        fields = ('id', 'review', 'user', 'post')