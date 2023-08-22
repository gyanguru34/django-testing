
# # django imports
# from django.test import TestCase, Client
# from django.urls import reverse

# # rest import
# import json
# from rest_framework import status

# # file import 
# from .models import Profile
# from .serializers import ProfileSerializers


# # initialize the APIClient app
# client = Client()


# class TestGet(TestCase):

#     # create test database 
#     def setUp(self):
#         self.casper = Profile.objects.create(
#             name='Casper', email="gyan@gyan.com", number=798874654, city='Black')
        
#         self.casper2 = Profile.objects.create(
#             name='Casper2', email="gy22an@gyan.com", number=798874654, city='Bldfack')
     
#     # create test fucnction with name test other wise it wont detect the test case 
#     def test_get_all(self):
#         # get API response
#         response = client.get(reverse('testing_get'))

#         # get data from db
#         profile = Profile.objects.all()
#         serializer = ProfileSerializers(profile, many=True)
#         print((serializer))
#         # print(serializer.data)

#         # assert the test case
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
     
#     def test_get_valid_pk(self):
#         # get api response 
#         response = client.get(reverse('testing_element',kwargs={'pk': self.casper2.pk}))

#         # get data from db
#         profile=Profile.objects.get(pk=self.casper2.pk)
#         serializer_obj=ProfileSerializers(profile)

#         # assert the test case
#         self.assertEqual(response.data,serializer_obj.data)

#     def test_get_invalid_pk(self):
#         # get invalid data response
#         response = client.get(
#             reverse('testing_element', kwargs={'pk': 30}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        


# class TestPost(TestCase):
#     """ Test module for inserting a new puppy """

#     def setUp(self):
#         self.valid_payload = {
#             'name': 'Muffin',
#             'email': "abc@abc.com",
#             'number': 123456789,
#             'city': 'White'
#         }
#         self.invalid_payload = {
#             'name': " ",
#             'email': "abcs@abcs.com",
#             'number': 123456789,
#             'city': 'White'
#         }

#     def test_create_valid_post(self):
#         response = client.post(
#             reverse('testing_get'),
#             data=json.dumps(self.valid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_create_invalid_post(self):
#         response = client.post(
#             reverse('testing_get'),
#             data=json.dumps(self.invalid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



# class UpdateSingleTest(TestCase):
#     """ Test module for updating an existing puppy record """

#     def setUp(self):
#         self.casper = Profile.objects.create(
#             name='bakurs', email='xyz@xyx.com', number=1111111, city='white')
#         self.muffin = Profile.objects.create(
#             name='Muffy', email='xyz@xyx.com', number=1111111, city='white')
        
#         self.valid_payload = {
#             'name': 'bakurs',
#             'email': 'xyz@xyx.com',
#             'number': 1111111,
#             'city': 'White'
#         }
#         self.invalid_payload = {
#             'name': '',
#             'email': 4,
#             'number': 'Pamerion',
#             'city': 'White'
#         }

#     def test_valid_update_puppy(self):
#         response = client.put(
#             reverse('testing_element', kwargs={'pk': self.muffin.pk}),
#             data=json.dumps(self.valid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     def test_invalid_update_puppy(self):
#         response = client.put(
#             reverse('testing_element', kwargs={'pk': self.muffin.pk}),
#             data=json.dumps(self.invalid_payload),
#             content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        
        
