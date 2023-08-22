# django imports
from django.test import TestCase, Client
from django.urls import reverse

# rest import
import json
from rest_framework import status

# file import 
from apps.restapi.models import Profile
from apps.restapi.serializers import ProfileSerializers


# initialize the APIClient app
client = Client()