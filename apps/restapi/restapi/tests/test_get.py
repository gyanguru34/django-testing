
from restapi.tests import client,status,TestCase,reverse,json,Profile,ProfileSerializers

class TestGet(TestCase):

    # create test database 
    def setUp(self):
        self.casper = Profile.objects.create(
            name='Casper', email="gyan@gyan.com", number=798874654, city='Black')
        
        self.casper2 = Profile.objects.create(
            name='Casper2', email="gy22an@gyan.com", number=798874654, city='Bldfack')
     
    # create test fucnction with name test other wise it wont detect the test case 
    def test_get_all(self):
        # get API response
        response = client.get(reverse('testing_get'))

        # get data from db
        profile = Profile.objects.all()
        serializer = ProfileSerializers(profile, many=True)
        print((serializer))
        # print(serializer.data)

        # assert the test case
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
     
    def test_get_valid_pk(self):
        # get api response 
        response = client.get(reverse('testing_element',kwargs={'pk': self.casper2.pk}))

        # get data from db
        profile=Profile.objects.get(pk=self.casper2.pk)
        serializer_obj=ProfileSerializers(profile)

        # assert the test case
        self.assertEqual(response.data,serializer_obj.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_pk(self):
        # get invalid data response
        response = client.get(
            reverse('testing_element', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        

