# django imports
from django.test import TestCase, Client
from django.urls import reverse

# rest import
import json
from rest_framework import status

# file import 
from restapi.models import Profile
from restapi.serializers import ProfileSerializers


# initialize the APIClient app
client = Client()