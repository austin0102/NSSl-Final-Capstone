from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User

class UserView(ViewSet):
  def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        tags = User.objects.all()
        serializer = UserSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'last_login', 'is_superuser', 'username',
                'last_name', 'email', 'is_staff', 'is_active',
                'date_joined', 'first_name', 'groups', 'user_permissions')