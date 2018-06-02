from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API view"""

    def get(self,request,format=None):
        """returns a list of APIView feature"""

        an_apiview =[
        'Uses http methods as functions (get,post,put,patch,delete)',
        'It is similar to a traditional django view'
        'Gives you the most control over your logic',
        'Is mapped manually to urls'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})
