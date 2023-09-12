from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parkfitapi.models import Difficulty


class DifficultyView(ViewSet):
  def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        levels = Difficulty.objects.all()
        serializer = DifficultySerializer(levels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  




class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = ('id', 'skillLevel')