from django.shortcuts import render, HttpResponse
from django.template import loader


from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser 
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view

from .models import Profile
from .serializers import ProfileSerializers
import io
# Create your views here.


@api_view(['GET', 'POST'])
def testing_get(request):
    if request.method == "GET":
        result = Profile.objects.all()
        results = ProfileSerializers(result, many=True)
        print(results.data)
        return Response(results.data)

    if request.method == 'POST':
        # converting the byte data to stream 
        json_data = request.body
        print('direct data is ', (json_data))
        stream = io.BytesIO(json_data)
        print("stream", (stream))

        #parsing the data to python dic
        pythondata = JSONParser().parse(stream)
        print(type(pythondata))

        # serilizing the data from python to complex dataype 
        serial = ProfileSerializers(data=pythondata)

        #validating the  data before serialization 
        if serial.is_valid():
            serial.save()
            res = {'msg': 'Data Created'}

            json_data = JSONRenderer().render(res)
            return HttpResponse(
                json_data, content_type='application/json',status=status.HTTP_201_CREATED
            )
        
        json_data = JSONRenderer().render(serial.errors)
        return HttpResponse(
            json_data, content_type='application/json',status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def testing_element(request,pk):

    try:
        singleProfile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        results = ProfileSerializers(singleProfile)
        print(results.data)
        return Response(results.data)    
    
    elif request.method == 'PUT':
        #creating the byte data to stream
        json_data = request.body
        print('direct data is ', (json_data))
        stream = io.BytesIO(json_data)
        print("stream", (stream))

        # parsing the data to python dic 
        data = JSONParser().parse(stream)

        #serializerr the data 
        serial= ProfileSerializers(data=data)

        # serilizer object is validating 
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_204_NO_CONTENT)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        singleProfile.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

