from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from parkfitapi.models import Classes, Difficulty

class UserView(ViewSet):
  def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  

  def retrieve(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
  


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = ('id', 'skillLevel')
  
class ClassesSerializer(serializers.ModelSerializer):
    difficulty = DifficultySerializer(many=False)

    class Meta:
        model = Classes
        fields = ('id', 'name', 'timeDate', 'location',
                'trainer', 'difficulty', 'price')



class UserSerializer(serializers.ModelSerializer):
    my_classes = ClassesSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'password', 'last_login', 'is_superuser', 'username',
                'last_name', 'email', 'is_staff', 'is_active',
                'date_joined', 'first_name', 'groups', 'user_permissions', 'my_classes')