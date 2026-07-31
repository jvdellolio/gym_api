from gc import get_objects

from django.http import Http404
from django.shortcuts import get_object_or_404

from config.api.models import Exercise
from config.api.serializers import ExerciseSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
 

class ExerciseList(APIView):
    def get(self, request):
        try:
            name = request.query_params.get('name')
            category = request.query_params.get('category')
            exercise = Exercise.objects.all()
            if name:
                exercise = exercise.filter(name__icontains=name)
            if category:
                exercise = exercise.filter(category__icontains=category)
            serializer = ExerciseSerializer(exercise, many=True)
            return Response(serializer.data, status=200)
        except Exception as exc:
            return Response(f"Ocorreu um erro inesperado:{exc}", status=500)
        
    def post(self, request):
        try:
            serializer = ExerciseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Exception as exc:
            return Response(f"Ocorreu um erro inesperado:{exc}", status=500)   
        
class ExerciseDetail(APIView):
    def get_object(self, pk):
            try:
                return get_object_or_404(Exercise, pk=pk) 
            except Http404:
                raise Http404("Exercício não encontrado")
    #def de detalhes
    def get(self, request, pk):
        try:
            exercise = self.get_object(pk)
            serializer = ExerciseSerializer(exercise)
            return Response(serializer.data, status=200)
        except Exception as exc:
            return Response(f"Ocorreu um erro inesperado:{exc}", status=500)
        
    def patch(self, request, pk):
        try:
            exercise = self.get_object(pk)
            serializer = ExerciseSerializer(exercise, data=request.data)
            if serializer.is_valid(partial=True):
                serializer.save()
                return Response(status=204)
            return Response(serializer.errors, status=400)
        except Exception as exc:
            return Response(f"Ocorreu um erro inesperado:{exc}", status=500)

    def delete(self, request, pk):
        try:
            exercise = self.get_object(pk)
            exercise.delete()
            return Response(status=204)
        except Exception as exc:
            return Response(f"Ocorreu um erro inesperado:{exc}", status=500)
    