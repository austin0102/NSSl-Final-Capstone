from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class TokenView(ViewSet):
  def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        tokens = Token.objects.all()
        serializer = TokenSerializer(tokens, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  
  def retrieve(self, request, pk):
        token = Token.objects.get(pk=pk)
        serializer = TokenSerializer(token)
        return Response(serializer.data)
  
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('user', 'pk')