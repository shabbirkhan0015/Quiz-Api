from rest_framework.serializers import ModelSerializer
from qv1.models import Quiz, Question

class QuizSerialzer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerialzer(ModelSerializer):
    class Meta:
        model = Question
        field = '__all__'