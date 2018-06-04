from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """returns a list of APIView feature"""

        an_apiview =[
        'Uses http methods as functions (get,post,put,patch,delete)',
        'It is similar to a traditional django view'
        'Gives you the most control over your logic',
        'Is mapped manually to urls'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(get,request):
        """create a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message':message})

        else:
             return Response(
                serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handle updating an oject"""

        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """patch request only update fields required"""

        return Response({'method':'patch'})


    def delete(self, request, pk=None):
        """delete an oject"""

        return Response({'method':'delete'})        
