from django.shortcuts import render

from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



from to_do_app.models import Exercise
from to_do_app.serializers import TaskSerializer

class TaskApiView(APIView):

    def get(
        self,
        request,
        format=None
    ):
        tasks = Exercise.objects.all()
        serializers = TaskSerializer(tasks, many=True)
        return Response(serializers.data)

    def post(
        self,
        request,
        format=None
    ):
        serializers = TaskSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)