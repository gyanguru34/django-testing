
from apps.restapi.tests import client,status,TestCase,reverse,json,Profile,ProfileSerializers


class DeleteSingleTest(TestCase):
    """ Test module for deleting an existing puppy record """

    def setUp(self):
        self.casper = Profile.objects.create(
            name='Casper', email="gyan@gyan.com", number=798874654, city='Black')
        self.casper2 = Profile.objects.create(
            name='Casper2', email="gy22an@gyan.com", number=798874654, city='Bldfack')

    def test_valid_delete(self):
        response = client.delete(
            reverse('testing_element', kwargs={'pk': self.casper2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete(self):
        response = client.delete(
            reverse('testing_element', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)