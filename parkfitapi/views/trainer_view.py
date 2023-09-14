from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from parkfitapi.models import Trainer

class TrainerView(ViewSet):
  def list(self, request):
     
        Trainers = Trainer.objects.all()
        serializer = TrainerSerializer(Trainers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  
  def retrieve(self, request, pk):
        Trainers = Trainer.objects.get(pk=pk)
        serializer = TrainerSerializer(Trainers)
        return Response(serializer.data)
  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'last_login', 'is_superuser', 'username',
                'last_name', 'email', 'is_staff', 'is_active',
                'date_joined', 'first_name', 'groups', 'user_permissions')

class TrainerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Trainer
        fields = ('id','user')