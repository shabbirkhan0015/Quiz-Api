from django.shortcuts import render
from rest_framework.views import APIView
from qv1.models import Question, Quiz
from qv1.serialzers import QuestionSerialzer,QuizSerialzer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class QuizView(APIView):
    def get_object(self):
        try:
            return Quiz.objects.all()
        except Quiz.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self, request, format="None"):
        querySet = self.get_object()
        serialzers = QuizSerialzer(querySet, many=True)
        return Response (data = serialzers.data, status = status.HTTP_200_OK)

    def post(self, request):
        serialzers = QuizSerialzer(data=request.data)
        try:
            if serialzers.is_valid():
                serialzers.save()
                return Response(data = serialzers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response (data=serialzers.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        queryset = Quiz.objects.get(id = request.data['id'])
        queryset.save()
        return Response (data = "delete", status=status.HTTP_410_GONE)

    def put(self, request):
        quiz = Quiz.objects.get(id = request.data['id'])
        serializer = QuizSerialzer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)
