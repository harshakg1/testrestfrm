from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
 
from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.views import APIView


#@api_view(['GET', 'POST', 'DELETE'])
class TutorialList(APIView):

    def post(self, request):
        # GET list of tutorials, POST a new tutorial, DELETE all tutorials

       
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():

            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_201_CREATED)


    def get(self, request):
    
        tutorials = Tutorial.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return Response(tutorials_serializer.data)
        # 'safe=False' for objects serialization        

           
 


