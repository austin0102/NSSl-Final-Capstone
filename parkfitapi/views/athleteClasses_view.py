
from django.contrib.auth.models import User
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from parkfitapi.models import AthleteClasses, Athlete, Classes, Difficulty


class athleteClassesView(ViewSet):
    def list(self, request):
        token = request.query_params.get("token")  # Get the token from query parameters
        if token is not None:
            try:
                user = Token.objects.get(key=token).user
                classes = AthleteClasses.objects.filter(athlete=user)
                serializer = athleteClassesSerializer(classes, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Token.DoesNotExist:
                return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # If token is not provided in query parameters, return all AthleteClasses
            classes = AthleteClasses.objects.all()
            serializer = athleteClassesSerializer(classes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        
    def create(self, request):
        # Extract athlete_id and class_attended_id from the request data
        athlete_id = request.data['athlete']
        athlete = User.objects.get(id=athlete_id)
        class_attended_id = request.data['class_attended']
        class_attended = Classes.objects.get(id=class_attended_id)

        try:
            # Create a new AthleteClasses object
            athlete_class = AthleteClasses.objects.create(
                athlete=athlete,
                class_attended=class_attended
            )
            serializer = athleteClassesSerializer(athlete_class)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')

class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = ('id', 'skillLevel')

class ClassesSerializer(serializers.ModelSerializer):
    trainer = UserSerializer(many=False)
    difficulty = DifficultySerializer(many=False)

    class Meta:
        model = Classes
        fields = ('id', 'name', 'timeDate', 'location',
                'trainer', 'difficulty', 'price')


class athleteClassesSerializer(serializers.ModelSerializer):
    class_attended = ClassesSerializer(many=False)
    class Meta:
        model = AthleteClasses
        fields = ('id', 'athlete', 'class_attended')
