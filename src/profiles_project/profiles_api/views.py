from django.shortcuts import render

from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from . import serializers
from . import models
from . import permissions

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


class HelloViewSet(viewsets.ViewSet):
    """Test Api ViewSets"""

    serializer_class = serializers.HelloSerializer


    def list(self,request):
        """Returns a hello message"""
        a_viewset = [
            'Uses actions (list,create, retrive, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'

        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})


    def create(self,request):
        """create a new hello message"""

        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message ='Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrive(self,request,pk=None):

        """handles objext by id"""

        return Response({'http-method':'get'})

    def update(self,request,pk=None):

        """update objext by id"""

        return Response({'http-method':'Put'})

    def partial_update(self,request,pk=None):

        """partialy update objext by id"""

        return Response({'http-method':'Patch'})

    def destroy(self,request,pk=None):

        """delete objext by id"""

        return Response({'http-method':'Delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ handles creating and updating  profiles"""

    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.object.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
