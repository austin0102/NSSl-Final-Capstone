from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parkfitapi.models import Classes, Difficulty, Comments
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.response import Response



class ClassesView(viewsets.ModelViewSet):
    # Assuming TimeDate is the field by which you want to order
    def list(self, request):
        classes = Classes.objects.all()
        token = request.query_params.get("token", None)
        trainer_id = request.query_params.get("trainer", None)

        if token:
            user = Token.objects.get(key=token).user
            classes = classes.filter(trainer=user)

        if trainer_id:
            classes = classes.filter(trainer=trainer_id)

        # Order the classes by the TimeDate field (from newest to oldest)
        classes = classes.order_by('-timeDate')

        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)


    
    def retrieve(self, request, pk):
        classes = Classes.objects.get(pk=pk)
        serializer = ClassesSerializer(classes)
        return Response(serializer.data)
    
    def create(self, request):
        trainer_id = request.data['trainer']
        trainer = User.objects.get(id=trainer_id)
        difficulty = Difficulty.objects.get(pk=request.data['difficulty'])

        classes = Classes.objects.create(
            name=request.data['name'],
            timeDate=request.data['timeDate'],
            location=request.data['location'],
            trainer=trainer,
            difficulty=difficulty,
            price=request.data['price']
        )

        serializer = ClassesSerializer(classes)
        return Response(serializer.data)
    
    def update(self, request, pk):
        

        classes = Classes.objects.get(pk=pk)
        classes.name = request.data["name"]
        classes.timeDate = request.data["timeDate"]
        classes.location = request.data["location"]
        classes.difficulty = Difficulty.objects.get(pk=request.data["difficulty"])
        classes.price = request.data['price']
        classes.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
    
        classes = Classes.objects.get(pk=pk)
        classes.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'username', 'last_name')

class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = ('id', 'skillLevel')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Comments
        fields = ('id', 'review', 'user', 'post')

class ClassesSerializer(serializers.ModelSerializer):
    trainer = UserSerializer(many=False)
    difficulty = DifficultySerializer(many=False)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Classes
        fields = ('id', 'name', 'timeDate', 'location',
                'trainer', 'difficulty', 'price', 'comments')
